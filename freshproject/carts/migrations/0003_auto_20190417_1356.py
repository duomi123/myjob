# Generated by Django 2.1.7 on 2019-04-17 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homegoods', '0002_auto_20190415_1940'),
        ('userinfo', '0005_userinfo_telephone'),
        ('carts', '0002_auto_20190417_1340'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carts',
            new_name='CartsInfo',
        ),
    ]