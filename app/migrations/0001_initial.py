# Generated by Django 2.1.4 on 2018-12-31 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='add_classes',
            fields=[
                ('id', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='add_contact',
            fields=[
                ('address', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='add_daily_timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_starting_time', models.TimeField()),
                ('class_ending_time', models.TimeField()),
                ('total_duration', models.IntegerField()),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.add_classes')),
            ],
        ),
        migrations.CreateModel(
            name='campuses',
            fields=[
                ('campus_id', models.IntegerField(primary_key=True, serialize=False)),
                ('campusname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('city_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='faculity_registration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=50)),
                ('exp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fee_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.IntegerField()),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.add_classes')),
            ],
        ),
        migrations.CreateModel(
            name='feedBackDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='front_office_module',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('joining_date', models.DateField()),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='installment_name',
            fields=[
                ('installment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('installment_Name', models.CharField(max_length=50)),
                ('coursename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.add_classes')),
            ],
        ),
        migrations.CreateModel(
            name='installment_payment',
            fields=[
                ('installment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('installment_amount', models.IntegerField()),
                ('installment_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.installment_name')),
            ],
        ),
        migrations.CreateModel(
            name='payment_details',
            fields=[
                ('DateandTIme', models.CharField(max_length=30)),
                ('coursename', models.CharField(max_length=50)),
                ('Installment_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('holdername', models.CharField(max_length=50)),
                ('card_number', models.IntegerField()),
                ('card_cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student_leave',
            fields=[
                ('r_number', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('cities', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_Registration',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField(default=10)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=20)),
                ('material_status', models.CharField(max_length=15)),
                ('course', models.CharField(max_length=15)),
                ('fee_of_course', models.IntegerField()),
                ('username', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=12)),
                ('r_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='transfer_request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('campus', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='campuses',
            name='cityname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.city'),
        ),
        migrations.AddField(
            model_name='add_daily_timetable',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.faculity_registration'),
        ),
    ]
