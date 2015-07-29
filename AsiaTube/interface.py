from AsiaTube.models import *

class IUser():
    def Insert(self, user): #�½��û�
        user.save()

    def Delete(self, id): #ɾ���û�
        CUser.objects.filter(id=id).delete()

    def SelectById(self, id): #��idѡ���û�
        if len(CUser.objects.filter(id=id)) != 0:
            return CUser.objects.get(id=id)
        else:
            return None

    def ModifyName(self, id, newName): #�޸��û���
        CUser.objects.filter(id=id).update(name=newName)

    def ModifyPassword(self, id, newPassword): #�޸�����
        CUser.objects.filter(id=id).update(password=newPassword)

    def ModifyEmail(self, id, newEmail): #�޸�Email��ַ
        CUser.objects.filter(id=id).update(email=newEmail)

    def ModifyImg(self, id, newImage): #�޸�ͷ��
        CUser.objects.filter(id=id).update(image=newImage)

    def ModifyAdmin(self, id, newAdmin): #�޸Ĺ���ԱȨ��
        CUser.objects.filter(id=id).update(admin=newAdmin)

    def AddLikenum(self, id):  #��������
        if len(CUser.objects.filter(id=id)) != 0:
            num = CUser.objects.get(id=id).likenum
            CUser.objects.filter(id=id).update(likenum=num+1)

    def UpdateUphistory(self, id, newUp):
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).uphistory
            history += str(newUp) + ' '
            CUser.objects.filter(id=id).update(uphistory=history)




