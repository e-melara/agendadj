from django.core.management.base import BaseCommand

import faker

from applications.persona.models import Person


class Command(BaseCommand):
    help = "para llenar la base de datos de usuario"
    
    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        
        faker.Faker.seed(0)
        for _ in range(25):
            Person.objects.create(
                full_name="{} {}".format(fake.name(), fake.last_name()),
                job=fake.job(),
                email=fake.ascii_email(),
                phone=fake.msisdn()
            )
            
        print(Person.objects.count())