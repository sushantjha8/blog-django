# Generated by Django 2.0.7 on 2018-07-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180710_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
