#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    pass
    def __init__(self, name = "Leonardo da Vinci", job = "Finance"):
        self.name = name
        self.job = job

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1<=len(name)<=25:
            name = name.title()
            self._name = name
        
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)
    

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job

        else:
            print("Job must be in list of approved jobs.")
    
    job = property(get_job, set_job)


pythagoras = Person(name = "Pythagoras", job = "Research & Development")
print(pythagoras.name)
print(pythagoras.job)

artist = Person(job = "Marketing")
print(artist.name)
print(artist.job)

salesman = Person(name = 123)
setattr(salesman, "name", "Michael")
print(salesman.name)
print(salesman.job)

salesman.job = "Sales"
print(getattr(salesman, "job"))

coo = Person(name = "Elon", job = "Driver")
print(coo.name)

setattr(coo, "job", "Admin")
print(coo.job)


