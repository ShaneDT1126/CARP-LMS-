# Generated by Django 5.0.6 on 2024-07-23 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_videolessoncontent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='course_id',
            new_name='class_id',
        ),
    ]