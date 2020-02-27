from django.shortcuts import render, redirect
from wine_quality_testing.models import wine
from django.http import HttpResponse
import joblib
# Create your views here.
def home(request):
    return render(request,'home.html')

def wineDetails(request):
    wine1 = wine()
    
    alochol = request.POST.get("alcohol")
    malic_acid = request.POST.get("malic_acid")
    ash = request.POST.get("ash")
    alcalinity_of_ash = request.POST.get("alcalinity_of_ash")
    magnesium = request.POST.get("magnesium")
    total_phenols = request.POST.get("total_phenols")
    flavanoids = request.POST.get("flavanoids")
    nonflavanoid_phenols = request.POST.get("nonflavanoid_phenols")
    proanthocyanins =request.POST.get("proanthocyanins")
    color_intensity = request.POST.get("color_intensity")
    hue = request.POST.get("hue")
    od315_of_diluted_wines = request.POST.get("od315_of_diluted_wines")
    proline = request.POST.get("proline")

    wine1.alcohol = request.POST.get("alcohol")
    wine1.malic_acid = request.POST.get("malic_acid")
    wine1.ash = request.POST.get("ash")
    wine1.alcalinity_of_ash = request.POST.get("alcalinity_of_ash")
    wine1.magnesium = request.POST.get("magnesium")
    wine1.total_phenols = request.POST.get("total_phenols")
    wine1.flavanoids = request.POST.get("flavanoids")
    wine1.nonflavanoid_phenols = request.POST.get("nonflavanoid_phenols")
    wine1.proanthocyanins = request.POST.get("proanthocyanins")
    wine1.color_intensity = request.POST.get("color_intensity")
    wine1.hue = request.POST.get("hue")
    wine1.od315_of_diluted_wines = request.POST.get("od315_of_diluted_wines")
    wine1.proline = request.POST.get("proline")


    X = [[alochol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocyanins, color_intensity, hue, od315_of_diluted_wines, proline ]]

    loaded_model = joblib.load('/home/dipak/workspace/Wine_Quality_Testing/ML/final_prediction.pickle')
    
    score = loaded_model.predict(X)
    print(score)
    response = HttpResponse("Ho gaya")
    return response

def modelPrediction(request ,id):
    print("=====start===")
    X = list(wine.objects.filter(id=id))
    pass
    # print(id)
    # print(type(X))
    # print("=====end===")
    # for x in X:
    #     print(x)
    # # =======Linking ML Model begins====
    # loaded_model = joblib.load('/home/volv/wine_quality/ML/final_prediction.pickle')
    
    # score = loaded_model.predict(X)
    # # =======Linking ML Model ends====

    return render(request, "prediction.html", {"score": score})