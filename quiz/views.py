import random
import logging

from django.shortcuts import render
from django.views.generic import ListView

from .models import InfoObjects

logger = logging.getLogger(__name__)


# Create your views here.


class InfoListView(ListView):
    paginate_by = 5
    model = InfoObjects
    template_name = 'infoview.html'


def quantity(request):
    if request.POST:
        logger.info(f'request.POST{request.POST}')
        nums = request.POST['question']
        logger.info(nums)
        # for i in nums:
        #     print('Осталось', nums - i, 'Вопросов')
        context = Question().run()

        return render(request, 'question.html', context)
    return render(request, 'quantity.html')


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


def question(request):
    if request.POST:
        logger.info(f'request.POST{request.POST}')
        context = Question().run()
        return render(request, 'question.html', context)
    else:
        logger.info(f'request.POST{request.POST}')
        # logger.info(request.POST['num'])
        context = Question().run()
        return render(request, 'question.html', context)


def check_answer(request):
    if request.POST:
        logger.info(f'request.POST{request.POST}')
        ans = request.POST["answer"]
        logger.info(f'NUMBER ANSWER: {ans}')
        # if ans ==
        # ans = Question().check_answer(ans)
        text_answ = InfoObjects.objects.get(id=ans)

        # ans = Question().check_answer(answer)
        context = {'ans': text_answ}
        return render(request, 'check_answer.html', context)


class Question:
    def __init__(self):
        self.random_answer_dict = {}
        self.items_random_question = None
        self.lst = None
        self.all_items = None
        self.stack = None
        self.NUMS =None

    def generate_nums_question(self):
        '''for random items'''
        self.all_items = InfoObjects.objects.all()
        self.lst = [i for i in range(1, len(self.all_items))]
        random.shuffle(self.lst)
        self.stack = self.lst[1:4]
        logger.info(f'GENERATE 4 RANDOM ITEMS {self.stack}')
        return self.stack

    def generate_items_answer(self):
        ''' Варианты ответов'''
        for i in self.stack:
            random_var_answer = InfoObjects.objects.get(id=i)
            self.random_answer_dict[random_var_answer.id] = random_var_answer.title
        logger.info(f'random_answer_dict:::{self.random_answer_dict}')
        return self.random_answer_dict

    def select_random_question(self):
        '''Select random question'''
        random_items_num = random.randint(1, len(self.lst))
        self.items_random_question = InfoObjects.objects.get(id=random_items_num)
        logger.info(f'Правильный номер ответа:{self.items_random_question.id} загадан:{self.items_random_question.title} ')
        return self.items_random_question, self.items_random_question.id

    def add_answer_to_items_question(self):
        if int(self.items_random_question.id) in self.random_answer_dict:
            return self.random_answer_dict
        else:
            self.random_answer_dict[self.items_random_question.id] = self.items_random_question.title
            return self.random_answer_dict

    def generate_context(self):
        return {'items_random_question': self.items_random_question, 'title': 'Вопрос',
                'random_answer_dict': self.random_answer_dict}

    def check_answer(self, answer):
        logger.info(f'QUEST{self.items_random_question.id}')
        return int(self.items_random_question.id) == answer

    def run(self):
        self.generate_nums_question()
        self.generate_items_answer()
        self.select_random_question()
        self.add_answer_to_items_question()
        return self.generate_context()
