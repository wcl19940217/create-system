from django.db import models

# Create your models here.
# 用户信息
class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=60)
    jf = models.IntegerField(default=0)

    def __repr__(self):
        return '<user{}{}{}{}>'.format(self.username,self.password,self.email,self.jf)

    __str__ = __repr__

# 提交的建议的模型类，该模型类与User表是多对一的关系，用外键关联
class Sug(models.Model):
    class Meta:
        db_table = 'sug'

    id = models.AutoField(primary_key=True)
    fl = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=1000)
    filename = models.CharField(max_length=100, default='')
    # 创建外键
    uid = models.ForeignKey('User', on_delete=models.CASCADE)
    # 标记合理化创意委员会是否处理该创意
    is_sl = models.BooleanField(default=False)
    # 是否受理该创意
    sl = models.BooleanField()
    # 创意采纳的等级
    dj = models.CharField(max_length=10)
    # 创意的执行人
    zxr = models.CharField(max_length=20)
    uname = models.CharField(max_length=20)

    def __repr__(self):
        return '<user{}{}{}{}>'.format(self.fl, self.title, self.content, self.filename)

    __str__ = __repr__