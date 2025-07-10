from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from .models import Product 


@api_view(['POST'])
def product_create(request):
    data = request.data 
    try:
        prduct = Product.objects.create(
            name =data["name"],
            description=data["description"],
            price=data["price"],
            stock=data["stock"]
        )
        return Response({"message":"Product created","id":prduct.id},status=status.HTTP_201_CREATED)
    except KeyError:
        return Response({"error":"Invaild Data"},status=status.HTTP_400_BAD_REQUEST) 

@api_view(['GET'])
def product_list(request):      # http:127.0.0.1:8000/api/products
    products = Product.objects.all().values()
    return Response(products, status.HTTP_200_OK)


@api_view(['GET'])
def product_detail(request,pk):
    try :
        product =Product.objects.get(pk=pk)
        return Response({
            "id":product.id,
            "name":product.name,
            "description": product.description,
            "price" : str(product.price),
            "stock" :product.stock

        },status = status.HTTP_200_OK )
    except Product.DoesNotExist :
        return Response ({"error": "Product not found"},status=status.HTTP_404_NOT_FOUND)
    


@api_view(['DELETE'])
def delete_product(request,id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"massage":"Product delete successfully"},status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist:
        return Response({"error":'Product not found'},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT','PATCH'])
def update_product(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error":"Product not found"},status=status.HTTP_404_NOT_FOUND)
    data = request.data
    product.name = data.get('name',product.name)
    product.description = data.get('description',product.description)
    product.price = data.get('price',product.price)
    product.stock = data.get('stock',product.stock)
    product.save()
    

    return Response({"massage":"Product updated successfully"})