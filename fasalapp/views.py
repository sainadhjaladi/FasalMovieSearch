from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.contrib import messages
from .models import Playlist


def loginregister(request):
    return render(request, 'loginregister.html')


def insertuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['pass']
        us = User(uname=username, phone=phone, uemail=email, password=password)
        us.save()
        messages.success(request, 'User registered successfully.')
    return render(request, 'loginregister.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(uemail=email, password=password)
            # Perform the login
            request.session['username'] = user.uname  # Store the username in the session
            messages.success(request, 'Login successful!')
            return redirect('success')  # Redirect to a home page after successful login
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'loginregister.html')


def success(request):
    username = request.session.get('username', 'Guest')  # Get the username from the session
    return render(request, 'success.html', {'username': username})


def user_logout(request):
    logout(request)
    # Redirect to a different page after logout, or maybe render a template
    return redirect('loginregister')


def playlist(request):
    return render(request, 'playlist.html', {})


def add_to_playlist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        poster = request.POST.get('poster')

        # Check if the movie is already in the playlist
        if Playlist.objects.filter(title=title).exists():
            return JsonResponse({'message': 'Movie already in the playlist.'})

        # Save the movie to the playlist
        playlist_item = Playlist(title=title, poster=poster)
        playlist_item.save()
        return JsonResponse({'message': 'Movie added to the playlist successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)


def get_playlist(request):
    playlist = Playlist.objects.all().values('title', 'poster')  # Fetch all playlist items from the database
    return JsonResponse(list(playlist), safe=False)


@csrf_exempt
def remove_from_playlist(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            title = data.get('title')
            if title:
                playlist_item = get_object_or_404(Playlist, title=title)
                playlist_item.delete()
                return JsonResponse({'message': 'Item removed from playlist.'})
            else:
                return JsonResponse({'error': 'Title parameter missing.'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON payload.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)
