# Generated by Django 2.1.4 on 2019-03-16 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_telegramcommand_in_admp_needs_bound_participant_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegramcommand',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]