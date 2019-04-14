# Generated by Django 2.2 on 2019-04-12 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100, verbose_name='Bilgi')),
                ('check_list', models.TextField(max_length=1000, verbose_name='Check List')),
                ('form_url', models.CharField(blank=True, max_length=255, null=True)),
                ('coupon_code', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='services.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(blank=True, max_length=21, null=True)),
                ('latitude', models.CharField(blank=True, max_length=21, null=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='services.Service')),
            ],
        ),
    ]
