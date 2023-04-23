##################################################################################
###############    FOREIGN CLASS IMPORTATIONS   #################################
################################################################################
from rest_framework import serializers
from data_API_App.models import Data_base, ShopSerializerls
##################################################################################
###############    VIEW FUNCTIONALITY   ########################################
################################################################################

class DataSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    second_name = serializers.CharField()
    def create(self, data):
        return Data_base.objects.create(**data)
    def update(self,instance, data):
        instance.name = data.get('name', instance.name)
        instance.second_name = data.get('second_name', instance.second_name)
        instance.save()
        return instance
class ShopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    snack = serializers.CharField()
    drink = serializers.CharField()
    def create(self, data):
        return Shop.objects.create(**data)
    def update(self,instance, data):
        instance.name = data.get('name', instance.name)
        instance.second_name = data.get('second_name', instance.second_name)
        instance.save()
        return instance

    