# Generated by Django 5.0.6 on 2024-10-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cruds',
            old_name='name',
            new_name='category',
        ),
        migrations.AddField(
            model_name='cruds',
            name='ads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cruds',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cruds',
            name='taxes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cruds',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
