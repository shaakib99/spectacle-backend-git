from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
import json
from django.shortcuts import HttpResponse,render,redirect
import urllib
import ssl
from django.views.decorators.csrf import csrf_exempt
import string
import random
from .postData import post_data

@api_view(['GET'])
def productList(request):
    data = Product.objects.all()
    serializer = ProductSerializer(data,many=True).data
    return Response(serializer)

@api_view(['GET'])
def productDetail(request,pk):
    try:
        data = Product.objects.get(product_id = pk)
        data.colors = data.colors.split(',')
        data= ProductSerializer(data,many = False).data
        dataStatus = {'datastatus': status.HTTP_200_OK}
    except Product.DoesNotExist:
        data = {}
        dataStatus = {'datastatus': status.HTTP_404_NOT_FOUND}

    relatedData = Product.objects.filter(product_id = not pk)[0:5]

    relatedData = ProductSerializer(relatedData, many = True).data

    combineData = [dataStatus,data,relatedData]
    return Response(combineData)

@api_view(['GET'])
def productSearch(request,searchText):
        data = Product.objects.filter(title__icontains= searchText+'')
        data = ProductSerializer(data,many = True).data
        return Response(data)

@api_view(['GET'])
def productSearchWithoutParam(request):
    data = Product.objects.all()
    data = ProductSerializer(data,many = True).data
    return Response(data)

@api_view(['POST'])
def sslCommerz(request):
    total = request.data['total']
    tran_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    post_data['total_amount'] = total
    post_data['tran_id'] =  tran_id
    url = "https://sandbox.sslcommerz.com/gwprocess/v4/api.php"
    result = sendRequest(url, post_data)
    if result['status'] == 'SUCCESS':
        return HttpResponse(json.dumps(result))

@csrf_exempt
def sslcommerzResult(request):
    if request.POST:
        data = {
            'tran_id': request.POST.get('tran_id'),
            'amount' : request.POST.get('amount'),
            'card_type' : request.POST.get('card_type')
        }
        data = json.dumps(data)
        template = 'spec_api/paymentStatus.html'
        return render(request,template,{'data': data})
    else:
        return HttpResponse('NOT A VALID PAYMENT')
@csrf_exempt
def sslcommerzfail(request):
    return HttpResponse('Transaction failed - ' + request.POST.get('error'))
@csrf_exempt
def sslcommerzcancel(request):
    host = 'http://127.0.0.1:3000/'
    clientHost = host+'information'
    return redirect(clientHost)

@api_view(['GET'])
def sslcomerzTranId(request, id):
    tran_url = 'https://sandbox.sslcommerz.com/validator/api/merchantTransIDvalidationAPI.php?'
    data = {}
    data['store_id'] = post_data['store_id']
    data['store_passwd'] = post_data['store_passwd']
    data['tran_id'] = id
    tran_url += 'store_id='+data['store_id']
    tran_url += '&store_passwd='+data['store_passwd']
    tran_url += '&tran_id='+id
    data = sendRequest(tran_url,data)
    return HttpResponse(json.dumps(data))

def sendRequest(url,data):
    data = urllib.parse.urlencode(data).encode()
    data = urllib.request.urlopen(url,data,60,context=ssl._create_unverified_context()).read()
    data = json.loads(data)
    return data