# Generated by Django 3.1.7 on 2021-04-15 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20210411_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='used_coupons',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
