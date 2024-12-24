from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.response import Response

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
        request.data['price'] = 25
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDiscount(APIView):

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
