# Generated by Django 2.1.2 on 2019-04-15 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manage_team', '0002_playerinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('game_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('max_players', models.PositiveIntegerField()),
                ('game_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeamInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50, unique=True)),
                ('team_points', models.IntegerField()),
                ('game_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_team.GameInfo')),
            ],
        ),
        migrations.DeleteModel(
            name='team_register',
        ),
        migrations.RemoveField(
            model_name='playerinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='age',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='playerinfo',
            name='alias',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='teaminfo',
            name='player_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_team.PlayerInfo'),
        ),
    ]
