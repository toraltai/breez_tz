from django.conf import settings
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.db.models import F, Sum
from .utils import allowed_file


@api_view(['POST'])
def add_deals(request):
    file_data = request.data.get('file')
    if allowed_file(str(file_data)):
        import json
        with open(f'{file_data}', 'r') as file:
            data = json.load(file)
    else:
        return Response('Need csv')
    
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
                # return Response(ProductSerializer(info).data)
                return Response({"status":"OK"})
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
                # return Response(ProductSerializer(info).data)
                return Response({"status":"OK"})
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
            # return Response(ProductSerializer(info).data)
            return Response({"status":"OK"})
    except KeyError:
        return Response({"status":"Something wrong"})


class UserItemAPI(generics.ListAPIView):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        return Customer.objects.prefetch_related('item').annotate(total=Sum('products__total')
                                                                  ).order_by('-total')[:5]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serialized_data = CustomerSerializer(queryset, many=True).data
        # cache.set('top5', serialized_data, 60*15)
        return super().list(request, *args, **kwargs)