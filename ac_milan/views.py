from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Player, MainPosition
from .serializers import PlayerSerializer, MainPositionSerializer

class PlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()
        main_position_id = self.kwargs.get('position_pk', None)
        player_id = self.kwargs.get('pk', None)

        if main_position_id:
            queryset = queryset.filter(position=main_position_id)

        if player_id:
            queryset = queryset.filter(id=player_id)

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        position_id = self.kwargs.get('position_pk', None)
        position = Position.objects.get(id=position_id)
        position_stat, created = MainPositionStat.objects.get_or_create(position=position)
        position_stat.count += 1
        position_stat.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



class MainPositionView(viewsets.ModelViewSet):
    queryset = MainPosition.objects.all()
    serializer_class = MainPositionSerializer

    def get_queryset(self):
        queryset = MainPosition.objects.all()
        main_position_id = self.kwargs.get('position_pk', None)
        if main_position_id:
            queryset = queryset.filter(id=main_position_id)
        return queryset