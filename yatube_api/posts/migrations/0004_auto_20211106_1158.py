# Generated by Django 2.2.16 on 2021-11-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_follow'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='following',
        ),
    ]