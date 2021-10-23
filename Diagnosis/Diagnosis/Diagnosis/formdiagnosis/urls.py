from django.contrib import admin
from django.urls import path
from .views import HomePage, ColdsDiagnosisPage , AllergyDiagnosisPage ,MusclePage, FlatulencePage ,DiarrheaPage, ConstipationPage, AllergiccontactPage, UrticariaPage, AllergicweatherPage, ColdallergyPage ,AccidentPage, ParasitePage, CoughPage
urlpatterns = [
    path("", HomePage, name='home-page'),
    path("colddiagnosis/<int:count>/<int:value>/", ColdsDiagnosisPage, name="colddig-page"),
    path("allergydianosis/<int:count>/<int:value>/", AllergyDiagnosisPage, name="allergy-page"),
    path("musclediagnosis/<int:count>/<int:value>/", MusclePage, name="muscle-page"),
    path("flatulencediagnosis/<int:count>/<int:value>/", FlatulencePage, name="flatulence-page"),
    path("diarrheadiagnosis/<int:count>/<int:value>/", DiarrheaPage, name="diarrhea-page"),
    path("constipationdiagnosis/<int:count>/<int:value>/", ConstipationPage, name="constipation-page"),
    path("allergiccontactdiagnosis/<int:count>/<int:value>/", AllergiccontactPage, name="allergiccontact-page"),
    path("urticariadiagnosis/<int:count>/<int:value>/", UrticariaPage, name="urticaria-page"),
    path("allergicweatherdiagnosis/<int:count>/<int:value>/", AllergicweatherPage, name="allergicweather-page"),
    path("coldallergydiagnosis/<int:count>/<int:value>/", ColdallergyPage, name="coldallergy-page"),
    path("accidentdiagnosis/<int:count>/<int:value>/", AccidentPage, name="accident-page"),
    path("parasitediagnosis/<int:count>/<int:value>/", ParasitePage, name="parasite-page"),
    path("coughdiagnosis/<int:count>/<int:value>/", CoughPage, name="cough-page"),
]