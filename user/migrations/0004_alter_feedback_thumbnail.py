# Generated by Django 4.0.4 on 2022-04-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_feedback_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
