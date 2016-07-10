"""sopraBDM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))


REST or not REST ?
- Extra action for routing on a single employee yes rest ...

"""

from django.conf.urls import url, include
from django.contrib import admin
from API.views import HWView, EmployeeTrainView, EmployeePredictView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from API.viewsets import EmployeeViewSet, WidgetViewSet, NotationViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'widgets', WidgetViewSet)
router.register(r'notations', NotationViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'hw/$', HWView.as_view()),
    url(r'employee_train/$', EmployeeTrainView.as_view()),
    url(r'employee_predict/$', EmployeePredictView.as_view()),
    url(r'api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework'
    ))
]
