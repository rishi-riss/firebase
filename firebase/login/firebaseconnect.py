from firebase_admin import firestore

def user_list(request):
    db = firestore.client()
    users_ref = db.collection('')
    users = [doc.to_dict() for doc in users_ref.get()]
    return render(request, 'user_list.html', {'users': users})