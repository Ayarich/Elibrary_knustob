# Generated by Django 3.2.12 on 2022-08-19 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src_library', '0003_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'ordering': ['-added']},
        ),
        migrations.AlterModelTable(
            name='video',
            table=None,
        ),
    ]
