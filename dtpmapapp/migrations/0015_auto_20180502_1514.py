# Generated by Django 2.0.4 on 2018-05-02 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dtpmapapp', '0014_remove_street_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='MVCParticipantType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, default=None, help_text='MVC Type name', max_length=1000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='mvc',
            name='participant_type',
            field=models.ForeignKey(blank=True, default=None, help_text='MVC Participant Type', null=True, on_delete=django.db.models.deletion.SET_NULL, to='dtpmapapp.MVCParticipantType'),
        ),
    ]