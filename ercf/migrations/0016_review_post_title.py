# Generated by Django 4.0.4 on 2022-05-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0015_review_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='post_title',
            field=models.TextField(default='post title'),
            preserve_default=False,
        ),
    ]
