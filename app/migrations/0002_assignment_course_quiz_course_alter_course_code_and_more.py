# Generated by Django 5.0.6 on 2025-02-19 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(default='301', on_delete=django.db.models.deletion.CASCADE, to='app.course'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(default=301, on_delete=django.db.models.deletion.CASCADE, to='app.course'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='app.programme'),
        ),
    ]
