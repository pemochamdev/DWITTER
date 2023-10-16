from django.shortcuts import render, get_object_or_404

from dwitter.models import Profile

def dashboard(request):
    return render(request, 'base.html')


def profile_list(request):
    user = request.user
    profiles = Profile.objects.exclude(user = user)

    context = {
        'profiles':profiles
    }
    return render(request, 'dwitter/profile_list.html', context=context)

def profile_views(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    context = {
        'profile':profile,
    }
    return render(request, 'dwitter/profile.html', context=context)
