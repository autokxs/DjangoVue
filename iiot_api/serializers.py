from rest_framework import serializers
from .models import Device,SteamPool,PoolInfo

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamPool
        fields = '__all__'

class PoolInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolInfo
        fields = '__all__'
    def get_steampool(self, obj):
        # obj是我们序列化的每个Book对象
        steampool_obj = obj.steampool   # 正向查询
        return {'id': steampool_obj.id,'status':steampool_obj.status}
