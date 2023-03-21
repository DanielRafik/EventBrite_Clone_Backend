# Generated by Django 4.2b1 on 2023-03-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('User_id', models.IntegerField()),
                ('NAME', models.CharField(max_length=50)),
                ('DESCRIIPTION', models.CharField(max_length=500)),
                ('TYPE', models.CharField(max_length=20)),
                ('CATEGORY_ID', models.IntegerField()),
                ('SUB_CATEGORY_ID', models.IntegerField()),
                ('ST_DATE', models.DateField()),
                ('END_DATE', models.DateField()),
                ('ST_TIME', models.TimeField()),
                ('END_TIME', models.TimeField()),
                ('ONLINE', models.BooleanField()),
                ('CAPACITY', models.IntegerField()),
                ('PASSWORD', models.CharField(max_length=10)),
                ('EVENT_PHOTO', models.ImageField(upload_to='')),
                ('locationـid', models.IntegerField()),
                ('STATUS', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('NAME', models.CharField(max_length=20)),
                ('PRICE', models.FloatField()),
                ('EVENT_ID', models.IntegerField()),
                ('GUEST_ID', models.IntegerField()),
                ('TICKET_NUM', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID', models.IntegerField()),
                ('F_NAME', models.CharField(max_length=20)),
                ('L_NAME', models.CharField(max_length=20)),
                ('EMAIL', models.EmailField(max_length=254)),
                ('PASSWORD', models.CharField(max_length=20)),
                ('AGE', models.IntegerField()),
                ('BIRTH_DATE', models.DateField()),
                ('PHONE', models.CharField(max_length=20)),
                ('CITY', models.CharField(max_length=20)),
                ('COUNTRY', models.CharField(max_length=20)),
                ('ADDRESS', models.CharField(max_length=20)),
                ('LOCATION_ID', models.IntegerField()),
                ('DISCOUNT_ID', models.IntegerField()),
            ],
        ),
    ]
