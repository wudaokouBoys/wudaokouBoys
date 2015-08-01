from AsiaTube.models import *
from .logic import AnalysisString

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

    def UpdateUphistory(self, id, newUp, operate): #�����ϴ���ʷ
        if len(CUser.objects.filter(id=id)) != 0:
            if operate == 'add':
                history = CUser.objects.get(id=id).uphistory
                history += str(newUp) + ' '
                CUser.objects.filter(id=id).update(uphistory=history)
            elif operate == 'delete':
                history = CUser.objects.get(id=id).uphistory
                uplist = AnalysisString(history)
                if newUp in uplist:
                    del uplist[uplist.index(newUp)]
                    newhistory = ' '.join(uplist) + ' '
                    CUser.objects.filter(id=id).update(uphistory=newhistory)


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
            return 0


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

    def UpdateComments(self, id, newComments, operate): #������Ƶ����
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

    def GetUnckeckVideo(self): #��ȡһ��δ�����Ƶ
        videos = CVideo.objects.order_by('id')
        for video in videos:
            if video.state == 0:
                return video.id;

    def GetUnckeckVideoNum(self): #��ȡδ�����Ƶ����
        videos = CVideo.objects.filter(state=0)
        return len(videos)


class IComment():
    def Insert(self, comment): #�½�����
        comment.save()

    def Delete(self, id): #ɾ������
        CComment.objects.filter(id=id).delete()

    def SelectById(self, id): #��idѡ������
        if len(CComment.objects.filter(id=id)) != 0:
            return CComment.objects.get(id=id)
        else:
            return None

    def ModifyUpper(self, id, newUpper): #�޸�������
        CComment.objects.filter(id=id).update(upper=newUpper)

    def ModifyTime(self, id, newTime): #�޸�����ʱ��
        CComment.objects.filter(id=id).update(time=newTime)

    def ModifyContent(self, id, newContent): #�޸���������
        CComment.objects.filter(id=id).update(content=newContent)

    def ModifyVideo(self, id, newVideo): #�޸�������Ƶ
        CComment.objects.filter(id=id).update(video=newVideo)

    def GetlastCommentId(self): #��ȡ���id
        if len(CComment.objects.order_by('-id')) != 0:
            return CComment.objects.order_by('-id')[0].id
        else:
            return 0


class IBulletscreen():
    def Insert(self, bscreen): #�½���Ļ
        bscreen.save()

    def Delete(self, id): #ɾ����Ļ
        CBulletsreen.objects.filter(id=id).delete()

    def SelectId(self, id): #��idѡ��Ļ
        if len(CBulletsreen.objects.filter(id=id)) != 0:
            return CBulletsreen.objects.get(id=id)
        else:
            return None

    def ModifyVideo(self, id, newVideo): #�޸�������Ƶ
        CBulletsreen.objects.filter(id=id).update(video=newVideo)

    def ModifyTime(self, id, newTime): #�޸ĵ�Ļʱ��
        CBulletsreen.objects.filter(id=id).update(time=newTime)

    def ModifyContent(self, id, newContent): #�޸ĵ�Ļ����
        CBulletsreen.objects.filter(id=id).update(content=newContent)

    def GetlastBsreenId(self): #��ȡ���id
        if len(CBulletsreen.objects.order_by('-id')) != 0:
            return CBulletsreen.objects.order_by('-id')[0].id
        else:
            return 0

class IType():
    def Insert(self, itype): #�½����
        itype.save()

    def Delete(self, id): #ɾ�����
        CType.objects.filter(id=id).delete()

    def SelectAllType(self): #��ȡ����б�
        typelist = []
        objlist = CType.objects.all()
        for obj in objlist:
            typelist.append(obj.content)
        return typelist

    def SelectById(self, id): #��id��ȡ���
        if len(CType.objects.filter(id=id)) != 0:
            return CType.objects.get(id=id)
        else:
            return None

    def ModifyContent(self, id, newContent): #�޸��������
        CType.objects.filter(id=id).update(content=newContent)

    def GetlastTypeId(self): #��ȡ���id
        if len(CType.objects.order_by('-id')) != 0:
            return CType.objects.order_by('-id')[0].id
        else:
            return 0


"""
user = CUser(
        id=3,
        name='test',
        password='',
        likenum=1,
        email='',
        uphistory='',
        image='',
        viewhistory='',
        follow='',
        followme='',
        admin='0',
    )

video = CVideo(
        id=2,
        title='asiaTube',
        discribe='a short movie',
        keyword='asia',
        type=1,
        upper=1,
        path='/no/',
        state=0,
        comments='',
        bsreen='',
        likenum=0,
        playnum=0,
        time = str(datetime.datetime.now())[0:19],
    )

comment = CComment(
        id = 2,
        upper = 1,
        time = str(datetime.datetime.now())[0:19],
        content = 'wo ding',
        video = 1,
    )

bsreen = CBulletsreen(
        id = 2,
        video = 1,
        time = str(datetime.datetime.now())[0:19],
        content = 'qian fang gao neng'
    )

ctype = CType(
        id = 2,
        content = 'news',
    )
"""