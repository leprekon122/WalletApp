import datetime
# from datetime import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import WalletData, WalletTag
from .views_logic import DataSetMAinPage, CreateTag, CreatePreTag, CreateWalletArticles, RewriteData, StatisticsLogic, \
    DeleteArticles
from rest_framework.views import APIView
from rest_framework import permissions
from django.db.models import Sum
from django.db.models import Q


# Create your views here.
def login_page(request):
    """Login page logic"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # data_set = DataSetMAinPage(username=request.user)
        login(request, user)
        # return render(request, "MyWalletMain/main_page.html", data_set.data_set)
        return redirect('main_page')

    return render(request, "MyWalletMain/login_page.html")


class MainPage(APIView):
    """Class for main page logic"""

    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        username = request.user
        data_set = DataSetMAinPage(username=username)
        filter_by_increasing = request.GET.get('increase')
        filter_by_decreasing = request.GET.get('decrease')
        filter_by_increasing_price = request.GET.get('increase_price')
        filter_by_decreasing_price = request.GET.get('filter_by_decreasing_price')
        filter_by_tag_name = request.GET.get('filter_by_tag_name')
        filter_by_pre_tag_name = request.GET.get('filter_by_pre_tag_name')
        show_all = request.GET.get('show_all')

        if show_all:
            logic = DataSetMAinPage(username=username)
            return render(request, 'MyWalletMain/main_page.html', logic.show_all_data)

        if filter_by_pre_tag_name:
            logic = DataSetMAinPage(pre_tag_name=filter_by_pre_tag_name, username=username)
            return render(request, 'MyWalletMain/main_page.html', logic.filter_by_pre_tag)

        if filter_by_tag_name:
            logic = DataSetMAinPage(tag_name=filter_by_tag_name, username=username)
            return render(request, 'MyWalletMain/main_page.html', logic.filter_by_tag_name)

        if filter_by_decreasing_price:
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_decreasing_price)

        if filter_by_increasing_price:
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_increasing_price)

        if filter_by_increasing:
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_increasing_date)

        if filter_by_decreasing:
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

    @staticmethod
    def post(request):
        data_set = DataSetMAinPage(username=request.user)
        username = request.user
        create_tag_btn = request.POST.get('create_tag_btn')
        create_pre_tag_btn = request.POST.get('create_pre_tag_btn')
        write_data = request.POST.get('write_data')
        rewrite_price_btn = request.POST.get('rewrite_price_btn')
        rewrite_tag_btn = request.POST.get('rewrite_tag_btn')
        delete_article = request.POST.get('delete_article')

        if rewrite_tag_btn:
            tag_id = request.POST.get('rewrite_tag_select')
            art_id = rewrite_tag_btn
            logic = RewriteData(article_id=art_id, rew_tag=tag_id).rewrite_tag
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if rewrite_price_btn:
            price = request.POST.get('rewrite_price')
            logic = RewriteData(rewrite_price_btn, price).rewrite_price
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if write_data:
            price = request.POST.get('price')
            chose_date = request.POST.get('chose_date')
            select_tag = request.POST.get('select_tag')
            select_pre_tag = request.POST.get('select_pre_tag')
            logic = CreateWalletArticles(price, select_tag, select_pre_tag, chose_date=chose_date,
                                         username=request.user).create_articles
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if create_tag_btn:
            logic = CreateTag(request.POST.get('create_tag'), username=username).create_tag
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if create_pre_tag_btn:
            logic = CreatePreTag(pre_tag=request.POST.get('create_pre_tag'), username=username).create_pre_tag
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if delete_article:
            logic = DeleteArticles(art_id=delete_article).delete_article()
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        return render(request, 'MyWalletMain/main_page.html', data_set.data_set)


class StatisticsPage(APIView):
    """Logic for statistics page"""
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        build_order = request.GET.get('build_order')
        username = request.user
        logic = StatisticsLogic(username=username).current_month_statistics

        if build_order:

            tag_id_set = []
            clean_data_set = {}
            tag_id_model = WalletTag.objects.filter(
                user=User.objects.filter(username=username).values()[0]['id']).values()
            for el in (tag_id_model):
                if el['tag_name'] not in tag_id_set:
                    tag_id_set.append(el)
                    clean_data_set[el['tag_name']] = 0

            model_data = []
            date_start = datetime.date(int(request.GET.get('date_start').split('-')[0]),
                                       int(request.GET.get('date_start').split('-')[1]),
                                       int(request.GET.get('date_start').split('-')[2]))
            date_finish = datetime.date(int(request.GET.get('date_finish').split('-')[0]),
                                        int(request.GET.get('date_finish').split('-')[1]),
                                        int(request.GET.get('date_finish').split('-')[2]))

            logic = StatisticsLogic(username=username, date_start=date_start, date_finish=date_finish)

            return render(request, "MyWalletMain/statistics_page.html", logic.statistic_for_period_of_time)

        data = {'model': logic}
        return render(request, "MyWalletMain/statistics_page.html", data)
