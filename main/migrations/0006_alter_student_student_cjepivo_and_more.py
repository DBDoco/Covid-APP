# Generated by Django 4.0.2 on 2022-02-23 19:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_student_student_adresa_zaposlenik_zaposlenik_adresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_cjepivo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.cjepivo'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_fakultet',
        ),
        migrations.AddField(
            model_name='student',
            name='student_fakultet',
            field=models.ManyToManyField(to='main.Fakultet'),
        ),
        migrations.AlterField(
            model_name='zaposlenik',
            name='zaposlenik_cjepivo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.cjepivo'),
        ),
        migrations.RemoveField(
            model_name='zaposlenik',
            name='zaposlenik_fakultet',
        ),
        migrations.AddField(
            model_name='zaposlenik',
            name='zaposlenik_fakultet',
            field=models.ManyToManyField(to='main.Fakultet'),
        ),
    ]
