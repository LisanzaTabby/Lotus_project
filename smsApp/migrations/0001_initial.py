# Generated by Django 5.0.7 on 2024-07-26 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100)),
                ('department', models.CharField(choices=[('Finance', 'Finance'), ('Records', 'Records'), ('Research', 'Research'), ('HR', 'HR')], max_length=100)),
                ('DateofBirth', models.DateField()),
                ('Date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('location', models.CharField(choices=[('Nairobi', 'Nairobi'), ('Kisumu', 'Kisumu'), ('Nakuru', 'Nakuru'), ('Naivasha', 'Naivasha'), ('Mombasa', 'Mombasa')])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=25)),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=100)),
                ('levelofstudy', models.CharField(choices=[('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Tertiary', 'Tertiary')])),
                ('position', models.CharField(choices=[('SingleOrphan', 'SingleOrphan'), ('DoubleOrphan', 'DoubleOrphan'), ('Disabled', 'Disabled')])),
                ('status', models.CharField(choices=[('New', 'New'), ('Contunuing', 'Contunuing'), ('Discontinued', 'Discontinued'), ('Completed', 'Completed')])),
                ('DateofBirth', models.DateField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsApp.donor')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smsApp.school')),
            ],
        ),
    ]
