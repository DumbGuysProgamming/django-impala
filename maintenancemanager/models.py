from django.db import models

class DataChangeLog(models.Model):
    scn = models.IntegerField(primary_key=True)
    connection_datetime = models.DateTimeField()
    def __str__(self):
        return '{}|{}'.format(self.scn, self.connection_datetime)

class ClientType(models.Model):
    client_type_id = models.IntegerField()
    client_type = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '{}|{}|{}'.format(self.scn, self.client_type_id, self.client_type)

class Client(models.Model):
    client_guid = models.CharField(max_length=32, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    email_address = models.EmailField(max_length=50)
    client_type_id = models.ForeignKey(ClientType)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.client_guid, self.first_name, self.last_name, self.phone_number
                         , self.email_address, str(self.client_type_id)])

class Vehicle(models.Model):
    vehicle_guid = models.CharField(max_length=32, primary_key=True)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.vehicle_guid, self.year, self.make, self.model])

class Ownership(models.Model):
    client_guid = models.ForeignKey(Client)
    vehicle_guid = models.ForeignKey(Vehicle)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.client_guid, self.vehicle_guid])

class Service(models.Model):
    service_guid = models.CharField(max_length=32, primary_key=True)
    vehicle_guid = models.ForeignKey(Vehicle)
    mileage_frequency = models.IntegerField()
    duration_frequency = models.DurationField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.service_guid, self.vehicle_guid, str(self.mileage_frequency)
                         , str(self.duration_frequency), str(self.cost)])


class ServiceTransaction(models.Model):
    transaction_guid = models.CharField(max_length=32, primary_key=True)
    client_guid = models.ForeignKey(Client)
    service_guid = models.ForeignKey(Service)
    mileage = models.IntegerField()
    date = models.DateField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.transaction_guid, self.client_guid, self.service_guid
                         , str(self.mileage), self.date])

class Shop(models.Model):
    client_guid = models.ForeignKey(Client)
    address = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.client_guid, self.address])

class ShopService(models.Model):
    client_guid = models.ForeignKey(Client)
    service_guid = models.ForeignKey(Service)
    shop_service_cost = models.DecimalField(max_digits=20, decimal_places=2)
    shop_service_time = models.DurationField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(self.scn), self.client_guid, self.service_guid, str(self.shop_service_cost)
                         , str(self.shop_service_time)])
