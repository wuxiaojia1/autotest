# Generated by Django 4.0.3 on 2022-03-03 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apistep',
            name='apiurl',
            field=models.CharField(max_length=200, verbose_name='接口地址'),
        ),
    ]
