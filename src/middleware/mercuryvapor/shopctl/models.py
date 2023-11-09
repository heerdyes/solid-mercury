from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    phnum = models.CharField(max_length=15)
    
    def __str__(self):
        return '%s (%s)'%(self.name, self.phnum)


class Source(models.Model):
    estname = models.CharField(max_length=30)
    esttype = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    phnum = models.CharField(max_length=15)
    address = models.CharField(max_length=30)
    
    def __str__(self):
        return '%s (%s), %s'%(self.estname, self.esttype, self.owner)


class Category(models.Model):
    generalname = models.CharField(max_length=30)
    specificname = models.CharField(max_length=30)
    comments = models.TextField()
    
    def __str__(self):
        return '%s (%s) [%s]'%(self.generalname, self.specificname, self.comments)


class Procbill(models.Model):
    createdon = models.DateTimeField(auto_now_add=True)
    paid = models.IntegerField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    
    def __str__(self):
        return '[%d] %s, %s'%(self.id, str(self.createdon), 'paid' if self.paid == 1 else 'pending')


class Purchase(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    procbill = models.ForeignKey(Procbill, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'item: %s, qty: %f, price: %f, billid: %d'%(str(self.category), self.qty, self.price, self.procbill.id)


class Batch(models.Model):
    expireson = models.DateTimeField()
    sp = models.FloatField()
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'usebefore: %s, mrp: %f'%(str(self.expireson), self.sp)


class Custbill(models.Model):
    createdon = models.DateTimeField(auto_now_add=True)
    paid = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    def __str__(self):
        return 'bill for %s, date: %s, %s'%(str(self.customer), str(self.createdon), 'paid' if self.paid == 1 else 'pending')


class Sale(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    qty = models.FloatField()
    price = models.FloatField()
    custbill = models.ForeignKey(Custbill, on_delete=models.CASCADE)
    
    def __str__(self):
        return '%s, %f, %f, [%s]'%(self.batch.purchase.category.generalname, self.qty, self.price, str(self.custbill))


class Stock(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    qty = models.FloatField()
    
    def __str__(self):
        icat = self.batch.purchase.category
        itemnm = icat.generalname + ' ' + icat.specificname
        return '%s, qty: %f'%(itemnm, self.qty)


class Pricelog(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    updatedon = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    
    def __str__(self):
        return '[batch:%d] modified %s, price: %f'%(self.batch.id, str(self.updatedon), self.price)

