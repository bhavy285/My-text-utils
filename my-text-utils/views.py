from typing import Counter
from django import http
from django.http import HttpResponse
from django.shortcuts import render

# def het(request):
#     return HttpResponse('''<h1>this is Het</h1><br> <a href="https://www.instagram.com/direct/inbox/" >insta bhavy shah</a>''')


# def hitul(request):
#     return HttpResponse("this is hitul shah")

def index(request):
    # return HttpResponse('''<h1> home</h1> <br> <a href="removepunc">removepunc </a><br><a href="newline">newline </a>   ''')
    # params = {'name' : 'Bhavy' , 'place' : 'Neptune'}
    # return render(request,'index.html' ,params)
    return render(request, 'index.html')


def analyzer(request):
    #  we get the text
    djtext = request.POST.get('text', 'default')
    # for the checkbox
    removepunc = request.POST.get('removepunc', 'off')
    capslock = request.POST.get('capslock', 'off')
    linere = request.POST.get('linere', 'off')
    spacecl = request.POST.get('spacecl', 'off')
    exspcl = request.POST.get('exspcl', 'off')
    chacou = request.POST.get('chacou', 'off')
    # print(request.GET.get('removepunc' , 'default'))
    # print(djtext)
    # print(removepunc)
    if removepunc == "on":

        punctions = ''' !()-[]{}/*-`<>/?;:='",.@#$%^&*()-_++'''
        analyzed = ""
        for char in djtext:
            if char not in punctions:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctions', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    # here very import note that
    # we have always make the same name at index.html and in views.py
    # here in index.html we gave the capslock name so in views.py we have to give that name complasary

    if(capslock == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'capatize it', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    if(linere == 'on'):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'newline remover ', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    if(spacecl == 'on'):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed = analyzed + char
        params = {'purpose': 'space remover ', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    if(exspcl == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extra space remover ', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    if(chacou == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'character counter ', 'analyzed_text': analyzed}
        djtext = analyzed

        # return render(request, 'analyzer.html' ,params)

    return render(request, 'analyzer.html', params)
    # else:
    #     return HttpResponse("Error")
    # return HttpResponse("this is remove page")

# def newline(request):
#     return HttpResponse("this is new line")

# def analyzer(request):
#     return HttpResponse("this is analyzer")
