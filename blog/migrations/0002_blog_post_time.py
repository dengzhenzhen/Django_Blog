# Generated by Django 2.0.7 on 2019-06-26 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='TIME',
            field=models.TimeField(auto_now=True),
        ),
    ]
