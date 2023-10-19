from app1.models import blogmodel
from rest_framework import serializers

class blogserializer(serializers.ModelSerializer):
	id=serializers.IntegerField()
	title=serializers.CharField(max_length=100)
	body=serializers.CharField(max_length=200)

	class Meta:
		model=blogmodel
		fields=('__all__')  