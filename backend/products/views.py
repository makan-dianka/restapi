from rest_framework import (
    generics, mixins, permissions, authentication)
from . models import Product
from . serialisers import ProductSerialiser

from . permissions import IsStaffEditorPermission

from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.authentication import TokenAuthentication

from django.shortcuts import get_object_or_404
from django.http import Http404

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
        ]
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perfom_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateApiView.as_view()

# class ProductListApiView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerialiser

# product_list_view = ProductListApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

product_detail_view = ProductDetailApiView.as_view()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    # lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateApiView.as_view()

class ProductDeleteApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerialiser

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_delete_view = ProductDeleteApiView.as_view()

class ProductMixinViews(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
    ):

    queryset = Product.objects.all()
    serializer_class = ProductSerialiser
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perfom_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)

product_mixin_view = ProductMixinViews.as_view()

# based views 
@api_view(["GET", "POST"])
def product_alt_view(request, pk=None, *args, **kwargs):
    # if it is get 
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerialiser(obj, many=False).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerialiser(queryset, many=True).data
        return Response(data)
    
    # if it is Post 
    if request.method=="POST":
        serializer = ProductSerialiser(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({'invalid' : 'not good data'}, status=400)
