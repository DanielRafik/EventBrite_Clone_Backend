# Generated by Django 4.2b1 on 2023-04-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0024_remove_event_locationـid'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_image',
            field=models.ImageField(default='image', upload_to=''),
            preserve_default=False,
        ),
    ]
