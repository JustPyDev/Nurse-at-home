# Generated by Django 4.0.3 on 2022-03-23 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0004_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='map',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='services',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ambulance.tariffs'),
        ),
    ]
