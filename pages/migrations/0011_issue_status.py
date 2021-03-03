# Generated by Django 3.1.4 on 2021-03-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210302_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Done', 'Done')], default=1, max_length=11),
            preserve_default=False,
        ),
    ]