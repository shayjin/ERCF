# Generated by Django 4.0.4 on 2022-05-27 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ercf', '0009_alter_review_commenter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
    ]