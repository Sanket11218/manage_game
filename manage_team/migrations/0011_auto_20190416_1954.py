# Generated by Django 2.1.2 on 2019-04-16 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_team', '0010_auto_20190416_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gameinfo',
            old_name='max_players',
            new_name='max_teams',
        ),
    ]
