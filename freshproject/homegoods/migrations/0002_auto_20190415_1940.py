# Generated by Django 2.1.7 on 2019-04-15 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homegoods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsinfo',
            name='gpic',
            field=models.ImageField(upload_to='userinfo/images/goods'),
        ),
    ]
