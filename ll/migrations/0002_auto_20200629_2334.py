# Generated by Django 3.0.4 on 2020-06-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='name',
            field=models.TextField(),
        ),
    ]
