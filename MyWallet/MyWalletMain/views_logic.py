from .models import PreTag, WalletTag, WalletData, NotificationModel
from django.db.models import Sum
from django.contrib.auth.models import User
from datetime import datetime
import datetime


class DataSetMAinPage:
    """class for creating data set"""

    def __init__(self, tag_name=None, pre_tag_name=None, username=None, chose_month=None):
        self.tag_name = tag_name
        self.pre_tag_name = pre_tag_name
        self.username = username
        self.get_user_id = User.objects.filter(username=self.username).values('id')[0]['id']
        self.month = datetime.datetime.now().strftime("%Y-%m")
        self.chose_month = chose_month

    @property
    def data_for_chosen_month(self):
        """data set for chosen month """
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.filter(user_id=self.get_user_id).values(),
                'tag': WalletTag.objects.filter(user_id=self.get_user_id).values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.chose_month).values(),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.chose_month).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def data_set(self):
        """main_data set """
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.filter(user_id=self.get_user_id).values(),
                'tag': WalletTag.objects.filter(user_id=self.get_user_id).values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def filter_by_increasing_date(self):
        """data_set after make increase date filter"""
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    '-date'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def filter_by_increasing_price(self):
        """data_set after make increase price filter"""
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    '-price'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def data_set_for_notification_page(self):
        """funct for creating data set in notification page"""
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'model': NotificationModel.objects.values(),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def data_set_for_alarm_bells(self):
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'model': NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values(),
                'num_of_notes': num_of_notes
                }
        return data

    @property
    def filter_by_decreasing_price(self):
        """data_set after make decrease price filter"""
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.all().values(),
                'tag': WalletTag.objects.all().values(),
                'data': WalletData.objects.filter(user=self.username, date__icontains=self.month).values().order_by(
                    'price'),
                'sum': WalletData.objects.filter(user=self.username, date__icontains=self.month).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
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
        num_of_notes = len(NotificationModel.objects.filter(alarm_date__icontains=datetime.date.today()).values())
        data = {'pre_tag': PreTag.objects.filter(user_id=self.get_user_id).values(),
                'tag': WalletTag.objects.filter(user_id=self.get_user_id).values(),
                'data': WalletData.objects.filter(user=self.username).values(),
                'sum': WalletData.objects.filter(user=self.username).values(
                    'price').aggregate(Sum('price')),
                'num_of_notes': num_of_notes
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

    def __init__(self, username, date_start=None, date_finish=None, tag_name=None, date_month=None):
        self.model = WalletTag.objects.all().values()
        self.month = datetime.datetime.now().strftime("%Y-%m")
        self.date_month = date_month
        self.date_start = date_start
        self.date_finish = date_finish
        self.tag_name = tag_name
        # self.month_new = datetime.date(2024, datetime.datetime.month, 24).strftime("%Y-%m")

        self.price_data = {}
        self.username = username
        self.get_user_id = User.objects.filter(username=self.username).values('id')[0]['id']

    @property
    def current_month_statistics(self):
        """func for build total rezult for month """
        for el in self.model:
            test = WalletData.objects.filter(wallet_tag_id=el['id'], date__icontains=self.month,
                                             user=self.username).aggregate(
                Sum('price'))
            self.price_data[f"{el['tag_name']}"] = test['price__sum']
        return self.price_data

    @property
    def statistic_for_month_by_tag(self):
        """func for making requst by chosen month and tag"""

        data = {'tag_sum': WalletData.objects.filter(user=self.username,
                                                     date__icontains=f"{self.date_month[0]}-{self.date_month[1]}",
                                                     wallet_tag_id=self.tag_name).aggregate(Sum('price'))['price__sum'],
                'model': WalletData.objects.filter(user=self.username,
                                                   date__icontains=f"{self.date_month[0]}-{self.date_month[1]}",
                                                   wallet_tag_id=self.tag_name).values(),
                'tag_name': WalletTag.objects.filter(id=self.tag_name).values('tag_name')[0]['tag_name'],
                'stat_flag': 1
                }

        return data

    @property
    def statistic_for_period_of_time(self):
        import datetime
        tag_id_set = []
        clean_data_set = {}
        tag_id_model = WalletTag.objects.filter(
            user=User.objects.filter(username=self.username).values()[0]['id']).values()
        for el in (tag_id_model):
            if el['tag_name'] not in tag_id_set:
                tag_id_set.append(el)
                clean_data_set[el['tag_name']] = 0

        model_data = []
        date_start = self.date_start
        date_finish = self.date_finish
        res = date_finish - date_start
        date_pack = []
        clean_data = {}
        for el in range(1, res.days + 1):
            dt = date_start + datetime.timedelta(days=el)
            date_pack.append(dt)

        for el in date_pack:
            test = WalletData.objects.filter(user=self.username, date__icontains=el).values()
            if len(test) != 0:
                model_data.append(test)

        for item in tag_id_set:
            for elem in model_data:
                if elem[0]['wallet_tag_id'] == item['id']:
                    clean_data_set[f"{item['tag_name']}"] += int(elem[0]['price'])
        data = {'model': clean_data_set}

        return data


class MainNotes:
    """Clss for cmenaging on Notes page"""

    def __init__(self, username, text_note, note_date):
        self.username = username
        self.text_note = text_note
        self.note_date = note_date

    @property
    def create_notes(self):
        """func for creatin new notes in notes page"""
        NotificationModel.objects.create(username=self.username, note_text=self.text_note, alarm_date=self.note_date)
        pass
