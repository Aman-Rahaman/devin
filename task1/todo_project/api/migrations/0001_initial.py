# Generated by Django 5.1.3 on 2024-11-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('task', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
