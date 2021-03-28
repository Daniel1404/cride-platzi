# Generated by Django 2.0.9 on 2021-03-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Circle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time in which the object was created', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time in which the object was modified', verbose_name='created at')),
                ('name', models.CharField(max_length=140, verbose_name='circle name')),
                ('slug', models.SlugField(max_length=40, unique=True)),
                ('description', models.CharField(max_length=255, verbose_name='circle description')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='circles/pictures')),
                ('rides_offered', models.PositiveIntegerField(default=0)),
                ('rides_taken', models.PositiveIntegerField(default=0)),
                ('verified', models.BooleanField(default=False, help_text='Verified circles are also know as official communities', verbose_name='verified circle')),
                ('is_public', models.BooleanField(default=True, help_text="If a circle isn't private it means that just the members know about it, and doesn't allow external users to join", verbose_name='public')),
                ('is_limited', models.BooleanField(default=False, help_text='Limited groups can grow up to a fixed number of members', verbose_name='limited')),
                ('members_limit', models.PositiveIntegerField(default=0, help_text='If circle is limited, this will be the limit of members')),
            ],
            options={
                'ordering': ['-rides_taken', '-rides_offered'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
