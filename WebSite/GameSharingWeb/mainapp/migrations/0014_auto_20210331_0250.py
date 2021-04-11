# Generated by Django 3.1.7 on 2021-03-30 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mainapp', '0013_auto_20210331_0236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='game_box',
        ),
        migrations.RemoveField(
            model_name='cartgame',
            name='game',
        ),
        migrations.RemoveField(
            model_name='gamebox',
            name='bag_room',
        ),
        migrations.AddField(
            model_name='cartgame',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartgame',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='BagRoom',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
