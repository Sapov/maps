from django.shortcuts import render
from django.views.generic import ListView

from .models import InfoObjects


# Create your views here.


class InfoListView(ListView):
    paginate_by = 5
    model = InfoObjects
    template_name = 'infoview.html'


# def view_order(request):
#     '''Вывод файлов только авторизованного пользователя'''
#     Orders = Order.objects.filter(Contractor=request.user).order_by('-id')
#     logger.info(f'Orders: {Orders}')
#
#     paginator = Paginator(Orders, 2)
#     if 'page' in request.GET:
#         page_num = request.GET.get('page')
#     else:
#         page_num = 1
#     logger.info(f'page_NUM: {page_num}')
#     page_obj = paginator.get_page(page_num)
#     logger.info(f'page_NUM: {page_obj}')
#
#     return render(request, "view_orders.html", {"Orders": Orders, 'title': 'Заказы', 'page_obj': page_obj})


