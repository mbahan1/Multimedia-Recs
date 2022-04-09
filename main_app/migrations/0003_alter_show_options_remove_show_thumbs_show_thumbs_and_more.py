# Generated by Django 4.0.3 on 2022-04-09 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_remove_show_reviews_review_show_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='show',
            options={'ordering': ['title']},
        ),
        migrations.RemoveField(
            model_name='show',
            name='thumbs',
        ),
        migrations.AddField(
            model_name='show',
            name='thumbs',
            field=models.ManyToManyField(blank=True, default=None, related_name='show_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='show',
            name='user',
        ),
        migrations.AddField(
            model_name='show',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
