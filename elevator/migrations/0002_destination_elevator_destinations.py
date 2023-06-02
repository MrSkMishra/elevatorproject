# Generated by Django 4.2.1 on 2023-06-02 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elevator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='elevator',
            name='destinations',
            field=models.ManyToManyField(to='elevator.destination'),
        ),
    ]
