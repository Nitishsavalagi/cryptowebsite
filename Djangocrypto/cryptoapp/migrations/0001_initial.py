# Generated by Django 3.2.6 on 2022-01-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('Symbol', models.CharField(max_length=250)),
                ('Current_Price', models.CharField(max_length=200)),
            ],
        ),
    ]
