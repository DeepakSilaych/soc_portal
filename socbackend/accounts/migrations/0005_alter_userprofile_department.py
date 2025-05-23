# Generated by Django 4.2.6 on 2025-04-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='department',
            field=models.CharField(choices=[('Aerospace Engineering', 'Aerospace Engineering'), ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Earth Sciences', 'Earth Sciences'), ('Economics', 'Economics'), ('Electrical Engineering', 'Electrical Engineering'), ('Energy Science and Engineering', 'Energy Science and Engineering'), ('Engineering Physics', 'Engineering Physics'), ('Environmental Science and Engineering', 'Environmental Science and Engineering'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Industrial Design Centre', 'Industrial Design Centre'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Metallurgical Engineering and Materials Science', 'Metallurgical Engineering and Materials Science'), ('Physics', 'Physics'), ('Industrial Engineering and Operations Research', 'Industrial Engineering and Operations Research'), ('Other', 'Other')], max_length=50),
        ),
    ]
