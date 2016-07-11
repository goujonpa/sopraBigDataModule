import json
import subprocess
import datetime
from django.core import serializers


from celery import Task
from API.models import Employee, Widget, Notation
from API.serializers import (
    EmployeeSerializer,
    WidgetSerializer,
    NotationSerializer
)


class TrainRecommender(Task):
    queue = "train"

    def run(self):
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
