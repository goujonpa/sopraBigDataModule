import json
import subprocess

from django.core import serializers


from API.models import Employee, Widget, Notation
from API.tasks import TrainRecommender
from API.serializers import (
    EmployeeSerializer,
    WidgetSerializer,
    NotationSerializer
)
from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from rest_framework.response import Response


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @list_route()
    def train(self, request):
        notations = serializers.serialize("json", Notation.objects.all())
        notations = json.loads(notations)
        l = list()
        for instance in notations:
            l.append([
                instance['fields']['employee'],
                instance['fields']['widget'],
                instance['fields']['rating']
            ])
        with open("./RLib/json/train_employee_widget_in.json", "write") as f:
            f.write(json.dumps(l))

        counts = {
            'employees': Employee.objects.count(),
            'widgets': Widget.objects.count(),
            'notations': Notation.objects.count()
        }

        with open("./RLib/json/train_counts_in.json", "write") as f:
            f.write(json.dumps(counts))

        cmd = "R CMD BATCH ./RLib/train_employee_model.R ./RLib/rout/train_employee_model.Rout"
        subprocess.call(cmd, shell=True)

        counts.update({'status': 'OK'})

        return Response(counts)

    @detail_route()
    def recommend_widgets(self, request, pk=None):
        "Uses the RLib module to predict the best widgets for user with pk = pk"

        req_data = request.GET
        employee_id = pk
        max_length = req_data['max_length']
        notations = serializers.serialize("json", Notation.objects.filter(
            employee__id=employee_id
        ))
        notations = json.loads(notations)
        l = list()
        for instance in notations:
            l.append([
                instance['fields']['employee'],
                instance['fields']['widget'],
                instance['fields']['rating']
            ])
        with open("./RLib/json/employee_predict_in.json", "write") as f:
            f.write(json.dumps(l))

        cmd = "R CMD BATCH ./RLib/employee_predict.R ./RLib/rout/employee_predict.Rout"
        subprocess.call(cmd, shell=True)

        with open("./RLib/json/employee_predict_out.json") as f:
            prediction = json.loads(f.read())

        r = Response({
            "status": "OK",
            "prediction": prediction
        })

        return r


class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class NotationViewSet(viewsets.ModelViewSet):
    queryset = Notation.objects.all()
    serializer_class = NotationSerializer
