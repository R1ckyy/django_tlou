# Generated by Django 4.2.1 on 2023-05-09 15:36

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import multiselectfield.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter game's full name", max_length=30, verbose_name='Game name')),
                ('isDLC', models.BooleanField(help_text='Is this game a DLC?', verbose_name='is DLC')),
                ('released', models.DateField(help_text='Release date of this game', verbose_name='released')),
                ('platforms', multiselectfield.db.fields.MultiSelectField(choices=[('PS3', 'Playstation3'), ('PS4', 'Playstation4'), ('PS5', 'Playstation5'), ('PC', 'Computer')], default=['PS3'], max_length=14, validators=[multiselectfield.validators.MaxValueMultiFieldValidator(4)], verbose_name='platform')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
                'ordering': ['released'],
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter group's name", max_length=80, verbose_name='Group name')),
                ('description', models.TextField(blank=True, help_text='Enter groups description', null=True)),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter character's first name", max_length=80, verbose_name='First name')),
                ('surname', models.CharField(blank=True, help_text="If known enter character's surname", max_length=80, null=True, verbose_name='Surname')),
                ('status', models.CharField(choices=[('Alive', 'Alive'), ('Dead', 'Dead'), ('Unknown', 'Unknown')], default='Unknown', help_text="Select character's status", max_length=7, verbose_name='Status')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown')], default='Unknown', help_text="Enter character's gender", max_length=7, verbose_name='Gender')),
                ('affiliation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.groups', verbose_name='Affiliation')),
                ('appears', models.ManyToManyField(to='characters.games', verbose_name='Appears in')),
            ],
            options={
                'verbose_name': ('Character',),
                'verbose_name_plural': 'Characters',
                'ordering': ['name'],
            },
        ),
    ]