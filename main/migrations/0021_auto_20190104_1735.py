# Generated by Django 2.1.4 on 2019-01-04 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_answer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegraphpage',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.TelegraphAccount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telegraphpage',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Group'),
        ),
    ]
