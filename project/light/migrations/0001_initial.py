# Generated by Django 4.2.7 on 2023-11-14 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('location', models.TextField()),
                ('state', models.BooleanField(default=False)),
                ('is_on_time', models.TimeField()),
                ('is_off_time', models.TimeField()),
            ],
        ),
    ]
