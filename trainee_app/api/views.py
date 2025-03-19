from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serlizer import Trainee_ser

@api_view(['GET','POST'])
def getAll(request):
    if (request.method=='GET'):
        return Response(
            data={'trainees': Trainee_ser.serlize_all()},
        )
    else:
        json_data = request.data
        trainee_ser_obj=Trainee_ser(data=json_data)
        if(trainee_ser_obj.is_valid()):
            trainee_ser_obj.save()
            return Response(
                data=trainee_ser_obj.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                data={'errors':trainee_ser_obj.errors},status=status.HTTP_400_BAD_REQUEST)
            
@api_view(['GET','PUT','DELETE','PATCH'])
def getbyid_update_delete(req,id):
    if(req.method=='GET'):
        return Response(
            data=Trainee_ser.getby_id(id),
            status=status.HTTP_200_OK
        )
    elif(req.method=='DELETE'):
        if(Trainee_ser.delete(req,id)):
            return Response(
                data={'message':'Trainee deleted successfully'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={'message':'Trainee not found'},
                status=status.HTTP_404_NOT_FOUND
            )
    elif(req.method=='PUT'):  
        json_data=req.data
        serobj=Trainee_ser.getupdateTrainee(id,json_data)
        if(serobj.is_valid()):
            serobj.save()
            return Response(
                data=serobj.data,
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={'errors':serobj.errors},
                status=status.HTTP_400_BAD_REQUEST
            )


