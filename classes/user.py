class User:
    def __init__(self, name, lastname, age, email, phone, address, city, state, country):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.country = country

        self.jobs = None
        self.hours_per_week = None
        self.days_per_week = None
        self.weeks_per_year = None


    def get_name(self):
        return self.name

    def get_lastname(self):
        return self.lastname

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country

    def get_jobs(self):
        return self.jobs

    def get_hours_per_week(self):
        return self.hours_per_week

    def get_days_per_week(self):
        return self.days_per_week

    def get_weeks_per_year(self):
        return self.weeks_per_year

    def set_jobs(self, jobs):
        self.jobs = jobs

    def set_hours_per_week(self, hours_per_week):
        self.hours_per_week = hours_per_week

    def set_days_per_week(self, days_per_week):
        self.days_per_week = days_per_week

    def set_weeks_per_year(self, weeks_per_year):
        self.weeks_per_year = weeks_per_year