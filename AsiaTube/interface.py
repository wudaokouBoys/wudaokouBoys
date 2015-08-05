# -*- coding=utf-8 -*-
from AsiaTube.models import *
import operator

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

    def UpdateUphistory(self, id, newUp, operate): #更新上传历史
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


    def UpdateViewhistory(self, id, newView): #更新观看历史
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).viewhistory
            historyList = AnalysisString(history)
            if newView in historyList:
                history =str(newView) + ' ' + history.split(str(newView)+' ')[0]+history.split(str(newView)+' ')[1]
            else:
                history += str(newView) + ' '
            CUser.objects.filter(id=id).update(viewhistory=history)

    def UpdateFollow(self, id, leader): #更新关注列表
        if len(CUser.objects.filter(id=id)) != 0:
            leaders = CUser.objects.get(id=id).follow
            leaders += str(leader) + ' '
            CUser.objects.filter(id=id).update(follow=leaders)

    def UpdateFollowme(self, id, follower): #更新关注列表
        if len(CUser.objects.filter(id=id)) != 0:
            followers = CUser.objects.get(id=id).followme
            followers += str(follower) + ' '
            CUser.objects.filter(id=id).update(followme=followers)

    def GetlastUserId(self): #获取最大id
        if len(CUser.objects.order_by('-id')) != 0:
            return CUser.objects.order_by('-id')[0].id
        else:
            return 0


class IVideo():
    def Insert(self, video): #添加视频
        video.save()

    def Delete(self, id):  #删除视频
        CVideo.objects.filter(id=id).delete()

    def SelectById(self, id): #用id选择视频
        if len(CVideo.objects.filter(id=id)) != 0:
            return CVideo.objects.get(id=id)
        else:
            return None

    def Search(self, condition, content): #搜索视频
        if condition == 'type':
            videos = CVideo.objects.filter(state=1).filter(type=content).order_by('-playnum')
            searchList = []
            for video in videos:
                searchitem = {
                    'id':video.id,
                    'title':video.title,
                    'playnum':video.playnum,
                    'likenum':video.likenum,
                    'comment':len(CComment.objects.filter(video=video.id)),
                    'BScreen':len(CBulletscreen.objects.filter(video=video.id)),
                    'uptime':video.time,
                    'discription':video.discribe,
                    'type':CType.objects.filter(id=video.type)[0].content,
                    'image':str(video.id) + '_v.png',
                    'upper':CUser.objects.filter(id=video.upper)[0].name,
                }
                searchList.append(searchitem)
            return searchList
        elif condition == 'keyword':
            videos = CVideo.objects.filter(state=1)
            searchList = []
            for video in videos:
                string = video.title + video.discribe
                if string.find(content) > -1:
                    searchitem = {
                        'id':video.id,
                        'title':video.title,
                        'playnum':video.playnum,
                        'likenum':video.likenum,
                        'comment':len(CComment.objects.filter(video=video.id)),
                        'BScreen':len(CBulletscreen.objects.filter(video=video.id)),
                        'uptime':video.time,
                        'discription':video.discribe,
                        'type':CType.objects.filter(id=video.type)[0].content,
                        'image':str(video.id) + '_v.png',
                        'upper':CUser.objects.filter(id=video.upper)[0].name,
                    }
                    searchList.append(searchitem)
            searchList = sorted(searchList, key=operator.itemgetter('playnum'))
            searchList.reverse()
            return searchList

    def ModifyTitle(self, id, newTitle): #修改视频标题
        CVideo.objects.filter(id=id).update(title=newTitle)

    def ModifyDiscribe(self, id, newDis): #修改视频描述
        CVideo.objects.filter(id=id).update(discribe=newDis)

    def ModifyKeyword(self, id, newKeyword): #修改视频关键词
        CVideo.objects.filter(id=id).update(keyword=newKeyword)

    def ModifyType(self, id, newType): #修改视频类别
        CVideo.objects.filter(id=id).update(type=newType)

    def ModifyUpper(self, id, newUpper): #修改上传者
        CVideo.objects.filter(id=id).update(upper=newUpper)

    def ModifyTime(self, id, newTime): #修改上传时间
        CVideo.objects.filter(id=id).update(time=newTime)

    def ModifyPath(self, id, newPath): #修改视频保存路径
        CVideo.objects.filter(id=id).update(path=newPath)

    def ModifyState(self, id, newState): #修改视频审核状态
        CVideo.objects.filter(id=id).update(state=newState)

    def UpdateComments(self, id, newComments, operate): #更新视频评论
        if len(CVideo.objects.filter(id=id)) != 0:
            comment = CVideo.objects.get(id=id).comments
            comment += str(newComments) + ' '
            CVideo.objects.filter(id=id).update(comments=comment)

    def UpdateBsreen(self, id, newBsreen): #更新视频弹幕
        if len(CVideo.objects.filter(id=id)) != 0:
            bsreens = CVideo.objects.get(id=id).bsreen
            bsreens += str(newBsreen) + ' '
            CVideo.objects.filter(id=id).update(bsreen=bsreens)

    def AddLikenum(self, id): #增加视频赞数
        if len(CVideo.objects.filter(id=id)) != 0:
            num = CVideo.objects.get(id=id).likenum
            CVideo.objects.filter(id=id).update(likenum=num+1)

    def AddPlaynum(self, id): #增加视频播放数
        if len(CVideo.objects.filter(id=id)) != 0:
            num = CVideo.objects.get(id=id).playnum
            CVideo.objects.filter(id=id).update(playnum=num+1)

    def GetlastVideoId(self): #获取最大id
        if len(CVideo.objects.order_by('-id')) != 0:
            return CVideo.objects.order_by('-id')[0].id
        else:
            return 0

    def GetUnckeckVideo(self): #获取一个未审核视频
        videos = CVideo.objects.order_by('id')
        for video in videos:
            if video.state == 0:
                return video.id;
        return -1

    def GetUnckeckVideoNum(self): #获取未审核视频数量
        videos = CVideo.objects.filter(state=0)
        return len(videos)


class IComment():
    def Insert(self, comment): #新建评论
        comment.save()

    def Delete(self, id): #删除评论
        CComment.objects.filter(id=id).delete()

    def SelectById(self, id): #用id选择评论
        if len(CComment.objects.filter(id=id)) != 0:
            return CComment.objects.get(id=id)
        else:
            return None

    def ModifyUpper(self, id, newUpper): #修改评论者
        CComment.objects.filter(id=id).update(upper=newUpper)

    def ModifyTime(self, id, newTime): #修改评论时间
        CComment.objects.filter(id=id).update(time=newTime)

    def ModifyContent(self, id, newContent): #修改评论内容
        CComment.objects.filter(id=id).update(content=newContent)

    def ModifyVideo(self, id, newVideo): #修改所属视频
        CComment.objects.filter(id=id).update(video=newVideo)

    def GetlastCommentId(self): #获取最大id
        if len(CComment.objects.order_by('-id')) != 0:
            return CComment.objects.order_by('-id')[0].id
        else:
            return 0


class IBulletscreen():
    def Insert(self, bscreen): #新建弹幕
        bscreen.save()

    def Delete(self, id): #删除弹幕
        CBulletscreen.objects.filter(id=id).delete()

    def SelectId(self, id): #用id选择弹幕
        if len(CBulletscreen.objects.filter(id=id)) != 0:
            return CBulletscreen.objects.get(id=id)
        else:
            return None

    def ModifyVideo(self, id, newVideo): #修改所属视频
        CBulletscreen.objects.filter(id=id).update(video=newVideo)

    def ModifyTime(self, id, newTime): #修改弹幕时间
        CBulletscreen.objects.filter(id=id).update(time=newTime)

    def ModifyContent(self, id, newContent): #修改弹幕内容
        CBulletscreen.objects.filter(id=id).update(content=newContent)

    def GetlastBsreenId(self): #获取最大id
        if len(CBulletscreen.objects.order_by('-id')) != 0:
            return CBulletscreen.objects.order_by('-id')[0].id
        else:
            return 0

class IType():
    def Insert(self, itype): #新建类别
        itype.save()

    def Delete(self, id): #删除类别
        CType.objects.filter(id=id).delete()

    def SelectAllType(self): #获取类别列表
        """typelist = []
        objlist = CType.objects.all()
        for obj in objlist:
            typelist.append(obj.content)
        return typelist"""
        return CType.objects.all()

    def SelectById(self, id): #用id获取类别
        if len(CType.objects.filter(id=id)) != 0:
            return CType.objects.get(id=id)
        else:
            return None

    def ModifyContent(self, id, newContent): #修改类别内容
        CType.objects.filter(id=id).update(content=newContent)

    def GetlastTypeId(self): #获取最大id
        if len(CType.objects.order_by('-id')) != 0:
            return CType.objects.order_by('-id')[0].id
        else:
            return 0

def AnalysisString(string):  #split string into list
    if string == None:
        return
    splitList = string.split(' ')
    if  len(splitList) != 0:
        splitList.pop()
    return splitList

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

bsreen = CBulletscreen(
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