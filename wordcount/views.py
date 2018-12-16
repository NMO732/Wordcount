from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    #return HttpResponse('<h1>This is your Home Page</h1>')
    return render(request,'home.html',{'name':"Hi There Nikhil"})


def contact(request):
    return HttpResponse('<h1>Contact Page</h1><br><h2>This is Contact Page</h2>')

def count(request):
    data = request.GET['fulltextarea']
    print(data)
    word_list=data.split()
    print(word_list)
    list_length = len(word_list)
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word]=1
    #sorted_list= sorted(worddictionary.items(),key = operator.itemgetter(1))
    return render(request,'count.html', {'fulltext': data, 'words': list_length,'worddictionary': worddictionary.items()})
