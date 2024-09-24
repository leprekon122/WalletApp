from .models import PreTag, WalletTag, WalletData
from django.db.models import Sum
from django.contrib.auth.models import User
from datetime import datetime


class DataSetMAinPage:
    """class for creating data set"""

    def __init__(self, tag_name=None, pre_tag_name=None, username=None):
        self.tag_name = tag_name
        self.pre_tag_name = pre_tag_name
        self.username = username
        self.get_user_id = User.objects.filter(username=self.username).values('id')[0]['id']
        self.month = datetime.now().strftime("%Y-%m")

    @property
    def data_set(self):
        """main_data set """
        data = {'pre_tag': PreTag.objects.filter(user_id=self.get_user_id).values(),
                'tag': WalletTag.objects.filter(user_id=self.get_user_id).values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_increasing_date(self):
        """data_set after make increase date filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    '-date'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_increasing_price(self):
        """data_set after make increase price filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    '-price'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_decreasing_price(self):
        """data_set after make decrease price filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    'price'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_tag_name(self):
        """logic for filtering by tag_name"""

        if (any([(self.tag_name != ''), (self.tag_name is not None)])):
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': WalletData.objects.filter(wallet_tag_id=self.tag_name, user=self.username,
                                                      date__icontains=self.month).values(),
                    'sum': WalletData.objects.filter(wallet_tag_id=self.tag_name,
                                                     user=self.username, date__icontains=self.month).values().aggregate(
                        Sum('price'))
                    }
            return data
        else:
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': 'No_such_data',
                    'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                    }
            return data

    @property
    def filter_by_pre_tag(self):
        """filter_by pre_tag"""
        if any([(self.pre_tag_name != ''), (self.pre_tag_name is not None)]):
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': WalletData.objects.filter(wallet_pre_tag_id=self.pre_tag_name, user=self.username,
                                                      date__icontains=self.month).values(),
                    'sum': WalletData.objects.filter(wallet_pre_tag_id=self.pre_tag_name,
                                                     user=self.username, date__icontains=self.month).values().aggregate(
                        Sum('price'))
                    }
            return data
        else:
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': 'No_such_data',
                    'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                    }
            return data

    @property
    def show_all_data(self):
        """filter for view all data"""
        data = {'pre_tag': PreTag.objects.filter(user_id=self.get_user_id).values(),
                'tag': WalletTag.objects.filter(user_id=self.get_user_id).values(),
                'data': WalletData.objects.filter(user=self.username).values(),
                'sum': WalletData.objects.filter(user=self.username).values(
                    'price').aggregate(Sum('price'))
                }
        return data


class CreateTag:
    """class for creating tags"""

    def __init__(self, tag_name, username):
        self.tag_name = tag_name
        self.username = username

    @property
    def create_tag(self):
        WalletTag.objects.create(tag_name=self.tag_name, user=self.username)
        return True


class CreatePreTag:
    """Create pre_tag logic class"""

    def __init__(self, pre_tag, username=None):
        self.pre_tag = pre_tag
        self.username = username

    @property
    def create_pre_tag(self):
        PreTag.objects.create(pre_tag_name=self.pre_tag, user=self.username)


class CreateWalletArticles:
    """class for creating data in main_page"""

    def __init__(self, price, tag, pre_tag, chose_date, username=None):
        self.price = price
        self.tag = tag
        self.pre_tag = pre_tag
        self.username = username
        self.chose_date = chose_date
        self.tag_id = WalletTag.objects.filter(tag_name=self.tag).values()[0]["id"]
        self.pre_tag_id = PreTag.objects.filter(pre_tag_name=self.pre_tag).values()[0]['id']

    @property
    def create_articles(self):
        """create articles"""
        WalletData.objects.create(price=self.price, wallet_tag_id=self.tag_id, wallet_pre_tag_id=self.pre_tag_id,
                                  user=self.username, date=self.chose_date)


class RewriteData:
    """class for rewriting data in WalletData model"""

    def __init__(self, article_id, rew_price=None, rew_tag=None):
        self.article_id = article_id
        self.rew_price = rew_price
        self.rew_tag = rew_tag

    @property
    def rewrite_price(self):
        """rewrite price in WalletData"""
        if self.rew_price != '':
            model = WalletData.objects.get(id=self.article_id)
            model.price = self.rew_price
            model.save()

    @property
    def rewrite_tag(self):
        """rewrite tag in WalletData"""
        if self.rew_tag != '':
            model = WalletData.objects.get(id=self.article_id)
            model.wallet_tag_id = self.rew_tag
            model.save()


class DeleteArticles:
    """class for delete logic in WalletData model"""

    def __init__(self, art_id):
        self.art_id = art_id

    def delete_article(self):
        """func for delete article"""
        WalletData.objects.filter(id=self.art_id).delete()


class StatisticsLogic:
    """class for statistics page logic"""

    def __init__(self, username):
        self.model = WalletTag.objects.all().values()
        self.month = datetime.now().strftime("%Y-%m")
        # self.month_new = datetime.date(2024, datetime.datetime.month, 24).strftime("%Y-%m")

        self.price_data = {}
        self.username = username
        self.get_user_id = User.objects.filter(username=self.username).values('id')[0]['id']

    @property
    def current_month_statistics(self):
        """funmc for build total rezult for month """
        for el in self.model:
            test = WalletData.objects.filter(wallet_tag_id=el['id'], date__icontains=self.month,
                                             user=self.username).aggregate(
                Sum('price'))
            self.price_data[f"{el['tag_name']}"] = test['price__sum']
        return self.price_data
