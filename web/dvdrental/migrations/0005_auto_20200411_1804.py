# Generated by Django 2.2.11 on 2020-04-11 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvdrental', '0004_auto_20200411_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dvdrental.Category'),
        ),
        migrations.AlterField(
            model_name='filmcategory',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dvdrental.Film'),
        ),
    ]