from django.shortcuts import render
from firebase import db
def view(request):
    ref=db.reference('D:\photos\wallpapers')
    data=ref.get()
    context={'image':data}
    return render(request,'index.html',context)