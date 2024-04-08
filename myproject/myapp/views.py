from contextlib import _RedirectStream
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse
from django.http import JsonResponse
from .models import ContactInquiry, Incident, IncidentStatus
from django.contrib import messages
from django.db import IntegrityError, connection
from django.db import transaction


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        property_type = request.POST.get("property-type")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save data to the database
        inquiry = ContactInquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            property_type=property_type,
            subject=subject,
            message=message,
        )
        inquiry.save()
        messages.success(request, "form reported successfully!")
        context["success"] = True
        context["name"] = name
        # Redirect to a success page

    return render(request, "contact.html", context)





def status(request):
    return render(request, "status.html")




def report(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        description = request.POST.get("description")
        category = request.POST.get("category")
        comments = request.POST.get("comments", "")
        lat_str = request.POST.get("latitude", "")
        long_str = request.POST.get("longitude", "")
        
        if lat_str.strip() and long_str.strip():
            latitude = float(lat_str)
            longitude = float(long_str)

        # Use transaction.atomic to ensure atomicity of the database operations
        with transaction.atomic():
            # Save the incident status
            myincidentstatus = IncidentStatus.objects.create(
                status_name="Pending",
                user_name=name
            )

            # Save the incident to the database with the associated status
            myincident = Incident.objects.create(
                name=name,
                phone=phone,
                description=description,
                category=category,
                comments=comments,
                latitude=latitude,
                longitude=longitude,
                status=myincidentstatus  # Assign the IncidentStatus object directly
            )
            myincident.save()
            myincidentstatus.save()

        messages.success(request, "Incident reported successfully!")
        context["success"] = True
        context["name"] = name

    return render(request, "report.html", context)



# def check_status(request):
#        if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')

#         # Query the database to get the status
#         report = get_object_or_404(Incident, name=name, phone=phone)
#         status = report.status

#         return render(request, 'status.html', {'status': status})

#        return render(request, 'status.html', {'status': None})


def check_status(request):
    status = None

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")

        # Use raw SQL query to fetch the status
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT status_name FROM myapp_incidentstatus WHERE status_id IN (SELECT status_id FROM myapp_incident WHERE name = %s AND phone = %s)",
                [name, phone],
            )
            row = cursor.fetchone()

            if row:
                status = row[0]

    return render(request, "status.html", {"status": status})
def get_incident_details(request, report_id):
    try:
        incident = Incident.objects.get(report_id=report_id)
        print(f"Report ID: {incident.report_id}")  # Add this line for debugging
        return render(request, 'incident_details.html', {'incident': incident})
    except Incident.DoesNotExist:
        return render(request, 'incident_details.html', {'error': 'Incident not found'})
    
    
def incident_list(request):
    incidents = Incident.objects.all()

    # Create a dictionary to store counts for each user
    user_report_counts = {}

    for incident in incidents:
        name = incident.name
        if name in user_report_counts:
            user_report_counts[name] += 1
        else:
            user_report_counts[name] = 1

    # Convert the dictionary into a list of tuples
    user_reports = [(name, count) for name, count in user_report_counts.items()]

    return render(request, 'incident_list.html', {'user_reports': user_reports})


# views.py


# views.py
def user_report_history(request, user_name):
    incidents = Incident.objects.filter(name=user_name)

    if request.method == 'POST':
        report_id = request.POST.get('mark_as_solved')
        if report_id:
            incident = get_object_or_404(Incident, report_id=report_id)
            solved_status = get_object_or_404(IncidentStatus, status_name='Solved')

            # Check if the incident is not already solved before updating
            if incident.status != solved_status:
                incident.status = solved_status
                IncidentStatus.status_name='Solved'
                
                
                incident.save()
                messages.success(request, f'Report {report_id} marked as solved.')

                # Redirect back to incident_list
                return redirect('incident_list')

    return render(request, 'user_report_history.html', {'user_name': user_name, 'incidents': incidents})


