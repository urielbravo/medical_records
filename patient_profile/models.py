from django.db import models
from datetime import datetime


class PatientProfile(models.Model):
    # patient basic info
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='patient_profile/images/', blank=True, default='patient_profile/images/Portrait_Placeholder.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    occupation = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    birthday = models.DateField()
    city_of_birth = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    recommended_by = models.CharField(max_length=100, blank=True)
    motive_of_consultancy = models.CharField(max_length=200, blank=True)

    # have you had any of the following?
    heart_problems = models.BooleanField(default=False) 
    epilepsy = models.BooleanField(default=False)
    high_blood_pressure = models.BooleanField(default=False) 
    headache = models.BooleanField(default=False)
    low_blood_pressure = models.BooleanField(default=False) 
    hepatitis_or_liver_disease = models.BooleanField(default=False)
    circulatory_problems = models.BooleanField(default=False) 
    cancer = models.BooleanField(default=False)
    nervous_problems = models.BooleanField(default=False) 
    psychiatric_treatment = models.BooleanField(default=False)
    radiotherapy = models.BooleanField(default=False) 
    chronic_diarrhea = models.BooleanField(default=False)
    artificial_heart_valves = models.BooleanField(default=False)
    anesthesia_allergy = models.BooleanField(default=False)
    recent_weight_loss = models.BooleanField(default=False)
    medicine_allergy = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    general_allergies = models.BooleanField(default=False)
    respiratory_disease = models.BooleanField(default=False)
    blood_disease = models.BooleanField(default=False)
    arthritis = models.BooleanField(default=False)
    hiv_aids = models.BooleanField(default=False)

    # have you had any allergic reaction to any drug?
    drug_allergy = models.BooleanField(default=False)
    which_drug_allergy = models.CharField(max_length=200, blank=True)
    taking_medication = models.BooleanField(default=False)
    which_medication = models.CharField(max_length=200, blank=True)
    under_medical_care = models.BooleanField(default=False)
    why_under_medical_care = models.CharField(max_length=200, blank=True)
    might_be_pregnant = models.BooleanField(default=False)
    any_other_thing = models.CharField(max_length=200, blank=True)
    
    # patient questionnaire
    orthodontics_brackets = models.BooleanField(default=False)
    bad_bite = models.BooleanField(default=False)
    facial_pain = models.BooleanField(default=False)
    face_jaw_hit = models.BooleanField(default=False)
    comb_pain = models.BooleanField(default=False)
    hard_close_teeth = models.BooleanField(default=False)
    eye_ear_face_pain = models.BooleanField(default=False)
    neck_stiffness = models.BooleanField(default=False)
    teeth_grind_sleep = models.BooleanField(default=False)
    wake_teeth_pain = models.BooleanField(default=False)
    hand_fingers_numbness = models.BooleanField(default=False)
    ear_noise = models.BooleanField(default=False)
    dizziness_and_nausea = models.BooleanField(default=False)
    temporomandibular_joint_pain = models.BooleanField(default=False)
    mandibular_joint_click_noise = models.BooleanField(default=False)
    mandibular_joint_treatment = models.BooleanField(default=False)
    fibromyalgia_diagnosis = models.BooleanField(default=False)
    sleep_disturbance = models.BooleanField(default=False)
    wake_up_tired = models.BooleanField(default=False)
    aspirin_or_other_analgesic = models.BooleanField(default=False)
    nail_tongue_lips_bite = models.BooleanField(default=False)
    chew_gum = models.BooleanField(default=False)
    perfectionist = models.BooleanField(default=False)
    nervous_anxious = models.BooleanField(default=False)
    muscle_relaxer_tranquilizers_antidepressants = models.BooleanField(default=False)
    open_jaw_lock = models.BooleanField(default=False) 
    bitting_comfortable = models.BooleanField(default=False)
    open_mouth_a_lot = models.BooleanField(default=False)
    recent_life_change = models.BooleanField(default=False)
    nervous_tension = models.BooleanField(default=False)
    # tipo de dolor de cabeza: unilateral o bilateral
    unilateral_headache = models.BooleanField(default=False)
    bilateral_headache = models.BooleanField(default=False)
    # como es el dolor de cabeza: pulsatil, opresivo o electrico
    pulsating_headache = models.BooleanField(default=False)
    oppressive_headache = models.BooleanField(default=False)
    electric_headache = models.BooleanField(default=False)
    ####################################################
    migraine = models.BooleanField(default=False)


    def __str__(self):
        return self.name
    
    @property
    def age(self):
        return int((datetime.now().date() - self.birthday).days / 365.25)
