# Generated by Django 3.1.2 on 2020-12-21 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201221_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]
