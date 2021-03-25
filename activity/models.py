from django.db import models

class Account(models.Model):
    external_id = models.TextField()
    salesperson = models.TextField()
    owner_email = models.TextField()
    company_name = models.TextField()
    company_natural = models.TextField()
    company_website = models.TextField()
    company_details = models.TextField()
    full_address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()
    country = models.TextField()
    phone = models.TextField()
    company_linkedin = models.TextField()
    company_industry = models.TextField()
    number_of_employees = models.TextField()
    revenue_in_millions_in_usd = models.TextField()
    company_region = models.TextField()

    def __str__(self):
        return self.external_id