# Generated by Django 3.1.7 on 2021-04-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0009_auto_20210412_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
