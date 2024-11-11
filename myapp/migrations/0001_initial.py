# Generated by Django 5.1.1 on 2024-10-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usermodel',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=200)),
                ('user_age', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
