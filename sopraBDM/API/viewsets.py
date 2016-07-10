import json
import subprocess

from django.core import serializers


from API.models import Employee, Widget, Notation
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

    @detail_route()
    def recommend_widgets(self, request, pk=None):
        "Uses the RLib module to predict the best widgets for user with pk = pk"

        # try:
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
        # except Exception as e:
        #     r = Response({
        #         "status": "FAILED",
        #         "message": str(e)
        #     })

        return r


class WidgetViewSet(viewsets.ModelViewSet):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer


class NotationViewSet(viewsets.ModelViewSet):
    queryset = Notation.objects.all()
    serializer_class = NotationSerializer
