# Generated by Django 4.2.3 on 2023-08-06 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventorganizer',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
