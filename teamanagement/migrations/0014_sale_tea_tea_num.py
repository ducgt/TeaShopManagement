# Generated by Django 2.1.4 on 2019-01-07 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamanagement', '0013_tea_addition_goods'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale_tea',
            name='tea_num',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
