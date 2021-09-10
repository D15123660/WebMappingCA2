from django.shortcuts import render


locations = [
    dict(author='MS', content='First content', title='location', date_posted='August 27, 2018')
]


# @login_required
def home(request):
    context = {
        'locations': locations
    }

    return render(request, 'home.html', context)
