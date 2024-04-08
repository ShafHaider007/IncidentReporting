
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from myapp.models import Incident
from accounts.models import Resident, Admin 
from django.http import  JsonResponse
from django.db import connection



def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                #using sql query
                with connection.cursor() as cursor:
                    cursor.execute("SELECT * FROM accounts_resident WHERE user_id = %s", [user.id])
                    is_resident = cursor.fetchone()

                    cursor.execute("SELECT * FROM accounts_admin WHERE user_id = %s", [user.id])
                    is_admin = cursor.fetchone()

                if is_resident:
                    request.session['user_role'] = 'resident'
                    messages.success(request, f"Welcome, {user.username}!")
                elif is_admin:
                    request.session['user_role'] = 'admin'
                    messages.success(request, f"Welcome, {user.username}!")
                else:
                    messages.error(request, "Invalid user role")

                return render(request, "index.html", {'user': request.user, 'messages': messages.get_messages(request)})
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Please provide both username and password.")

    return render(request, "login.html", {'messages': messages.get_messages(request)})



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        role = request.POST["role"]

        #check for the user name
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken. Please choose a different one.")
            return redirect("register")

        if pass1 == pass2:
            # Create a User and assign the role
            user = User.objects.create_user(username=username, email=email, password=pass1)
            user.first_name = fname
            user.last_name = lname
            user.save()

            if role == 'RESIDENTS':
                # Assuming you have a UserProfile model with a OneToOneField to User for residents
                resident_profile = Resident.objects.create(user=user, lname=lname, fname=fname, email=email)
                resident_profile.save()
            elif role == 'ADMIN':
                # Assuming you have a UserProfile model with a OneToOneField to User for admins
                admin_profile = Admin.objects.create(user=user, lname=lname, fname=fname, email=email)
                admin_profile.save()
                
            else:
                messages.error(request, "Invalid user role")
                return redirect("register")
            messages.success(request, "Registered successfully")
            return redirect("user_login")
        else:
            messages.error(request, "Passwords do not match")
            return redirect("register")
    else:
        return render(request, "register.html")

def user_logout(request):
    logout(request)
    return redirect("home")

def checkreport(request):
    pending_incidents = Incident.objects.filter(status__status_name="Pending")
    return render(request, "adminreports.html", {"pending_incidents": pending_incidents})
