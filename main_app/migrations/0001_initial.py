# Generated by Django 4.0.3 on 2022-04-02 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('date_written', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('first_aired', models.IntegerField()),
                ('last_aired', models.IntegerField()),
                ('genre', models.CharField(choices=[('act', 'Action'), ('com', 'Comedy'), ('comdram', 'Comedy/Drama'), ('crim', 'Crime/Mystery'), ('doc', 'Documentary'), ('docdram', 'Docudrama'), ('dram', 'Drama'), ('histdram', 'Historical Drama'), ('music', 'Musical'), ('news', 'News'), ('police', 'Police Procedural'), ('reality', 'Reality'), ('romcom', 'Romantic Comedy'), ('romdram', 'Romantic Drama'), ('scifi', 'Science Fiction'), ('sitcom', 'Sitcom'), ('susp', 'Suspense')], max_length=50)),
                ('stream_service', models.CharField(choices=[('acron', 'Acorn TV'), ('amaz', 'Amazon Prime TV'), ('amc', 'AMC+'), ('appl', 'Apple TV+'), ('att', 'AT&T'), ('brit', 'BritBox'), ('cbs', 'CBS'), ('dirtv', 'DirecTV'), ('dis', 'Disney+'), ('fubo', 'Fubo'), ('hbo', 'HBO Max'), ('hoop', 'Hoopla'), ('hulu', 'Hulu+'), ('kan', 'Kanopy'), ('nbc', 'NBC'), ('net', 'Netflix'), ('para', 'Paramount+'), ('show', 'Showtime'), ('star', 'Starz'), ('tou', 'YouTube'), ('tcm', 'TCM')], max_length=250)),
                ('img', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('thumbs', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reviews', models.ManyToManyField(to='main_app.review')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['thumbs'],
            },
        ),
    ]
