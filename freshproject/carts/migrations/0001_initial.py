# Generated by Django 2.1.7 on 2019-04-17 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userinfo', '0005_userinfo_telephone'),
        ('homegoods', '0002_auto_20190415_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counts', models.IntegerField()),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homegoods.GoodsInfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='userinfo.Userinfo')),
            ],
        ),
    ]