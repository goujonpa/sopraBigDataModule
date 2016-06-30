from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core import serializers

import json
import subprocess
from API.models import Employee, Widget, Notation


class HWView(View):
    """Hello World API View"""

    def get(self, request):
        """Returns a JSON Response saying "Hello World"""
        return JsonResponse({"response": "Hello World !"})


class InitDBView(View):
    """Init DB API View"""

    def post(self, request):
        """Adds an object to DB"""

        try:
            post_data = json.loads(request.body)
            if post_data['object'] == 'employee':
                att = post_data['attributes']
                new = Employee(**att)
                new.save()
            elif post_data['object'] == 'widget':
                att = post_data['attributes']
                new = Widget(**att)
                new.save()
            elif post_data['object'] == 'notation':
                att = post_data['attributes']
                employee = Employee.objects.get(pk=att['employee'])
                widget = Widget.objects.get(pk=att['widget'])
                rating = att['rating']
                new = Notation(employee=employee, widget=widget, rating=rating)
                new.save()
            print(str(post_data))
            r = JsonResponse({"status": "OK"})
        except Exception as e:
            r = JsonResponse({
                "status": "FAILED",
                "message": str(e)
            })

        return r


class EmployeeTrainView(View):
    """Returns a prediction for an employee"""

    def get(self, request):
        """Returns the prediction as a JSON response"""
        try:
            cmd = "R CMD BATCH ./RLib/train_employee_model.R"
            subprocess.call(cmd, shell=True)

            r = JsonResponse({
                "status": "OK",
            })
        except Exception as e:
            r = JsonResponse({
                "status": "FAILED",
                "message": str(e)
            })

        return r


class EmployeePredictView(View):
    """Returns a prediction for an employee"""

    def get(self, request):
        """Returns the prediction as a JSON response"""
        try:
            post_data = json.loads(request.body)
            employee_id = post_data['id']
            max_length = post_data['max_length']
            notations = serializers.serialize("json", Notation.objects.filter(
                employee__id=employee_id
            ))
            notations = json.loads(notations)
            l = list()
            for instance in notations:
                l.append([
                    instance['fields']['employee'],
                    instance['fields']['widget'],
                    instance['fields']['rating']]
                )
            with open("./RLib/employee_predict_in.json", "write") as f:
                f.write(json.dumps(l))

            cmd = "R CMD BATCH ./RLib/employee_predict.R"
            subprocess.call(cmd, shell=True)

            r = JsonResponse({
                "status": "OK",
            })
        except Exception as e:
            r = JsonResponse({
                "status": "FAILED",
                "message": str(e)
            })

        return r
