# Generated by Django 3.2.10 on 2022-01-13 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_alter_category_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finance.category', verbose_name='カテゴリ'),
        ),
    ]
