# Generated by Django 4.1.4 on 2023-05-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_resume_profile_alter_resume_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='resumedoc/'),
        ),
    ]
