# Generated by Django 5.0.1 on 2024-02-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_account_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='accttyp',
            new_name='accttype',
        ),
        migrations.AlterField(
            model_name='account',
            name='acctnum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_status',
            field=models.CharField(default='pending', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(default='pending', max_length=30),
        ),
    ]
