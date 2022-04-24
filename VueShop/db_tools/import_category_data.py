__author__ = 'panshidi'

import os
import sys
import django


pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(pwd + '../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'VueShop.settings')
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

for lev1_row in row_data:
    lev1_instance = GoodsCategory()
    lev1_instance.code = lev1_row['code']
    lev1_instance.name = lev1_row['name']
    lev1_instance.category_type = 1
    lev1_instance.save()
    for lev2_row in lev1_row['sub_categorys']:
        lev2_instance = GoodsCategory()
        lev2_instance.code = lev2_row['code']
        lev2_instance.name = lev2_row['name']
        lev2_instance.category_type = 2
        lev2_instance.parent_category = lev1_instance
        lev2_instance.save()
        for lev3_row in lev1_row['sub_categorys']:
            lev3_instance = GoodsCategory()
            lev3_instance.code = lev3_row['code']
            lev3_instance.name = lev3_row['name']
            lev3_instance.category_type = 3
            lev3_instance.parent_category = lev1_instance
            lev3_instance.save()
#  django的model可以独立使用
