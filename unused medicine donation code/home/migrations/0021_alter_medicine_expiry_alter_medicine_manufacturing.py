# Generated by Django 4.2.6 on 2024-01-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_medicine_expiry_alter_medicine_manufacturing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expiry',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='manufacturing',
            field=models.DateField(blank=True, null=True),
        ),
    ]