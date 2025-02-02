from django.shortcuts import render

users = [
    {
        'name': 'John Doe',
        'email': 'johndoe@gmail.com',
        'phone': '555-555-5555',
        'password': 'password1'
        },
    {
        'name': 'Jane Doe',
        'email': 'janedoe@gmail.com',
        'phone': '555-555-5553',
        'password': 'password2'
    }
]
def home(request):
    return render(request, 'user_profile/profile.html', {'users': users, 'title': 'User Profile'})

def about(request):
    return render(request, 'user_profile/about.html', {'title': 'About'})