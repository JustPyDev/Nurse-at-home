# Generated by Django 4.0.3 on 2022-03-22 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='price',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='tariff1',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='tariff2',
        ),
        migrations.CreateModel(
            name='Tariffs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(blank=True, max_length=156, unique=True)),
                ('price', models.IntegerField()),
                ('type_price', models.CharField(max_length=156)),
                ('character', models.TextField()),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance.menu')),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambulance.tariffs'),
        ),
    ]