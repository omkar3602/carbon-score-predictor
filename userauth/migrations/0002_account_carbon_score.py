# Generated by Django 3.2.7 on 2023-02-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='carbon_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
