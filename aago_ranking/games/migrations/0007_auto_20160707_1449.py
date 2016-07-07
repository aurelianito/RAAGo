# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-07 14:49
from __future__ import unicode_literals

import aago_ranking.games.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20160630_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='events.Event'),
        ),
        migrations.AlterField(
            model_name='game',
            name='handicap',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='komi',
            field=models.DecimalField(decimal_places=1, max_digits=10, validators=[aago_ranking.games.models.validate_whole_halfs]),
        ),
        migrations.AlterField(
            model_name='game',
            name='points',
            field=models.DecimalField(decimal_places=1, max_digits=10, validators=[aago_ranking.games.models.validate_whole_halfs]),
        ),
        migrations.AlterField(
            model_name='game',
            name='result',
            field=models.CharField(choices=[('black', 'Black Wins'), ('white', 'White Wins'), ('draw', 'Draw'), ('both_lose', 'Both lose'), ('null_match', 'Null match')], max_length=16),
        ),
    ]
