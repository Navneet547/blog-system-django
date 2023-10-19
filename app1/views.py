from django.shortcuts import render
from rest_framework.views import APIView  
from rest_framework.response import Response 
from rest_framework import status   
from django.views import View
from app1.models import blogmodel
from app1.serializers import blogserializer
from django.shortcuts import get_object_or_404
# Create your views here.
class blogview(View):
	def get(self,request):
		data=blogmodel.objects.all()
		context={
		'data':data,
		}
		return render(request,'index.html',context)


class blogserializerview(APIView):
	def get(self,request):
		data=blogmodel.objects.all()
		serializer=blogserializer(data,many=True)
		return Response({'status':'success','data':serializer.data}, status=status.HTTP_200_OK)

	def post(self, request):  
	    serializer = blogserializer(data=request.data)  

	    if serializer.is_valid():  
	        serializer.save()  
	        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
	    else:  
	        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
	def put(self, request):
	    data = request.data
	    student_id = data.get('id')

	    try:
	        student = blogmodel.objects.get(id=student_id)
	    except blogmodel.DoesNotExist:
	        return Response({"status": "error", "message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

	    serializer = blogserializer(student, data=data)
	    if serializer.is_valid():
	        serializer.save()
	        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
	    else:
	        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):   
	    data = request.data
	    data_id = data.get('id')

	    try:
	        blog = blogmodel.objects.get(id=data_id)
	        blog.delete()
	        return Response({"status": "success", "message": "Student deleted successfully"}, status=status.HTTP_200_OK)
	    except blogmodel.DoesNotExist:
	        return Response({"status": "error", "message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
