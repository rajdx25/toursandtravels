# Generated by Django 4.0.4 on 2022-04-22 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_feedback_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='thumbnail',
            field=models.ImageField(default='None', upload_to='uploads/'),
        ),
    ]
