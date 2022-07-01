# Generated by Django 4.0.4 on 2022-07-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_article_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlescope',
            old_name='scope',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='scope',
            name='articles',
        ),
        migrations.AddField(
            model_name='scope',
            name='tag',
            field=models.ManyToManyField(related_name='tag', through='articles.ArticleScope', to='articles.article'),
        ),
    ]
