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
        return '|'.join([str(scn), client_guid, first_name, last_name, phone_number
                         , email_address, str(client_type_id)])

class Vehicle(models.Model):
    vehicle_guid = models.CharField(max_length=32, primary_key=True)
    year = models.IntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), vehicle_guid, year, make, model])

class Ownership(models.Model):
    client_guid = models.ForeignKey(Client)
    vehicle_guid = models.ForeignKey(Vehicle)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), client_guid, vehicle_guid])

class Service(models.Model):
    service_guid = models.CharField(max_length=32, primary_key=True)
    vehicle_guid = models.ForeignKey(Vehicle)
    mileage_frequency = models.IntegerField()
    duration_frequency = models.DurationField()
    cost = models.DecimalField(max_digits=20, decimal_places=2)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), service_guid, vehicle_guid, str(mileage_frequency)
                         , str(duration_frequency), str(cost)])


class ServiceTransaction(models.Model):
    transaction_guid = models.CharField(max_length=32, primary_key=True)
    client_guid = models.ForeignKey(Client)
    service_guid = models.ForeignKey(Service)
    mileage = models.IntegerField()
    date = models.DateField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), transaction_guid, client_guid, service_guid
                         , str(mileage), date])

class Shop(models.Model):
    client_guid = models.ForeignKey(Client)
    address = models.CharField(max_length=50)
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), client_guid, address])

class ShopService(models.Model):
    client_guid = models.ForeignKey(Client)
    service_guid = models.ForeignKey(Service)
    shop_service_cost = models.DecimalField(max_digits=20, decimal_places=2)
    shop_service_time = models.DurationField()
    scn = models.ForeignKey(DataChangeLog)
    def __str__(self):
        return '|'.join([str(scn), client_guid, service_guid, str(shop_service_cost)
                         , str(shop_service_time)])
