# Generated by Django 4.0.3 on 2022-03-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulance', '0008_delete_footer_contact_about_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
