# Generated by Django 3.1.6 on 2021-02-13 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('position', models.CharField(choices=[('fron', 'Front-end developer'), ('back', 'Back-end developer'), ('data', 'Data scientist'), ('project', 'Project manager')], max_length=7)),
                ('email', models.EmailField(max_length=254)),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=250)),
                ('issue_type', models.CharField(choices=[('Bug', 'Bug'), ('Data', 'Database'), ('Front', 'Front-end')], max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=650)),
                ('deadline', models.DateField()),
                ('priority', models.CharField(choices=[('Urgent', 'Urgent'), ('ASAP', 'ASAP'), ('Normal', 'Normal')], max_length=6)),
                ('added_date', models.DateField(auto_now=True)),
                ('devs', models.ManyToManyField(to='pages.Employee')),
                ('issues', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.issue')),
            ],
        ),
    ]
