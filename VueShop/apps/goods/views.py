from django.shortcuts import render
from rest_framework import status
from rest_framework.viewsets import ViewSetMixin

from .serializers import GoodsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Goods
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets


# class GoodsListView(APIView):
#     """
#     列出所有的snippets或者创建一个新的snippet。
#     """
#     def get(self, request, format=None):
#         goods = Goods.objects.all()
#         goods_serializer = GoodsSerializers(goods, many=True)
#         return Response(goods_serializer.data)
#
#     # def post(self, request, format=None):
#     #     serializer = GoodsSerializers(data=request)
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoodsResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    max_page_size = 1000


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    pagination_class = GoodsResultsSetPagination
