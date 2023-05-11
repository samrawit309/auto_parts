from django.db import models

class Make(models.Model):
    """A topic the user is requesting about"""
    text =models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """return a string representation of the model"""
        return self.text

 
class Entry(models.Model):
    """Something specfic requested about the car"""
    make = models.ForeignKey(Make,on_delete=models.CASCADE)
    modelcar=models.ForeignKey(ModelCar,on_delete=models.CASCADE)
    text = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
       """return a string reprsentation of the model"""
       return self.text[:50] + "....."
    


