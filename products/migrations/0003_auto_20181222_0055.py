# Generated by Django 2.1.4 on 2018-12-21 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20181222_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.BigIntegerField(default=0),
        ),
    ]