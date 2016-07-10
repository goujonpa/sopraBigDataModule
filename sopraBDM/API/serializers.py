from rest_framework import serializers
from API.models import Employee, Widget, Notation


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'pk',
            'last_name',
            'first_name',
            'birth_date',
            'joined_date',
            'salary',
            'phone',
            'performance_indice',
            'gender',
            'children_number',
            'adress',
            'mail',
            'married'
        )


class WidgetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Widget
        fields = (
            'pk',
            'name',
            'author',
            'description'
        )


class NotationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Notation
        fields = (
            'pk',
            'employee',
            'widget',
            'rating'
        )
