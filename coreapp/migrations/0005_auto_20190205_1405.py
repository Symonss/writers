# Generated by Django 2.0.9 on 2019-02-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0004_auto_20190202_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='email',
            field=models.CharField(default='yourmail@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='admin',
            name='first_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='admin',
            name='last_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='admin',
            name='phone',
            field=models.IntegerField(default='0792799958'),
        ),
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(default='yourmail@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='first_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='last_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.IntegerField(default='0792799958'),
        ),
        migrations.AddField(
            model_name='subadmin',
            name='email',
            field=models.CharField(default='yourmail@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='subadmin',
            name='first_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='subadmin',
            name='last_name',
            field=models.CharField(default='Peterson', max_length=50),
        ),
        migrations.AddField(
            model_name='subadmin',
            name='phone',
            field=models.IntegerField(default='0792799958'),
        ),
    ]
