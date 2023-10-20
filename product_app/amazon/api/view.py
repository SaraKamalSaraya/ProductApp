from rest_framework.response import Response
from rest_framework.decorators import api_view
from amazon.models import Products
from amazon.api.serializers import ProductSerializer

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        products = Products.get_all_products()
        serialized_products = ProductSerializer(products, many = True)
        return Response({'message': 'Products Data Receieved Successfully', 'products': serialized_products.data}, status=200)
    
    elif request.method == 'POST':
        product = ProductSerializer(data=request.data)
        if product.is_valid():
            product.save()
            return Response({'message': 'Product Added Successfully', 'product':product.data}, status=201)
        return Response(product.errors, status=400)
    

@api_view(['GET','DELETE','PUT'])
def product_resource(request,id):
    product = Products.get_sepcific_object(id=id)
    if request.method == 'GET':
        serialized_products = ProductSerializer(product)
        return Response({'message':'Product Data Receieved Successfully', 'product':serialized_products.data}, status=200)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response({'message':'Product Deleted'}, status=204)
    
    elif request.method == 'PUT':
        serialized_product = ProductSerializer(instance=product, data=request.data)
        if serialized_product.is_valid():
            serialized_product.save()
            return Response({'message': 'Product Added Successfully', 'product':serialized_product.data}, status=201)
        return Response(serialized_product.errors, status=400)

