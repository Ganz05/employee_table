from django.db import models

# Create your models here.
class employee(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    
   
    def __str__(self):
        return self.ename
    
class dept(models.Model):
    empno=models.ForeignKey(employee,on_delete=models.CASCADE) 
    deptno=models.IntegerField()
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100)