# Generated by Django 4.2.14 on 2024-07-19 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PreTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_tag_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'PreTag',
                'verbose_name_plural': 'PreTag',
            },
        ),
        migrations.CreateModel(
            name='WalletTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'WalletTag',
                'verbose_name_plural': 'WalletTag',
            },
        ),
        migrations.CreateModel(
            name='WalletData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('date', models.DateField(auto_now=True)),
                ('wallet_pre_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWalletMain.pretag')),
                ('wallet_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyWalletMain.wallettag')),
            ],
            options={
                'verbose_name': 'WalletData',
                'verbose_name_plural': 'WalletData',
            },
        ),
    ]
