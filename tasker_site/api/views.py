from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.authentication import TokenAuthentication


# Create your views here.
@api_view(['GET'])
def api_detail(request):
	data = {
		'API Overview': 'api/',
		'Task ': '',
	}
	return JsonResponse(data, safe=False)
