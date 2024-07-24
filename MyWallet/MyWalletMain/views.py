from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .views_logic import DataSetMAinPage, CreateTag, CreatePreTag, CreateWalletArticles
from rest_framework.views import APIView
from rest_framework import permissions


# Create your views here.
def login_page(request):
    """Login page logic"""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        data_set = DataSetMAinPage()
        login(request, user)
        return render(request, "MyWalletMain/main_page.html", data_set.data_set)

    return render(request, "MyWalletMain/login_page.html")


class MainPage(APIView):
    """Class for main page logic"""

    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        data_set = DataSetMAinPage()
        filter_by_increasing = request.GET.get('increase')
        filter_by_decreasing = request.GET.get('decrease')
        filter_by_increasing_price = request.GET.get('increase_price')
        filter_by_decreasing_price = request.GET.get('filter_by_decreasing_price')
        filter_by_tag_name = request.GET.get('filter_by_tag_name')
        filter_by_pre_tag_name = request.GET.get('filter_by_pre_tag_name')
        print(data_set.data_set['sum'])

        if filter_by_pre_tag_name:
            """filtering by pre_tag"""
            logic = DataSetMAinPage(pre_tag_name=filter_by_pre_tag_name)
            return render(request, 'MyWalletMain/main_page.html', logic.filter_by_pre_tag)

        if filter_by_tag_name:
            """filter by tag name """
            logic = DataSetMAinPage(tag_name=filter_by_tag_name)
            return render(request, 'MyWalletMain/main_page.html', logic.filter_by_tag_name)

        if filter_by_decreasing_price:
            """logic for filter by decreasing price"""
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_decreasing_price_price)

        if filter_by_increasing_price:
            """logic for filter by increasing price"""
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_increasing_price)

        if filter_by_increasing:
            """filter by increasing date"""
            return render(request, 'MyWalletMain/main_page.html', data_set.filter_by_increasing_date)

        if filter_by_decreasing:
            """filter by decreasing date"""
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

    @staticmethod
    def post(request):
        data_set = DataSetMAinPage()
        create_tag_btn = request.POST.get('create_tag_btn')
        create_pre_tag_btn = request.POST.get('create_pre_tag_btn')
        write_data = request.POST.get('write_data')

        if write_data:
            """create new articles"""
            price = request.POST.get('price')
            select_tag = request.POST.get('select_tag')
            select_pre_tag = request.POST.get('select_pre_tag')
            logic = CreateWalletArticles(price, select_tag, select_pre_tag).create_articles
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if create_tag_btn:
            """create new tag"""
            logic = CreateTag(request.POST.get('create_tag')).create_tag
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        if create_pre_tag_btn:
            """create_pre_tag"""
            logic = CreatePreTag(pre_tag=request.POST.get('create_pre_tag')).create_pre_tag
            return render(request, 'MyWalletMain/main_page.html', data_set.data_set)

        return render(request, 'MyWalletMain/main_page.html', data_set.data_set)
