# Generated by Django 3.2.3 on 2021-06-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, default='patient_profile/images/Portrait_Placeholder.png', upload_to='patient_profile/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('occupation', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('city_of_birth', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('recommended_by', models.CharField(blank=True, max_length=100)),
                ('motive_of_consultancy', models.CharField(blank=True, max_length=200)),
                ('heart_problems', models.BooleanField(default=False)),
                ('epilepsy', models.BooleanField(default=False)),
                ('high_blood_pressure', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('low_blood_pressure', models.BooleanField(default=False)),
                ('hepatitis_or_liver_disease', models.BooleanField(default=False)),
                ('circulatory_problems', models.BooleanField(default=False)),
                ('cancer', models.BooleanField(default=False)),
                ('nervous_problems', models.BooleanField(default=False)),
                ('psychiatric_treatment', models.BooleanField(default=False)),
                ('radiotherapy', models.BooleanField(default=False)),
                ('chronic_diarrhea', models.BooleanField(default=False)),
                ('artificial_heart_valves', models.BooleanField(default=False)),
                ('anesthesia_allergy', models.BooleanField(default=False)),
                ('recent_weight_loss', models.BooleanField(default=False)),
                ('medicine_allergy', models.BooleanField(default=False)),
                ('diabetes', models.BooleanField(default=False)),
                ('general_allergies', models.BooleanField(default=False)),
                ('respiratory_disease', models.BooleanField(default=False)),
                ('blood_disease', models.BooleanField(default=False)),
                ('arthritis', models.BooleanField(default=False)),
                ('hiv_aids', models.BooleanField(default=False)),
                ('drug_allergy', models.BooleanField(default=False)),
                ('which_drug_allergy', models.CharField(blank=True, max_length=200)),
                ('taking_medication', models.BooleanField(default=False)),
                ('which_medication', models.CharField(blank=True, max_length=200)),
                ('under_medical_care', models.BooleanField(default=False)),
                ('why_under_medical_care', models.CharField(blank=True, max_length=200)),
                ('might_be_pregnant', models.BooleanField(default=False)),
                ('any_other_thing', models.CharField(blank=True, max_length=200)),
                ('orthodontics_brackets', models.BooleanField(default=False)),
                ('bad_bite', models.BooleanField(default=False)),
                ('facial_pain', models.BooleanField(default=False)),
                ('face_jaw_hit', models.BooleanField(default=False)),
                ('comb_pain', models.BooleanField(default=False)),
                ('hard_close_teeth', models.BooleanField(default=False)),
                ('eye_ear_face_pain', models.BooleanField(default=False)),
                ('neck_stiffness', models.BooleanField(default=False)),
                ('teeth_grind_sleep', models.BooleanField(default=False)),
                ('wake_teeth_pain', models.BooleanField(default=False)),
                ('hand_fingers_numbness', models.BooleanField(default=False)),
                ('ear_noise', models.BooleanField(default=False)),
                ('dizziness_and_nausea', models.BooleanField(default=False)),
                ('temporomandibular_joint_pain', models.BooleanField(default=False)),
                ('mandibular_joint_click_noise', models.BooleanField(default=False)),
                ('mandibular_joint_treatment', models.BooleanField(default=False)),
                ('fibromyalgia_diagnosis', models.BooleanField(default=False)),
                ('sleep_disturbance', models.BooleanField(default=False)),
                ('wake_up_tired', models.BooleanField(default=False)),
                ('aspirin_or_other_analgesic', models.BooleanField(default=False)),
                ('nail_tongue_lips_bite', models.BooleanField(default=False)),
                ('chew_gum', models.BooleanField(default=False)),
                ('perfectionist', models.BooleanField(default=False)),
                ('nervous_anxious', models.BooleanField(default=False)),
                ('muscle_relaxer_tranquilizers_antidepressants', models.BooleanField(default=False)),
                ('open_jaw_lock', models.BooleanField(default=False)),
                ('bitting_comfortable', models.BooleanField(default=False)),
                ('open_mouth_a_lot', models.BooleanField(default=False)),
                ('recent_life_change', models.BooleanField(default=False)),
                ('nervous_tension', models.BooleanField(default=False)),
                ('headache_pains_questionnaire', models.BooleanField(default=False)),
                ('bilateral_unilateral_headache', models.BooleanField(default=False)),
                ('pulsating_headache', models.BooleanField(default=False)),
                ('migraine', models.BooleanField(default=False)),
            ],
        ),
    ]
