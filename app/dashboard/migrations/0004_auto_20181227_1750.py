# Generated by Django 2.1.4 on 2018-12-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_labsresearch_upcoming'),
    ]

    operations = [
        migrations.AddField(
            model_name='interest',
            name='completion_message',
            field=models.TextField(blank=True, default='', verbose_name='Worker Completion Message'),
        ),
        migrations.AlterField(
            model_name='interest',
            name='status',
            field=models.CharField(choices=[('review', 'Needs Review'), ('warned', 'Hunter Warned'), ('okay', 'Okay'), ('snoozed', 'Snoozed'), ('pending', 'Pending'), ('SBU', 'Stopped By User'), ('SBF', 'Stopped By Funder'), ('SBS', 'Stopped By Staff'), ('BC', 'Bounty Canceled')], default='okay', help_text='The current status of the interest', max_length=7, verbose_name='Status'),
        ),
    ]
