# Generated by Django 3.2.2 on 2021-05-12 23:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('microservice', '0003_auto_20210512_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestlogs',
            name='created_att',
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='body',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='content_length',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='content_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='method',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='requestlogs',
            name='request_meta',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('completed', 'completed transaction'), ('pending', 'pending transaction'), ('failed', 'failed transaction')], default='completed', max_length=10),
        ),
    ]
