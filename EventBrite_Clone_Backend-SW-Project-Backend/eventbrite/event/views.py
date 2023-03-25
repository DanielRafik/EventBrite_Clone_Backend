"""
This module contains several view classes for the events app.

class:EventCreateView: A viewset for creating an event instance.

class:AllEventListView: A viewset for retrieving all event instances.

class:EventSearchView: A viewset for searching event instances by title.

class:EventListtype: A viewset for retrieving event instances by type.

class:EventListCategory: A viewset for retrieving event instances by category.

class:EventListSupCategory: A viewset for retrieving event instances by sub-category.

class:EventListVenue: A viewset for retrieving event instances by venue.

class:OnlineEventsAPIView: A viewset for retrieving online event instances.

"""


from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from django.http import JsonResponse, HttpResponse
from .serializers import *
from rest_framework import generics
from user import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from datetime import date
from .models import event


class EventCreateView(generics.CreateAPIView):
    """
    A viewset for creating an event instance.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = eventSerializer
    queryset = event.objects.all()


class AllEventListView(APIView):
    """
    A viewset for retrieving all event instances.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        This view should return a list of all the events.
        """

        events = event.objects.all()
        serializer = eventSerializer(events, many=True)
        return Response(serializer.data)


class EventSearchView(generics.ListAPIView):
    """
    A viewset for searching event instances by title.
    """
    permission_classes = [IsAuthenticated]
    queryset = event.objects.all()
    serializer_class = eventSerializer

    def get_queryset(self):
        """
        This view should return a list of all the events
        for the title specified in the URL parameter.
        """
        event_name = self.kwargs['event_name']
        return event.objects.filter(Title=event_name)


class EventListtype(generics.ListAPIView):
    """
    A viewset for retrieving event instances by type.
    """
    serializer_class = eventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the events
        for the type specified in the URL parameter.
        """
        event_type = self.kwargs['event_type']
        return event.objects.filter(type=event_type)


class EventListCategory(generics.ListAPIView):
    """
    A viewset for retrieving event instances by category.
    """
    serializer_class = eventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the events
        for the category specified in the URL parameter.
        """
        event_Category = self.kwargs['event_Category']
        return event.objects.filter(Category=event_Category)


class EventListSupCategory(generics.ListAPIView):
    """
    A viewset for retrieving event instances by sub-category.
    """
    serializer_class = eventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the events
        for the sub-category specified in the URL parameter.
        """
        event_sub_Category = self.kwargs['event_sub_Category']
        return event.objects.filter(sub_Category=event_sub_Category)


class EventListVenue(generics.ListAPIView):
    """
    A viewset for retrieving event instances by venue.
    """
    serializer_class = eventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the events
        for the venue specified in the URL parameter.
        """
        event_venue = self.kwargs['event_venue']
        return event.objects.filter(venue_name=event_venue)


class OnlineEventsAPIView(APIView):
    """
    A viewset for retrieving event which the online is 'true' .
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        This view should return a list of all the online events.
        """
        events = event.objects.filter(online='t')
        serializer = eventSerializer(events, many=True)
        return Response(serializer.data)
