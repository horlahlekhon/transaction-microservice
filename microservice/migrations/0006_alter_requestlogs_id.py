# Generated by Django 3.2.2 on 2021-05-12 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microservice', '0005_requestlogs_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestlogs',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]