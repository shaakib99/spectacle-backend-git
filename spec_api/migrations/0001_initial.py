# Generated by Django 3.1.4 on 2020-12-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(db_index=True, max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('colors', models.CharField(choices=[('black', 'black'), ('blue', 'blue')], max_length=10)),
                ('image', models.CharField(max_length=256)),
            ],
        ),
    ]
