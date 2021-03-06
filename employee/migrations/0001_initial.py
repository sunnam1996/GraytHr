# Generated by Django 2.1.7 on 2019-11-19 16:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import employee.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bankdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=40)),
                ('ifsc_code', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='nomatch', message='IFSC code should be 11 digits', regex='^.{11}$')])),
                ('bank_account_holder_name', models.CharField(max_length=32)),
                ('bank_account_number', models.CharField(max_length=20)),
                ('branch_name', models.CharField(max_length=32)),
                ('account_type', models.CharField(max_length=20)),
                ('payment_type', models.CharField(max_length=20)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Careerinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField(validators=[employee.models.past])),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be ten digits and only numbers are allowed', regex='^[0-9]{10}$')])),
                ('role', models.CharField(choices=[('dev', 'Developers'), ('lead', 'Team Lead'), ('manager', 'Project Manager'), ('hr', 'HR'), ('su', 'Super User')], default='dev', max_length=32)),
                ('reporting_lead', models.CharField(max_length=40, null=True)),
                ('password', models.CharField(max_length=40)),
                ('date_of_joining', models.DateField()),
                ('confirmation_date', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(null=True, upload_to='files')),
                ('emp_status', models.CharField(choices=[('pp', 'Probation Period'), ('cn', 'Confirmed')], default='pp', max_length=20)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A +ve'), ('A-', 'A -ve'), ('B+', 'B +ve'), ('B-', 'B -ve'), ('O+', 'O +ve'), ('O-', 'O -ve'), ('AB+', 'AB +ve'), ('AB+', 'AB -ve')], max_length=30, null=True)),
                ('marital_status', models.CharField(blank=True, choices=[('s', 'Single'), ('m', 'Married')], max_length=20, null=True)),
                ('pan_card', models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^.{10}$')])),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('designation', models.CharField(max_length=40)),
                ('company_name', models.CharField(max_length=40)),
                ('company_address', models.CharField(max_length=120)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Familydetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('relation', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A +ve'), ('A-', 'A -ve'), ('B+', 'B +ve'), ('B-', 'B -ve'), ('O+', 'O +ve'), ('O-', 'O -ve'), ('AB+', 'AB +ve'), ('AB+', 'AB -ve')], max_length=30, null=True)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female')], max_length=20)),
                ('nationality', models.CharField(max_length=30)),
                ('profession', models.CharField(max_length=40)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='PFdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_join_date', models.DateField()),
                ('pf_scheme', models.CharField(max_length=30)),
                ('uan_number', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(code='nomatch', message='UAN number should be 12 digits', regex='^.{12}$')])),
                ('pf_number', models.CharField(max_length=32)),
                ('esi_number', models.CharField(max_length=20)),
                ('family_pf_number', models.CharField(max_length=32)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Qualificationdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=60)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('institute', models.CharField(max_length=120)),
                ('grade', models.CharField(max_length=40)),
                ('qualification_area', models.CharField(max_length=40)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Resignation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_on', models.DateField()),
                ('leaving_reason', models.CharField(max_length=120)),
                ('leaving_date', models.DateField(blank=True, null=True)),
                ('final_settlement_date', models.DateField(blank=True, null=True)),
                ('date_of_relieve', models.DateField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=120, null=True)),
                ('active_flag', models.BooleanField(default=True, verbose_name='active')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='careerinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='bankdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.Employee'),
        ),
    ]
