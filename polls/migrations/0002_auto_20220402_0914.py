# Generated by Django 3.2.8 on 2022-04-02 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kg',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='kg',
            name='type',
            field=models.CharField(default=None, max_length=100),
        ),
    ]