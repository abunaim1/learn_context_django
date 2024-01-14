from django.shortcuts import render

# when we give data back end to fornt end with a dictionary it is called context

def home(request):
    d = {'author' : 'Naim', 'age' : 20, 'lst' : [1,2,3,4]}
    return render(request,'home.html', d)