# Generated by Django 3.2 on 2021-04-25 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codechef_management_app', '0004_delete_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='codechef_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='prn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role_id',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
