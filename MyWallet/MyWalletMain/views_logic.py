from .models import PreTag, WalletTag, WalletData
from django.db.models import Sum
from django.contrib.auth.models import User


class DataSetMAinPage:
    """class for creating data set"""

    def __init__(self, tag_name=None, pre_tag_name=None, username=None):
        self.tag_name = tag_name
        self.pre_tag_name = pre_tag_name
        self.username = username

    @property
    def data_set(self):
        """main_data set """
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username).values(),
                'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_increasing_date(self):
        """data_set after make increase date filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username).values().order_by('-date'),
                'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_increasing_price(self):
        """data_set after make increase price filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(self.username).values().order_by('-price'),
                'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_decreasing_price_price(self):
        """data_set after make decrease price filter"""
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.all().values(user=self.username).order_by('price'),
                'sum': WalletData.objects.filter(user=self.username).values('price').aggregate(Sum('price'))
                }
        return data

    @property
    def filter_by_tag_name(self):
        """logic for filtering by tag_name"""

        if (any([(self.tag_name != ''), (self.tag_name != None)])):
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': WalletData.objects.filter(wallet_tag_id=self.tag_name, user=self.username).values(),
                    'sum': WalletData.objects.filter(wallet_tag_id=self.tag_name,
                                                     user=self.username).values().aggregate(Sum('price'))
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
        if (any([(self.pre_tag_name != ''), (self.pre_tag_name != None)])):
            data = {'pre_tag': PreTag.objects.all().values(),
                    'tag': WalletTag.objects.all().values(),
                    'data': WalletData.objects.filter(wallet_pre_tag_id=self.pre_tag_name, user=self.username).values(),
                    'sum': WalletData.objects.filter(wallet_pre_tag_id=self.pre_tag_name,
                                                     user=self.username).values().aggregate(
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


class CreateTag:
    """class for creating tags"""

    def __init__(self, tag_name):
        self.tag_name = tag_name

    @property
    def create_tag(self):
        WalletTag.objects.create(tag_name=self.tag_name)


class CreatePreTag:
    """Create pre_tag logic class"""

    def __init__(self, pre_tag):
        self.pre_tag = pre_tag

    @property
    def create_pre_tag(self):
        PreTag.objects.create(pre_tag_name=self.pre_tag)


class CreateWalletArticles:
    """class for creating data in main_page"""

    def __init__(self, price, tag, pre_tag, username=None):
        self.price = price
        self.tag = tag
        self.pre_tag = pre_tag
        self.username = username
        self.tag_id = WalletTag.objects.filter(tag_name=self.tag).values()[0]["id"]
        self.pre_tag_id = PreTag.objects.filter(pre_tag_name=self.pre_tag).values()[0]['id']

    @property
    def create_articles(self):
        """create articles"""
        WalletData.objects.create(price=self.price, wallet_tag_id=self.tag_id, wallet_pre_tag_id=self.pre_tag_id,
                                  user=self.username)
