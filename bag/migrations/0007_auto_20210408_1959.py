# Generated by Django 3.1.7 on 2021-04-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0006_auto_20210407_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='tips',
            field=models.CharField(max_length=20),
        ),
    ]
