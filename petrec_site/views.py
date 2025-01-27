from collections import Counter
import os
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.urls import reverse
import pandas as pd
from .forms import FeedbackForm

global upouoarquivo
upouoarquivo = False

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'thanks.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')

def index(request):
    return render(request, 'index.html')

def graph(request):
    if(upouoarquivo):
        context = {
            'colunas': list(data.columns)
        }
        return render(request, 'graph.html', context)
    return render(request, 'graph.html')

def feedback(request):
    return render(request, 'feedback.html')

def readfile(filename):
    global data, arquivo
    arquivo = pd.read_csv(filename, sep=',', engine='python')
    data = pd.DataFrame(data=arquivo)
    global upouoarquivo
    upouoarquivo = True





def data(request):
    ex = {}

    if "POST" == request.method:
        csv_file = request.FILES["csv_file"]
        if csv_file.name.endswith('.csv'):
            savefile = FileSystemStorage()
            name = savefile.save(csv_file.name, csv_file)
            d = os.getcwd()
            file_directory = d+'/media//'+name
            readfile(file_directory)
            return redirect("/graph")
        else:
            messages.warning(request,'O tipo de arquivo não é CSV')


    return render(request, 'data.html')






