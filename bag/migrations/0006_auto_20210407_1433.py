# Generated by Django 3.1.7 on 2021-04-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0005_remove_tips_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tips',
            name='tips',
            field=models.IntegerField(default=0),
        ),
    ]
