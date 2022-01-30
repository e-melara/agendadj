from datetime import datetime
from random import randint
from django.core.management.base import BaseCommand

import faker
from applications.persona.models import Person, Hobby, Reunion


class Command(BaseCommand):
    help = "para llenar la base de datos de usuario"
    
    def handle(self, *args, **kwargs):
        fake = faker.Faker()
        
        faker.Faker.seed(0)
        for _ in range(20):
            person = randint(1, 25)
            now = datetime.now()
            Reunion.objects.create(
                persona_id = person,
                hora = now.strftime("%H:%M:%S"),
                fecha = datetime.now(),
                asunto = fake.company_email(),
            )
            
        # for _ in range(25):
        #     Person.objects.create(
        #         full_name="{} {}".format(fake.name(), fake.last_name()),
        #         job=fake.job(),
        #         email=fake.ascii_email(),
        #         phone=fake.msisdn()
        #     )
            
        # print(Person.objects.count())
        
        # for _ in range(10):
        #     Hobby.objects.create(
        #         hobby = fake.job()
        #     )
            
        # print(Hobby.objects.count())