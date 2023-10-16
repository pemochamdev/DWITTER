from django.shortcuts import render, get_object_or_404

from dwitter.models import Profile, Dweet

def dashboard(request):
    all_dweet = Dweet.objects.filter(user = request.user)

    context = {'all_dweet':all_dweet}
    return render(request, 'dwitter/dashboard.html', context)


def profile_list(request):
    user = request.user
    profiles = Profile.objects.exclude(user = user)

    context = {
        'profiles':profiles
    }
    return render(request, 'dwitter/profile_list.html', context=context)



def profile_views(request, pk):
    
    profile = get_object_or_404(Profile, pk=pk)
    if request.method =='POST':
        curent_user_profile = request.user.profile
        data = request.POST
        action = data.get('follow')
        if action =='follow':
            curent_user_profile.follows.add(profile)
        elif action =='unfollow':
            curent_user_profile.follows.remove(profile)
        curent_user_profile.save()
    context = {
        'profile':profile,
    }
    return render(request, 'dwitter/profile.html', context=context)
