from django.shortcuts import render


def index(request):
    return render(request, 'calorie_counter/index.html')


def calculate_bmr(weight, height, age, gender):
    if gender == 'male':
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    return bmr


def calculate_tdee(bmr, activity_level):
    tdee = bmr * activity_level
    return tdee


def calorie_counter(request):
    if request.method == 'POST':
        weight = float(request.POST['weight'])
        height = float(request.POST['height'])
        age = int(request.POST['age'])
        gender = request.POST['gender']
        activity_level = float(request.POST['activity_level'])
        bmr = calculate_bmr(weight, height, age, gender)
        tdee = calculate_tdee(bmr, activity_level)
        tdee_formatted = '{:.2f}'.format(tdee)
        return render(request, 'calorie_counter/calorie_counter_results.html', {'tdee': tdee_formatted})
    else:
        return render(request, 'calorie_counter/calorie_counter.html')


def about(request):
    return render(request, 'calorie_counter/about.html')
