from django.db import models


class Account(models.Model):
    external_id = models.TextField(null=True, default=None, blank=True)
    salesperson = models.TextField(null=True, default=None, blank=True)
    owner_email = models.TextField(null=True, default=None, blank=True)
    company_name = models.TextField(null=True, default=None, blank=True)
    company_natural = models.TextField(null=True, default=None, blank=True)
    company_website = models.TextField(null=True, default=None, blank=True)
    company_details = models.TextField(null=True, default=None, blank=True)
    full_address = models.TextField(null=True, default=None, blank=True)
    city = models.TextField(null=True, default=None, blank=True)
    state = models.TextField(null=True, default=None, blank=True)
    zipcode = models.TextField(null=True, default=None, blank=True)
    country = models.TextField(null=True, default=None, blank=True)
    phone = models.TextField(null=True, default=None, blank=True)
    company_linkedin = models.TextField(null=True, default=None, blank=True)
    company_industry = models.TextField(null=True, default=None, blank=True)
    number_of_employees = models.TextField(null=True, default=None, blank=True)
    revenue_in_millions_in_usd = models.TextField(
        null=True, default=None, blank=True)
    company_region = models.TextField(null=True, default=None, blank=True)

    def __str__(self):
        return self.external_id


class Activity(models.Model):
    account = models.ForeignKey(Account)
    activity = models.TextField(null=True, default=None, blank=True)

    def __str__(self):
        return self.activity
