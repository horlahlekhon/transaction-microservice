# Generated by Django 3.2.2 on 2021-05-12 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microservice', '0004_auto_20210512_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestlogs',
            name='path',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
