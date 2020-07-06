from django.db import models


class GitCategory(models.Model):
    category=models.CharField(verbose_name='类别',max_length=40)

    class Meta:
        db_table='gitcategory'
        verbose_name='类别'

    def __str__(self):
        return str(self.category)


# Create your models here.
class GitVersion(models.Model):
    func=models.CharField(verbose_name='功能',max_length=1000)
    command=models.CharField(verbose_name='命令',max_length=500)
    comment =models.CharField(verbose_name='备注',max_length=1000,null=True,blank=True)
    cate=models.ForeignKey('GitCategory',null=True,blank=True,on_delete=models.DO_NOTHING,verbose_name='分类')

    class Meta:
        db_table='gitversion'
        verbose_name='git版本管理'

    def __str__(self):
        return str(self.func)
