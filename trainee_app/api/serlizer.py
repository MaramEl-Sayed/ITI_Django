from rest_framework import serializers
from course_app.models import Course  
from ..models import Trainee
class Trainee_ser(serializers.Serializer):
    
    id=serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    age = serializers.IntegerField()
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    @classmethod
    def serlize_all(cls):
        return cls(Trainee.getalltrainees(),many=True).data
    @classmethod
    def getby_id(cls,id):
        return Trainee_ser(instance=Trainee.gettraineebyid(id)).data
    @classmethod
    def delete(cls,id):
        Trainee.objects.filter(id=id).delete()
        return True
    @classmethod
    def getupdateTrainee(cls,id,data):
        oldobj=Trainee.gettraineebyid(id)
        return Trainee_ser(instance=oldobj,data=data)


    def create(self,validate_data):
       obj= Trainee()
       obj.name=validate_data['name']
       obj.email=validate_data['email']
       obj.age=validate_data['age']
       obj.course=validate_data['course']
       obj.save()
       return obj
    
    def update(self,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.email=validate_data.get('email',instance.email)
        instance.age=validate_data.get('age',instance.age)
        instance.course=validate_data.get('course',instance.course)
        instance.save()
        return instance