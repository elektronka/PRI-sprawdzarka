from django.db import models



class Student(models.Model):
    snumber = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()

class Plagiaty(models.Model):
    id=models.IntegerField(primary_key=True)
    snumber=models.IntegerField(max_length=6)
    sprawko_name=models.CharField(max_length=32)
    plagiat_percentage=models.IntegerField(max_length=3)
    with_who=models.IntegerField(max_length=6)


class Szablon_zadan(models.Model):
    przedmiot=models.CharField(max_length=32)
    temat=models.CharField(max_length=32)
    nr_zadania=models.IntegerField(max_length=2)
    pkt_zadanie= models.IntegerField(max_length=2)
    tresc=models.CharField(max_length=2000)
    pop_roz=models.CharField(max_length=2000)

class groups(models.Model):
    nazwa=models.CharField(primary_key=True,max_length=5)
    przedmiot=models.CharField(max_length=32)
    opis=models.CharField(max_length=32)