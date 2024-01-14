from django.shortcuts import render

# when we give data back end to fornt end with a dictionary it is called context

def home(request):
    d = {'author' : 'Naim', 'age' : 10, 'lst' : [1,2,3,4], 'courses' : [
            {
                'id' : 1,
                'name' : 'python',
                'fee' : 10000
            },
            {
                'id' : 2,
                'name' : 'Django',
                'fee' : 12000
            },
            {
                'id' : 3,
                'name' : 'C',
                'fee' : 2000
            },
        ]
    }
    return render(request,'home.html', d)