# Generated by Django 4.1.7 on 2023-03-29 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0002_alter_availability_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='booked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='booked_slots', to='appusers.student'),
        ),
    ]
