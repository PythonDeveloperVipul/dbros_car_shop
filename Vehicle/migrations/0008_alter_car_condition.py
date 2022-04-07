# Generated by Django 4.0.3 on 2022-03-29 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0007_alter_car_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='condition',
            field=models.CharField(choices=[('p', 'Poor'), ('f', 'Fair'), ('g', 'Good'), ('e', 'Excellence')], default='Select', max_length=8),
        ),
    ]
