"""VueShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from xadmin.plugins import xversion
import xadmin
from django.conf.urls import url
from django.views.static import serve
from VueShop.settings import MEDIA_ROOT
# from goods.views_base import GoodsListView
from rest_framework.documentation import include_docs_urls
from goods.views import GoodsListViewSet
from rest_framework.routers import DefaultRouter

# 创建路由器并注册我们的视图。
router = DefaultRouter()
xversion.register_models()
xadmin.autodiscover()

# goods_list = GoodsListViewSet.as_view({
#     'get': 'list',
# })

router.register(r'goods', GoodsListViewSet)
urlpatterns = [
    path(r'xadmin/', xadmin.site.urls),
    re_path(r'media/(?P<path>.*?)$', serve, {'document_root': MEDIA_ROOT}),
    #  商品列表详情页面
    url(r'^', include(router.urls)),
    path(r'docs/', include_docs_urls(title='b')),
    path('api-auth/', include('rest_framework.urls'))
]
