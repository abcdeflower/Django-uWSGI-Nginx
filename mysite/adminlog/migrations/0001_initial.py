# Generated by Django 2.0.2 on 2018-03-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=30)),
                ('pwd', models.CharField(max_length=30)),
            ],
        ),
    ]
