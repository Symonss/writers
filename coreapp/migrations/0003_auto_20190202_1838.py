# Generated by Django 2.0.10 on 2019-02-02 15:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_auto_20190201_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]