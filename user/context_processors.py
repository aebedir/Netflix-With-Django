from .models import *

def get_profiles(request):
    profiller = Profile.objects.filter(user=request.user)
    context={
        'profiller':profiller
    }
    return context