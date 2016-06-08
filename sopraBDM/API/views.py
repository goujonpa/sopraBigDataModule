from django.shortcuts import render
from django.views.generic import View 
from django.http import JsonResponse

# Create your views here.

class HWView(View):
    """Hello World API View"""

    def get(self, request):
        """Returns a JSON Response saying "Hello World"""
        return JsonResponse({"response": "Hello World !"});

