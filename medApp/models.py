# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Consultation(models.Model):
    consultation_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    arret_maladie = models.CharField(max_length=255, blank=True, null=True)
    diag_note = models.CharField(max_length=255, blank=True, null=True)
    patient_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='Patient_patient_id')  # Field name made lowercase.
    medecin_medecin = models.ForeignKey('Medecin', models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.

    class Meta:
        db_table = 'consultation'


class ExamenComplementaire(models.Model):
    exam_complementaire_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=15, blank=True, null=True)
    contenue = models.CharField(max_length=255, blank=True, null=True)
    consultation_consultation = models.ForeignKey(Consultation, models.DO_NOTHING, db_column='Consultation_consultation_id')  # Field name made lowercase.
    patient_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='Patient_patient_id')  # Field name made lowercase.
    medecin_medecin = models.ForeignKey('Medecin', models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.

    class Meta:
        db_table = 'examen_complementaire'


class Medecin(models.Model):
    medecin_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    specialite = models.CharField(max_length=100, blank=True, null=True)
    adresse = models.CharField(max_length=150, blank=True, null=True)
    tel = models.CharField(max_length=40, blank=True, null=True)
    numero_ordre = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        db_table = 'medecin'


class Medicament(models.Model):
    medicament_id = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=45)
    type_produit = models.CharField(max_length=45, blank=True, null=True)
    classe = models.CharField(max_length=45, blank=True, null=True)
    laboratoire = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'medicament'


class Ordonnance(models.Model):
    ordaonnance_id = models.AutoField(primary_key=True)
    date = models.DateField(blank=True, null=True)
    patient_patient = models.ForeignKey('Patient', models.DO_NOTHING, db_column='Patient_patient_id')  # Field name made lowercase.
    medecin_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.
    consultation_consultation = models.ForeignKey(Consultation, models.DO_NOTHING, db_column='Consultation_consultation_id')  # Field name made lowercase.

    class Meta:
        db_table = 'ordonnance'


class OrdonnanceHasMedicament(models.Model):
    ordonnance_ordaonnance = models.ForeignKey(Ordonnance, models.DO_NOTHING, db_column='Ordonnance_ordaonnance_id')  # Field name made lowercase.
    medicament_medicament = models.ForeignKey(Medicament, models.DO_NOTHING, db_column='Medicament_medicament_id')  # Field name made lowercase.
    posologie = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'ordonnance_has_medicament'
        unique_together = (('ordonnance_ordaonnance', 'medicament_medicament'),)


class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    sexe = models.CharField(max_length=6, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    tel = models.CharField(max_length=30, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'patient'


class PatientHasMedecin(models.Model):
    patient_patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='Patient_patient_id')  # Field name made lowercase.
    medecin_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.

    class Meta:
        db_table = 'patient_has_medecin'
        unique_together = (('patient_patient', 'medecin_medecin'),)


class Secretaire(models.Model):
    secretaire_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nom = models.CharField(max_length=100, blank=True, null=True)
    prenom = models.CharField(max_length=100, blank=True, null=True)
    medecin_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.

    class Meta:
        db_table = 'secretaire'


class Transfert(models.Model):
    transfert_id = models.AutoField(primary_key=True)
    diagnostique = models.CharField(max_length=255, blank=True, null=True)
    examen = models.CharField(max_length=255, blank=True, null=True)
    consultation_consultation = models.ForeignKey(Consultation, models.DO_NOTHING, db_column='Consultation_consultation_id')  # Field name made lowercase.
    patient_patient = models.ForeignKey(Patient, models.DO_NOTHING, db_column='Patient_patient_id')  # Field name made lowercase.
    medecin_medecin = models.ForeignKey(Medecin, models.DO_NOTHING, db_column='Medecin_medecin_id')  # Field name made lowercase.

    class Meta:
        db_table = 'transfert'
