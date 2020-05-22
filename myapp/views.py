from django.shortcuts import render, redirect
from .forms import StudentForm
from docx import *


def index(request):

    if request.method == "POST":
        file = str(request.FILES['document']).split(".")
        if "docx" in file:

            document = Document(request.FILES['document'])
            lines = []
            for para in document.paragraphs:
                temp = ""
                line = (para.text).split()
                c = 0
                for x in line:
                    if (x == ":"):
                        c = 1
                    if (c > 1):
                        temp += x + " "
                    c += 1
                print(temp)
                lines.append(temp.strip())

            context = {'fname': lines[0],
                       'lname': lines[1],
                       'mail': lines[2],
                       'number': lines[3],
                       'address': lines[4],
                       'city': lines[5],
                       'state': lines[6],
                       'country': lines[7],
                       'edu': lines[8],
                       'skill': lines[9]

                       }
            store=""
            for x in context:
                if(context[x]==""):
                    store+= x+ ""
            if store != "":
                return render(request,"error.html",{"correct":store.strip()})
            form = StudentForm(context)
            print(form)
            if form.is_valid():
                form.save()
                return redirect("/index")
        else:
            return render(request,"wrongdoc.html")
    return render(request, 'index.html')


