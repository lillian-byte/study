# Generated by Django 2.1.4 on 2020-07-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gitVersionManagement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gitversion',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='备注'),
        ),
    ]
