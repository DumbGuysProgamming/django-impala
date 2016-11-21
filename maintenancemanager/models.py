from django.db import models

class DataChangeLog(models.Model):
    scn = models.IntegerField(primary_key=True)
    connection_datetime = models.DateTimeField()
    def __str__(self):
        return '|'.join([str(self.connection_datetime)])

class ClientType(models.Model):
    client_type_id = models.IntegerField()
    client_type = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.client_type])

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email_address = models.EmailField(max_length=50)
    client_type_id = models.ForeignKey(ClientType)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.last_name, self.first_name, str(self.client_type_id)])

class Vehicle(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.year), self.make, self.model])

class Ownership(models.Model):
    client_id = models.ForeignKey(Client)
    vehicle_id = models.ForeignKey(Vehicle)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.client_id.last_name, self.client_id.first_name, str(self.vehicle_id.year), self.vehicle_id.make, self.vehicle_id.model])

class Service(models.Model):
    vehicle_id = models.ForeignKey(Vehicle)
    service_name = models.CharField(max_length=50)
    mileage_frequency = models.IntegerField()
    duration_frequency = models.DurationField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.service_name, str(self.mileage_frequency)
                         , str(self.duration_frequency), str(self.cost)])

class ServiceTransaction(models.Model):
    client_id = models.ForeignKey(Client)
    service_id = models.ForeignKey(Service)
    mileage = models.IntegerField()
    date = models.DateField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.id), self.service_id.service_name, str(self.mileage), str(self.date)])

class Shop(models.Model):
    client_id = models.ForeignKey(Client)
    address = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.client_id.first_name, self.client_id.last_name, self.address])

class ShopService(models.Model):
    shop_id = models.ForeignKey(Shop, default=2)
    service_id = models.ForeignKey(Service)
    shop_service_cost = models.DecimalField(max_digits=20, decimal_places=2)
    shop_service_time = models.DurationField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([self.shop_id.client_id.last_name, self.shop_id.client_id.first_name
                         , self.service_id.service_name, str(self.shop_service_cost)
                         , str(self.shop_service_time)])
