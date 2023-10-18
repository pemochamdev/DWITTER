from django.shortcuts import render, get_object_or_404, redirect

from dwitter.models import Profile, Dweet
from dwitter.forms import DweetForm

def dashboard(request):
    all_dweet = Dweet.objects.filter(user__profile__in = request.user.profile.follows.all()).order_by('-created_at')
    if request.method =='POST':
        form = DweetForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return redirect('/')
    else:
        form = DweetForm()


    context = {
        'all_dweet':all_dweet,
        'form':form,
        }
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
