# Generated by Django 4.0.1 on 2024-04-26 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0007_employerapprovalquestion_employerapprovalanswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EmployerApprovalAnswer',
        ),
        migrations.DeleteModel(
            name='EmployerApprovalQuestion',
        ),
    ]