# Generated by Django 4.2.2 on 2024-01-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_result_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='number',
            field=models.FloatField(default=0.0),
        ),
    ]