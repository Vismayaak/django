# Generated by Django 5.1.1 on 2024-10-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_hotel_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='user10',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_number', models.CharField(max_length=100)),
            ],
        ),
    ]
