from django.shortcuts import render
from django.contrib.auth import authenticate, login

from .models import WalletData
from .views_logic import DataSetMAinPage, CreateTag, CreatePreTag, CreateWalletArticles
from rest_framework.views import APIView
from rest_framework import permissions
from datetime import datetime, date


# Create your views here.
def login_page(request):
    """Login page logic"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        data_set = DataSetMAinPage(username=request.user)
        login(request, user)
        return render(request, "MyWalletMain/main_page.html", data_set.data_set)

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

        return render(request, 'MyWalletMain/main_page.html', data_set.data_set)
