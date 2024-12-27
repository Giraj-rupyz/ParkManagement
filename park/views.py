from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import Ticket, UserTypeDiscount
from .serializers import TicketSerializer, UserTypeSerializer

# Create your views here.

user_types_list = []


class ListVisitor(APIView):

    def get(self, request):
        visitors = Ticket.objects.all()
        serializer = TicketSerializer(visitors, many=True)
        return Response(serializer.data)


class CreateTicket(APIView):

    def post(self, request):
        lst=list(UserTypeDiscount.objects.all())
        discount_map={UserType.user_type: UserType.discount for UserType in lst}
        base_price=500
        if request.data['user_type'] in discount_map.keys():
            request.data['price']=base_price-((discount_map[request.data['user_type']]/100)*base_price)

        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDiscount(APIView):
    permission_classes=[permissions.IsAuthenticated]

    def post(self, request):
        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewOffers(APIView):

    def get(self, request):
        offers = UserTypeDiscount.objects.all()
        serializer = UserTypeSerializer(offers, many=True)
        return Response(serializer.data)
