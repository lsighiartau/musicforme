# Generated by Django 3.1.3 on 2020-11-14 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicforme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='headline',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
