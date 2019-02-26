from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class FibonacciSerializer(serializers.ModelSerializer):
	f0 = serializers.IntegerField(min_value=0, required=True)
	f1 = serializers.IntegerField(min_value=1, required=True)
	N = serializers.IntegerField(min_value=1, required=True)
	result = serializers.SerializerMethodField()
	
	fib_number = None
	def validate(self , data):
		f0 = data.get('f0', 0)
		f1 = data.get('f1', None)
		n = data.get('N', None)
	
		if not f1:
			raise ValidationError("F1 is required.")	

		if not n:
			raise ValidationError("N is required.")
		
		return data	
	def get_result(self, data):
		f0 = data.get('f0', None)
		f1 = data.get('f1', None)
		n = data.get('N', None)
		i=2
		while i<n:
		    f0,f1 = f1,f0+f1
		    i += 1
		return f1
	class Meta:
		model = User
		fields = ('f0', 'f1', 'N', 'result')
				