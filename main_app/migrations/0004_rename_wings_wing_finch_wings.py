# Generated by Django 4.1.4 on 2023-01-03 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_wings_alter_feeding_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Wings',
            new_name='Wing',
        ),
        migrations.AddField(
            model_name='finch',
            name='wings',
            field=models.ManyToManyField(to='main_app.wing'),
        ),
    ]
