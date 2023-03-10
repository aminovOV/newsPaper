# Generated by Django 4.1.7 on 2023-03-06 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postcategory',
            options={'verbose_name': 'Категория публикации', 'verbose_name_plural': 'Категории публикации'},
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('N', 'Новость'), ('A', 'Статья')], max_length=1, verbose_name='Тип новости'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='postcategory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post', verbose_name='Публикация'),
        ),
    ]
