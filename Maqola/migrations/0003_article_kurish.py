# Generated by Django 3.2.2 on 2021-06-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maqola', '0002_article_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='kurish',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
