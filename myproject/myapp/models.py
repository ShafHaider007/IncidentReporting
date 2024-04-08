from django.db import models
from django.db import models, connection


# Create your models here.
# class Incident(models.Model):
#     report_id = models.BigAutoField(
#         auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
#     )
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     description = models.TextField()
#     category = models.CharField(max_length=50)
#     comments = models.TextField(blank=True, null=True)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     status = models.CharField(max_length=20, default="Pending")

#     def __str__(self):
#         return f"Report ID: {self.report_id}, Name: {self.name}"

# class Incident(models.Model):
#     report_id = models.BigAutoField(
#         auto_created=True, primary_key=True, serialize=False
#     )
#     name = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15)
#     description = models.TextField()
#     category = models.CharField(max_length=50)
#     comments = models.TextField(blank=True, null=True)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     status = models.CharField(max_length=20, default="Pending")

#     def __str__(self):
#         return f"Report ID: {self.report_id}, Name: {self.name}"

#     def save_with_raw_sql(self):
#         with connection.cursor() as cursor:
#             cursor.execute(
#                 """
#                 INSERT INTO myapp_incident (name, phone, description, category, comments, latitude, longitude, status)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
#             """,
#                 [
#                     self.name,
#                     self.phone,
#                     self.description,
#                     self.category,
#                     self.comments,
#                     self.latitude,
#                     self.longitude,
#                     self.status,
#                 ],
#             )


# class IncidentStatus(models.Model):
#     status_id = models.AutoField(primary_key=True)
#     status_name = models.CharField(max_length=50, default="Pending")
#     user_name=models.CharField(max_length=100 , default="NuLL")

#     def __str__(self):
#         return self.status_name

from django.db import models

class IncidentStatus(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_name = models.CharField(max_length=50, default="Pending")
    user_name = models.CharField(max_length=100, default="NuLL")

    def __str__(self):
        return self.status_name

    def save_with_raw_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO myapp_incidentstatus (status_name, user_name, status_id)
                VALUES (%s, %s,%s)
                """,
                [
                    self.status_name,
                    self.user_name,
                    self.status_id,
                ],
            )

class Incident(models.Model):
    report_id = models.BigAutoField(
        auto_created=True, primary_key=True, serialize=False
    )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    description = models.TextField()
    category = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.ForeignKey(IncidentStatus, on_delete=models.CASCADE)

    def __str__(self):
        return f"Report ID: {self.report_id}, Name: {self.name}"

    def save_with_raw_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO myapp_incident (name, phone, description, category, comments, latitude, longitude, status_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """,
                [
                    self.name,
                    self.phone,
                    self.description,
                    self.category,
                    self.comments,
                    self.latitude,
                    self.longitude,
                    self.status_id,
                ],
            )



class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    property_type = models.CharField(
        max_length=20,
        choices=[
            ("apartment", "Apartment"),
            ("house", "House"),
            ("commercial", "Commercial Property"),
            ("land", "Land"),
        ],
    )
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    def save_with_raw_sql(self):
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO yourapp_contactinquiry (name, email, phone, property_type, subject, message)
                VALUES (%s, %s, %s, %s, %s, %s)
            """,
                [
                    self.name,
                    self.email,
                    self.phone,
                    self.property_type,
                    self.subject,
                    self.message,
                ],
            )
