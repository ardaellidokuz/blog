# Generated by Django 3.2.4 on 2021-07-01 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resimler',
            name='ctgry',
            field=models.CharField(default='SOME STRING', max_length=50, verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='resimler',
            name='src',
            field=models.TextField(default='SOME STRING', verbose_name='Src'),
        ),
        migrations.AddField(
            model_name='yazılar',
            name='article',
            field=models.TextField(default='SOME STRING'),
        ),
        migrations.AddField(
            model_name='yazılar',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='yazılar',
            name='title',
            field=models.CharField(default='SOME STRING', max_length=50),
        ),
    ]