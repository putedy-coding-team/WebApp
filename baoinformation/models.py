from django.db import models

# Create your models here.


class BaoNumber(models.Model):
    bao_number = models.IntegerField(verbose_name="包号", unique=True)
    start_work_time = models.DateTimeField(verbose_name="开始服役时间")
    on_line = models.BooleanField(verbose_name="在线状态")
    bao_empty = models.CharField(verbose_name="空信息", max_length=200, default="1")

    def __str__(self):
        return str(self.bao_number)

    class Meta:
        verbose_name = "包号信息"
        verbose_name_plural = "包号信息"


class PublicInformation(models.Model):
    bao_number = models.ForeignKey('BaoNumber', on_delete=models.CASCADE)
    b_time = models.DateTimeField(verbose_name="包况时间戳")
    first_temp_area = models.CharField(verbose_name="高温区域1", max_length=50)
    first_temp_value = models.CharField(verbose_name="高温值1", max_length=50)
    second_temp_area = models.CharField(verbose_name="高温区域2", max_length=50)
    second_temp_value = models.CharField(verbose_name="高温值2", max_length=50)
    first_empty = models.CharField(verbose_name="空信息1", max_length=200, default="1")
    second_empty = models.CharField(verbose_name="空信息2", max_length=200, default="1")
    third_empty = models.CharField(verbose_name="空信息3", max_length=200, default="1")
    is_delete = models.BooleanField(verbose_name="删除", default=False)

    def __str__(self):
        return str(self.b_time)

    class Meta:
        ordering = ["-b_time"]
        verbose_name = "包况信息"
        verbose_name_plural = "包况信息"


class MaintainInformation(models.Model):
    bao_number = models.ForeignKey('BaoNumber', on_delete=models.CASCADE)
    m_time = models.DateTimeField(verbose_name="维护时间")
    m_information = models.CharField(verbose_name="维护信息", max_length=200)
    m_description = models.CharField(verbose_name="维护说明", max_length=200)
    m_empty = models.CharField(verbose_name="空信息", max_length=200, default="1")

    def __str__(self):
        return str(self.m_time)

    class Meta:
        ordering = ["-m_time"]
        verbose_name = "维护信息"
        verbose_name_plural = "维护信息"


class MaintainEvent(models.Model):
    m_event = models.CharField(verbose_name="维护事件", max_length=200)
    m_event_time = models.DateTimeField(verbose_name="维护事件添加时间", auto_now_add=True)

    def __str__(self):
        return str(self.m_event_time)

    class Meta:
        ordering = ["-m_event_time"]
        verbose_name = "维护事件"
        verbose_name_plural = "维护事件"


class Hardware(models.Model):
    hardware = models.CharField(verbose_name="硬件名称", max_length=50, unique=True)
    operation_status = models.BooleanField(verbose_name="运行状态")
    hardware_online_time = models.DateTimeField(verbose_name="硬件上线时间")
    factory = models.CharField(verbose_name="硬件厂商", max_length=50)

    def __str__(self):
        return self.hardware

    class Meta:
        verbose_name = "硬件信息"
        verbose_name_plural = "硬件信息"
