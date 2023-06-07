from django.http import JsonResponse, HttpResponse
import json

from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.serialisers import ProductSerialiser

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serialiser = ProductSerialiser(data=request.data)
    if request.method=="POST":
        if serialiser.is_valid():
            # instance = serialiser.save()
            print(serialiser.data)
            return Response(serialiser.data)
        return Response({'invalid' : 'not good data'}, status=400)
