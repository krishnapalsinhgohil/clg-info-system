# Generated by Django 2.0.3 on 2018-03-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20180329_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='credits',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
