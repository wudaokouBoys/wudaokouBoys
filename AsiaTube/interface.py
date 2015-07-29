from AsiaTube.models import *

class IUser():
    def Insert(self, user): #新建用户
        user.save()

    def Delete(self, id): #删除用户
        CUser.objects.filter(id=id).delete()

    def SelectById(self, id): #用id选择用户
        if len(CUser.objects.filter(id=id)) != 0:
            return CUser.objects.get(id=id)
        else:
            return None

    def ModifyName(self, id, newName): #修改用户名
        CUser.objects.filter(id=id).update(name=newName)

    def ModifyPassword(self, id, newPassword): #修改密码
        CUser.objects.filter(id=id).update(password=newPassword)

    def ModifyEmail(self, id, newEmail): #修改Email地址
        CUser.objects.filter(id=id).update(email=newEmail)

    def ModifyImg(self, id, newImage): #修改头像
        CUser.objects.filter(id=id).update(image=newImage)

    def ModifyAdmin(self, id, newAdmin): #修改管理员权限
        CUser.objects.filter(id=id).update(admin=newAdmin)

    def AddLikenum(self, id):  #增加赞数
        if len(CUser.objects.filter(id=id)) != 0:
            num = CUser.objects.get(id=id).likenum
            CUser.objects.filter(id=id).update(likenum=num+1)

    def UpdateUphistory(self, id, newUp):
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).uphistory
            history += str(newUp) + ' '
            CUser.objects.filter(id=id).update(uphistory=history)




