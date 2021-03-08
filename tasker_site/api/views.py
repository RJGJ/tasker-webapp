from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def api_detail(request):
	data = "API BASE DIR"
	return JsonResponse(data, safe=False)
