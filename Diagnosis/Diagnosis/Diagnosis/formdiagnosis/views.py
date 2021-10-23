from typing import Sequence
from django.db.models import query
from django.shortcuts import render, redirect
from .models import ColdSymptom, AllergySymptom, MuscleSymptom, FlatulenceSymptom, DiarrheaSymptom, ConstipationSymptom, AllergiccontactSymptom, UrticariaSymptom, AllergicweatherSymptom, ColdallergySymptom, AccidentSymptom,ParasiteSymptom, CoughSymptom

def HomePage(request):
    request.session["total"] = 0
    return render(request, 'formdiagnosis/homepage.html')

def ColdsDiagnosisPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 9:
        bypass = ColdSymptom.objects.get(Sequence=8)
        request.session[bypass.QuestionName] = value
        query_question = ColdSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName]) 
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/8)*100
        return render(request, 'formdiagnosis/diagnosis_ans.html', context={"percent":percentage})
    question = ColdSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = ColdSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName]) 
    return render(request, "formdiagnosis/colddiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def ColdsDiagnosisDisplay(request):
    return render(request, "formdiagnosis/diagnosis_ans.html")

def AllergyDiagnosisPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 10:
        bypass = AllergySymptom.objects.get(Sequence=9)
        request.session[bypass.QuestionName] = value
        query_question = AllergySymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName]) 
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/9)*100
        return render(request, 'formdiagnosis/diagnosis_ans_allergy.html', context={"percent":percentage})
    question = AllergySymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = AllergySymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName]) 
    return render(request, "formdiagnosis/allergydiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )


def MusclePage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 4:
        bypass = MuscleSymptom.objects.get(Sequence=3)
        request.session[bypass.QuestionName] = value
        query_question = MuscleSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/3)*100
        return render(request, 'formdiagnosis/muscle_ans.html', context={"percent":percentage})
    question = MuscleSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = MuscleSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/musclediagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def FlatulencePage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 7:
        bypass = FlatulenceSymptom.objects.get(Sequence=6)
        request.session[bypass.QuestionName] = value
        query_question = FlatulenceSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/6)*100
        return render(request, 'formdiagnosis/flatulence_ans.html', context={"percent":percentage})
    question = FlatulenceSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = FlatulenceSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/flatulencediagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def DiarrheaPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 8:
        bypass = DiarrheaSymptom.objects.get(Sequence=7)
        request.session[bypass.QuestionName] = value
        query_question = DiarrheaSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/7)*100
        return render(request, 'formdiagnosis/diarrhea_ans.html', context={"percent":percentage})
    question = DiarrheaSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = DiarrheaSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/diarrheadiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def ConstipationPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 4:
        bypass = ConstipationSymptom.objects.get(Sequence=3)
        request.session[bypass.QuestionName] = value
        query_question = ConstipationSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/3)*100
        return render(request, 'formdiagnosis/constipation_ans.html', context={"percent":percentage})
    question = ConstipationSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = ConstipationSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/constipationdiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def AllergiccontactPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 7:
        bypass = AllergiccontactSymptom.objects.get(Sequence=6)
        request.session[bypass.QuestionName] = value
        query_question = AllergiccontactSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/6)*100
        return render(request, 'formdiagnosis/allergiccontact_ans.html', context={"percent":percentage})
    question = AllergiccontactSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = AllergiccontactSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/allergiccontactdiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def UrticariaPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 5:
        bypass = UrticariaSymptom.objects.get(Sequence=4)
        request.session[bypass.QuestionName] = value
        query_question = UrticariaSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/4)*100
        return render(request, 'formdiagnosis/urticaria_ans.html', context={"percent":percentage})
    question = UrticariaSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = UrticariaSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/urticariadiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def AllergicweatherPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 6:
        bypass = AllergicweatherSymptom.objects.get(Sequence=5)
        request.session[bypass.QuestionName] = value
        query_question = AllergicweatherSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/5)*100
        return render(request, 'formdiagnosis/allergicweather_ans.html', context={"percent":percentage})
    question = AllergicweatherSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = AllergicweatherSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/allergicweatherdiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def ColdallergyPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 9:
        bypass = ColdallergySymptom.objects.get(Sequence=8)
        request.session[bypass.QuestionName] = value
        query_question = ColdallergySymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/8)*100
        return render(request, 'formdiagnosis/coldallergy_ans.html', context={"percent":percentage})
    question = ColdallergySymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = ColdallergySymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/coldallergydiagnosis.html", context={"Question": question, "NextSequence": int(NextSequence) + 1})

def AccidentPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 2:
        bypass = AccidentSymptom.objects.get(Sequence=1)
        request.session[bypass.QuestionName] = value
        query_question = AccidentSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/1)*100
        return render(request, 'formdiagnosis/accident_ans.html', context={"percent":percentage})
    question = AccidentSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = AccidentSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/accidentdiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def ParasitePage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 5:
        bypass =  ParasiteSymptom.objects.get(Sequence=4)
        request.session[bypass.QuestionName] = value
        query_question =  ParasiteSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/4)*100
        return render(request, 'formdiagnosis/parasite_ans.html', context={"percent":percentage})
    question =  ParasiteSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion =  ParasiteSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/parasitediagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

def CoughPage(request, count, value):
    listtotal = []
    sumtotal = 0
    if count == 4:
        bypass = CoughSymptom.objects.get(Sequence=3)
        request.session[bypass.QuestionName] = value
        query_question =  CoughSymptom.objects.all()
        for data in query_question:
            listtotal.append(request.session[data.QuestionName])
        for i in listtotal:
            if i == 1:
                sumtotal += i
        percentage = (sumtotal/3)*100
        return render(request, 'formdiagnosis/cough_ans.html', context={"percent":percentage})
    question =  CoughSymptom.objects.get(Sequence=count)
    NextSequence = question.Sequence
    if count > 1:
        SaveQuestion = CoughSymptom.objects.get(Sequence=count-1)
        request.session[SaveQuestion.QuestionName] = value
        print(SaveQuestion.QuestionName, request.session[SaveQuestion.QuestionName])
    return render(request, "formdiagnosis/coughdiagnosis.html", context={"Question":question, "NextSequence":int(NextSequence)+1} )

