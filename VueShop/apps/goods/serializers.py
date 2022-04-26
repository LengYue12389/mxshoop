from rest_framework import serializers
from .models import Goods, GoodsCategory


# class GoodsSerializers(serializers.Serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Goods.objects.create(**validated_data)
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()

    class Meta:
        model = Goods
        # fields = ['name', 'add_time', 'click_num', 'goods_front_image', 'market_price']
        fields = '__all__'

