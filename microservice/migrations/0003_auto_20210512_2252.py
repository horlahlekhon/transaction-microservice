# Generated by Django 3.2.2 on 2021-05-12 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microservice', '0002_rename_client_id_transactions_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
