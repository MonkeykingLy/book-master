# Generated by Django 2.0.1 on 2020-03-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200301_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actioncomment',
            name='comment',
            field=models.TextField(verbose_name='活动评论'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
