# Generated by Django 4.0.3 on 2022-03-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_apis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apis',
            options={'verbose_name': '单一场景接口', 'verbose_name_plural': '单一场景接口'},
        ),
        migrations.AddField(
            model_name='apis',
            name='producter',
            field=models.CharField(max_length=200, null=True, verbose_name='产品负责人'),
        ),
    ]
