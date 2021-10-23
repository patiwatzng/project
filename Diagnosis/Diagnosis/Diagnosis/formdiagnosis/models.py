from django.db import models

class ColdSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class AllergySymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class MuscleSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class FlatulenceSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class DiarrheaSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class ConstipationSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class AllergiccontactSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class UrticariaSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class AllergicweatherSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class ColdallergySymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class AccidentSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class ParasiteSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

class CoughSymptom(models.Model):
    Sequence = models.IntegerField(blank=True, null=True)
    Symptom = models.CharField(max_length=500, blank=True)
    QuestionName = models.CharField(max_length=500, blank=True)

