# Generated by Django 4.0.4 on 2022-06-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0039_alter_album_des'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='appearsOn',
            field=models.TextField(default='?'),
            preserve_default=False,
        ),
    ]
