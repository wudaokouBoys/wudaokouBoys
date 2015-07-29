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

    def UpdateUphistory(self, id, newUp): #更新上传历史
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).uphistory
            history += str(newUp) + ' '
            CUser.objects.filter(id=id).update(uphistory=history)

    def UpdateViewhistory(self, id, newView): #更新观看历史
        if len(CUser.objects.filter(id=id)) != 0:
            history = CUser.objects.get(id=id).viewhistory
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
            return


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

    def Search(self, condition): #搜索视频
        return

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

    def UpdateComments(self, id, newComments): #更新视频评论
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


class IBulletscreen():
    def Insert(self, bscreen): #新建弹幕
        bscreen.save()

    def Delete(self, id): #删除弹幕
        CBulletsreen.objects.filter(id=id).delete()

    def SelectId(self, id): #用id选择弹幕
        if len(CBulletsreen.objects.filter(id=id)) != 0:
            return CBulletsreen.objects.get(id=id)
        else:
            return None

    def ModifyVideo(self, id, newVideo): #修改所属视频
        CBulletsreen.objects.filter(id=id).update(video=newVideo)

    def ModifyTime(self, id, newTime): #修改弹幕时间
        CBulletsreen.objects.filter(id=id).update(time=newTime)

    def ModifyContent(self, id, newContent): #修改弹幕内容
        CBulletsreen.objects.filter(id=id).update(content=newContent)

class IType():
    def Insert(self, itype): #新建类别
        itype.save()

    def Delete(self, id): #删除类别
        CType.objects.filter(id=id).delete()

    def SelectAllType(self): #获取类别列表
        typelist = []
        objlist = CType.objects.all()
        for obj in objlist:
            typelist.append(obj.content)
        return typelist

    def SelectById(self, id): #用id获取类别
        if len(CType.objects.filter(id=id)) != 0:
            return CType.objects.get(id=id)
        else:
            return None

    def ModifyContent(self, id, newContent): #修改类别内容
        CType.objects.filter(id=id).update(content=newContent)


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