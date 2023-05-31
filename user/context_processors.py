from .models import *

def get_profiles(request):
    if request.user.is_authenticated:
        profiller = Profile.objects.filter(user=request.user)
    else:
        profiller =''
    context={
        'profiller':profiller
    }
    return context