# Generated by Django 3.2.8 on 2021-10-26 20:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ex02', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]