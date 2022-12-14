# Generated by Django 4.1.1 on 2022-09-27 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='college',
            field=models.CharField(choices=[('COLLEGE OF EDUCATION', 'COLLEGE OF EDUCATION'), ('COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION', 'COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION'), ('COLLEGE OF HEALTH AND ALLIED SCIENCES', 'COLLEGE OF HEALTH AND ALLIED SCIENCES'), ('COLLEGE OF HUMANITIES AND SOCIAL SCIENCES', 'COLLEGE OF HUMANITIES AND SOCIAL SCIENCES'), ('COLLEGE OF EARTH SCIENCES', 'COLLEGE OF EARTH SCIENCES')], default='COLLEGE OF INFORMATICS AND VIRTUAL EDUCATION', max_length=255),
        ),
        migrations.AlterField(
            model_name='program',
            name='competences',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='knowledge',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='program',
            name='special_requirements',
            field=models.TextField(blank=True, null=True),
        ),
    ]
