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

    def UpdateUphistory(self, id, newUp): #�����ϴ���ʷ
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).uphistory
            history += str(newUp) + ' '
            CUser.objects.filter(id=id).update(uphistory=history)

    def UpdateViewhistory(self, id, newView): #���¹ۿ���ʷ
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).viewhistory
            history += str(newView) + ' '
            CUser.objects.filter(id=id).update(viewhistory=history)

    def UpdateFollow(self, id, leader): #���¹�ע�б�
        if len(CUser.objects.filter(id=id)) != 0:
            leaders = CUser.objects.get(id=id).follow
            leaders += str(leader) + ' '
            CUser.objects.filter(id=id).update(follow=leaders)

    def UpdateFollowme(self, id, follower): #���¹�ע�б�
        if len(CUser.objects.filter(id=id)) != 0:
            followers = CUser.objects.get(id=id).followme
            followers += str(follower) + ' '
            CUser.objects.filter(id=id).update(followme=followers)

    def GetlastUserId(self): #��ȡ���id
        if len(CUser.objects.order_by('-id')) != 0:
            return CUser.objects.order_by('-id')[0].id
        else:
            return


class IVideo():
    def Insert(self, video): #�����Ƶ
        video.save()

    def Delete(self, id):  #ɾ����Ƶ
        CVideo.objects.filter(id=id).delete()

    def SelectById(self, id): #��idѡ����Ƶ
        if len(CVideo.objects.filter(id=id)) != 0:
            return CVideo.objects.get(id=id)
        else:
            return None

    def Search(self, condition): #������Ƶ
        return

    def ModifyTitle(self, id, newTitle): #�޸���Ƶ����
        CVideo.objects.filter(id=id).update(title=newTitle)

    def ModifyDiscribe(self, id, newDis): #�޸���Ƶ����
        CVideo.objects.filter(id=id).update(discribe=newDis)

    def ModifyKeyword(self, id, newKeyword): #�޸���Ƶ�ؼ���
        CVideo.objects.filter(id=id).update(keyword=newKeyword)

    def ModifyType(self, id, newType): #�޸���Ƶ���
        CVideo.objects.filter(id=id).update(type=newType)

    def ModifyUpper(self, id, newUpper): #�޸��ϴ���
        CVideo.objects.filter(id=id).update(upper=newUpper)

    def ModifyTime(self, id, newTime): #�޸��ϴ�ʱ��
        CVideo.objects.filter(id=id).update(time=newTime)

    def ModifyPath(self, id, newPath): #�޸���Ƶ����·��
        CVideo.objects.filter(id=id).update(path=newPath)

    def ModifyState(self, id, newState): #�޸���Ƶ���״̬
        CVideo.objects.filter(id=id).update(state=newState)

    def UpdateComments(self, id, newComments): #������Ƶ����
        if len(CVideo.objects.filter(id=id)) != 0:
            comment = CVideo.objects.get(id=id).comments
            comment += str(newComments) + ' '
            CVideo.objects.filter(id=id).update(comments=comment)

    def UpdateBsreen(self, id, newBsreen): #������Ƶ��Ļ
        if len(CVideo.objects.filter(id=id)) != 0:
            bsreens = CVideo.objects.get(id=id).bsreen
            bsreens += str(newBsreen) + ' '
            CVideo.objects.filter(id=id).update(bsreen=bsreens)

    def AddLikenum(self, id): #������Ƶ����
        if len(CVideo.objects.filter(id=id)) != 0:
            num = CVideo.objects.get(id=id).likenum
            CVideo.objects.filter(id=id).update(likenum=num+1)

    def AddPlaynum(self, id): #������Ƶ������
        if len(CVideo.objects.filter(id=id)) != 0:
            num = CVideo.objects.get(id=id).playnum
            CVideo.objects.filter(id=id).update(playnum=num+1)

    def GetlastVideoId(self): #��ȡ���id
        if len(CVideo.objects.order_by('-id')) != 0:
            return CVideo.objects.order_by('-id')[0].id
        else:
            return 0

