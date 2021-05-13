# Generated by Django 3.2.2 on 2021-05-12 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('webhook_url', models.URLField()),
                ('api_key', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RequestLogs',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('ip', models.GenericIPAddressField()),
                ('created_att', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.PositiveIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('transaction_reference', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('created_at', models.DateTimeField()),
                ('status', models.CharField(choices=[('completed', 'completed transaction'), ('pending', 'pending transaction'), ('failed', 'failed transaction')], default='failed', max_length=10)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='microservice.clients')),
            ],
        ),
    ]