# Generated by Django 4.1.7 on 2023-04-01 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appusers', '0004_delete_tutorsession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availability',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='appusers.tutor'),
        ),
        migrations.AlterField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', to='appusers.course'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='courses',
            field=models.ManyToManyField(related_name='tutors', to='appusers.course'),
        ),
    ]