from django.http import HttpResponse
from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import F


class FileAPI(APIView):
    def post(self, request):
        file_data = request.data.get('file')
        if file_data:
            import json
            with open(f'{file_data}', 'r') as file:
                data = json.load(file)
        
        customer = data['customer']
        item = data['item']
        total = data['total']
        quantity = data['quantity']
        date=data['date']
            
        try:
            if Customer.objects.filter(customer=customer).exists():
        # Обновить существующую запись Product, если item уже существует у пользователя
                product = Product.objects.filter(customer__customer=customer, item=item).first()
                if product:
                    Product.objects.filter(customer__customer=customer, item=item).update(
                        total=F('total') + total,
                        quantity=F('quantity') + quantity,
                    )
                    info = product
                    return Response(ProductSerializer(info).data)
                else:
                    # Если item не существует, создать новую запись Product
                    customer_obj = Customer.objects.get(customer=customer)
                    info = Product.objects.create(
                                            customer=customer_obj,
                                            item=item,
                                            total=total,
                                            quantity=quantity,
                                            date=date)
                    customer_obj.item.add(info)
                    return Response(ProductSerializer(info).data)
            else:
                # Если пользователь не существует, создать нового Customer и новую запись Product
                customer_obj = Customer.objects.create(customer=customer)
                info = Product.objects.create(
                    customer=customer_obj,
                    item=item,
                    total=total,
                    quantity=quantity,
                    date=data.get('date'),
                )
                customer_obj.item.add(info)
                return Response(ProductSerializer(info).data)
        except KeyError:
            return Response("Something wrong")
 
    
class UserItemAPI(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = UserItemSerializer

    # def get(self,request):
    #     queryset = Product.objects.all()
    #     return Response({"request":queryset})