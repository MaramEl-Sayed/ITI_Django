from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.response import Response
from rest_framework import status
from .serlizer import Course_ser
from rest_framework import generics
from ..models import Course
from rest_framework.viewsets import ViewSet,ModelViewSet

class Course_List_Create(APIView):
    def get(self,req):
        return Response(
            data={'courses': Course_ser.serialize_all()},status=HTTP_200_OK

        )
    def post(self,req):
        serobj = Course_ser(data=req.data)
        if serobj.is_valid():
            serobj.save()
            return Response(
                data=serobj.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data=serobj.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class Course_get_update_delete(APIView): 
    def get(self,req,id):
        return Response(
            data={'course': Course_ser.getbyid(id)},
            status=status.HTTP_200_OK)
    def put(self,req,id):
        course = Course_ser.getbyid(id)
        serobj = Course_ser(course,data=req.data)
        if serobj.is_valid():
            serobj.save()
            return Response(
                data=serobj.data,
                status=status.HTTP_200_OK
            )
        return Response(
            data=serobj.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,req,id):
        course = Course_ser.getbyid(id)
        course.delete()
        return Response(
            data={},
            status=status.HTTP_204_NO_CONTENT
        )

        
class Course_List_Create_Generic(generics.ListCreateAPIView):
    queryset = Course.getallcourses()
    serializer_class = Course_ser

class Course_get_update_delete_Generic(generics.RetrieveUpdateDestroyAPIView):
    queryset=Course.getallcourses()
    serializer_class = Course_ser

class CourseModelViewSet(ModelViewSet):
    queryset=Course.getallcourses()
    serializer_class = Course_ser






