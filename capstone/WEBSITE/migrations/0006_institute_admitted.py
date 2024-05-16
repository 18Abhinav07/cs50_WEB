# Generated by Django 5.0.3 on 2024-04-09 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBSITE', '0005_delete_institute_admitted'),
    ]

    operations = [
        migrations.CreateModel(
            name='INSTITUTE_ADMITTED',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('roll_no', models.IntegerField()),
                ('reason', models.CharField(max_length=100)),
                ('permission', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('vehicle_no', models.CharField(max_length=10)),
            ],
        ),
    ]
