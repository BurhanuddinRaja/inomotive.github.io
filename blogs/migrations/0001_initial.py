# Generated by Django 3.1.5 on 2021-03-24 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=13)),
                ('author', models.CharField(max_length=100)),
                ('timeStamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]
