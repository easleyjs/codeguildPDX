# Generated by Django 2.2.1 on 2019-05-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='checked_out_by',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
