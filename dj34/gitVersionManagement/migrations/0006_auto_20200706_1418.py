# Generated by Django 2.1.4 on 2020-07-06 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gitVersionManagement', '0005_auto_20200706_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gitversion',
            name='cate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='gitVersionManagement.GitCategory', verbose_name='分类'),
        ),
    ]
