# Generated by Django 4.1.4 on 2022-12-13 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseNTALevels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course', verbose_name='Module')),
                ('nta_level', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.ntalevel', verbose_name='Module')),
            ],
        ),
    ]
