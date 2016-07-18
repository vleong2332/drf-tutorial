from rest_framework import serializers
from .models import Player, MainPosition


class MainPositionSerializer(serializers.ModelSerializer):
    stat = serializers.SerializerMethodField()

    class Meta:
        model = MainPosition
        fields = ('id', 'slug', 'name', 'stat')

    def get_stat():
        stat = obj.positionstat_set.get()
        return stat.count()



class PlayerSerializer(serializers.ModelSerializer):
    position_id = serializers.PrimaryKeyRelatedField(
        queryset=MainPosition.objects.all(),
        source='position',
        write_only=True
    )
    position = MainPositionSerializer(read_only=True)

    class Meta:
        model = Player
        fields = ('id', 'name', 'number', 'position', 'position_id')

    # def create(self, validated_data):
    #     position_data = validated_data.pop('position')
    #     print 'in CREATE()'
    #     print position_data
    #     position, _ = MainPosition.objects.get_or_create(**position_data)
    #     player = Player.objects.create(
    #         position=position,
    #         **validated_data
    #     )
    #     return player