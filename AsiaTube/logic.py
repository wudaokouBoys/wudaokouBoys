# -*- coding=utf-8 -*-
from AsiaTube.interface import *

"""
    remain to do:
    Login
    AddComment
    AddBsreen
    UpVideo
    ModifyInfo
    SetSensitiveWord
    CalculateInfo
"""

def AnalysisString(string):  #解析字符串
    if string == None:
        return
    splitList = string.split(' ')
    if  len(splitList) != 0:
        splitList.pop()
    return splitList

def DeleteVideo(user_id, video_id): #删除上传视频
    iuser = IUser()
    iuser.UpdateUphistory(user_id, video_id, 'delete')
    ivideo = IVideo()
    video = ivideo.SelectById(video_id)
    commentList = AnalysisString(video.comments)
    bulletsreenList = AnalysisString(video.bsreen)
    icomment = IComment()
    ibsreen = IBulletscreen()
    for comment in commentList:
        icomment.Delete(comment)
    for bsreen in bulletsreenList:
        ibsreen.Delete(bsreen)
    ivideo.Delete(video_id)
    return True

def FollowUser(user_id, leaeder_id): #关注某人
    iuser = IUser()
    user = iuser.SelectById(user_id)
    list = AnalysisString(user.follow)
    if leaeder_id in list:
        return False
    else:
        iuser.UpdateFollow(user_id, leaeder_id)
        iuser.UpdateFollowme(leaeder_id, user_id)
        return True

def Likevideo(video_id): #点赞视频、用户
    ivideo = IVideo()
    video =  ivideo.SelectById(video_id)
    ivideo.AddLikenum(video_id)
    iuser = IUser()
    iuser.AddLikenum(video.upper)

def GetUpHistory(user_id): #获取用户上传历史
    iuser = IUser()
    user = iuser.SelectById(user_id)
    uphistoryList = AnalysisString(user.uphistory)
    return uphistoryList

def GetViewHistory(user_id): #获取用户观看历史
    iuser = IUser()
    user = iuser.SelectById(user_id)
    viewhistory = AnalysisString(user.viewhistory)
    return viewhistory

"""
    administrator operation
"""
def DeleteUser(operator_id, user_id): #删除用户
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        ivideo = IVideo()
        user = iuser.SelectById(user_id)
        videoList = AnalysisString(user.uphistory)
        for video in videoList:
            ivideo.Delete(video)
        iuser.Delete(user_id)
        return True

def SetAdmin(operator_id, user_id):  #设置管理员
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        iuser.ModifyAdmin(user_id, 1)
        return True

def CheckVideo(operator_id, video_id): #审核通过视频
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        ivideo = IVideo()
        ivideo.ModifyState(video_id, 1)
        return True

def AddType(operator_id, str_type): #添加类别
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        itype =IType()
        typeList = itype.SelectAllType()
        if str_type in typeList:
            return  False
        else:
            newType = CType(
                id=itype.GetlastTypeId()+1,
                content=str_type,
            )
            itype.Insert(newType)
            return True

def DeleteType(operator_id, type_id): #删除类别
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        itype = IType()
        itype.Delete(type_id)
        return True

def DeleteComment(operator_id, comment_id): #删除评论
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        icomment = IComment()
        icomment.Delete(comment_id)
        return True

"""
    video operation
"""

def GetComment(video_id):  #获取视频评论
    commentLib = []
    commentList = CComment.objects.filter(video=video_id)
    iuser = IUser()
    i = 1
    for comment in commentList:
        user = iuser.SelectById(comment.upper)
        content = {
            'id':comment.id,
            'image':user.image,
            'name':user.name,
            'layer':i,
            'content':comment.content,
            'time':comment.time,
        }
        i += 1
        commentLib.append(content)
    return commentLib

def GetBsreen(video_id):  #获取视频弹幕
    """bscreenLib = []
    ivideo = IVideo()
    video = ivideo.SelectById(video_id)
    bscreenList = AnalysisString(video.bsreen)
    ibsreen = IBulletscreen()
    for bsreen in bscreenList:
        content = ibsreen.SelectById(bsreen).content
        bscreenLib.append(content)"""
    bscreenLib = CBulletscreen.objects.filter(video=video_id)
    return bscreenLib