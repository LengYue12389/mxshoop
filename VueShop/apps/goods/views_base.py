from django.views.generic import View
from goods.models import Goods
from django.http import HttpResponse
import json
from django.forms.models import model_to_dict


class GoodsListView(View):
    def get(self, request):
        json_list = []
        goods = Goods.objects.all()[:10]
        for good in goods:
            json_dict = dict()
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)

        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        return HttpResponse(json.dumps(json_list), content_type='application/json')
