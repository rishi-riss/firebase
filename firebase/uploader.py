from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
from firebase_admin import db

class IndexView(TemplateView):
    template_name = 'index.html'

class SubmitView(View):
    def post(self, request):
        # Get the form data
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        email = request.POST.get('email')

        # Create a dictionary with the data
        data = {
            'name': name,
            'age': age,
            'email': email
        }

        # Add the data to a Firestore collection
        doc_ref = db.collection('users').document()
        doc_ref.set(data)

        return render(request, 'success.html')
