# Generated by Django 4.0.4 on 2022-05-27 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ercf', '0005_review_approved_alter_review_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='commenter',
            field=models.CharField(default='User', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]
