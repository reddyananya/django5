# Generated by Django 4.0.1 on 2024-04-26 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_remove_joblisting_job_type_alter_joblisting_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblisting',
            name='job_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
