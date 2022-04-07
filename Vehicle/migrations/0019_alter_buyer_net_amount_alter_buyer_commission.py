# Generated by Django 4.0.3 on 2022-04-04 13:07

from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0018_rename_commision_currency_buyer_commission_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='Net_amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=10),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='commission',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='USD', max_digits=10),
        ),
    ]
