from rest_framework import serializers
from ..models import *

class Course_ser(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)  
    # name = serializers.CharField(max_length=255, required=True)  
    # description = serializers.CharField(max_length=500, required=True)  

    class Meta:
        model=Course
        fields='__all__'

    @classmethod
    def get_all(cls):
        return cls(Course.getallcourses(), many=True).data
    
    @classmethod
    def getbyid(cls, id):
    
        return Course.getcoursebyid(id)
 
