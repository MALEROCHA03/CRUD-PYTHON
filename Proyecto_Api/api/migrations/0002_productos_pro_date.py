# Generated by Django 3.2.8 on 2021-10-11 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='pro_date',
            field=models.DateTimeField(null=True),
        ),
    ]
