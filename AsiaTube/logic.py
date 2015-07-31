from .interface import *
from .models import *

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

def AnalysisString(string):  #�����ַ���
    splitList = string.split(' ')
    if  len(splitList) != 0:
        splitList.pop()
    return splitList

def DeleteVideo(user_id, video_id): #ɾ���ϴ���Ƶ
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

def FollowUser(user_id, leaeder_id): #��עĳ��
    iuser = IUser()
    user = iuser.SelectById(user_id)
    list = AnalysisString(user.follow)
    if leaeder_id in list:
        return False
    else:
        iuser.UpdateFollow(user_id, leaeder_id)
        iuser.UpdateFollowme(leaeder_id, user_id)
        return True

def Likevideo(video_id): #������Ƶ���û�
    ivideo = IVideo()
    video =  ivideo.SelectById(video_id)
    ivideo.AddLikenum(video_id)
    iuser = IUser()
    iuser.AddLikenum(video.upper)

def GetUpHistory(user_id): #��ȡ�û��ϴ���ʷ
    iuser = IUser()
    user = iuser.SelectById(user_id)
    uphistoryList = AnalysisString(user.uphistory)
    return uphistoryList

def GetViewHistory(user_id): #��ȡ�û��ۿ���ʷ
    iuser = IUser()
    user = iuser.SelectById(user_id)
    viewhistory = AnalysisString(user.viewhistory)
    return viewhistory

"""
    administrator operation
"""
def DeleteUser(operator_id, user_id): #ɾ���û�
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        iuser.Delete(user_id)
        return True

def SetAdmin(operator_id, user_id):  #���ù���Ա
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        iuser.ModifyAdmin(user_id, 1)
        return True

def CheckVideo(operator_id, video_id): #���ͨ����Ƶ
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        ivideo = IVideo()
        ivideo.ModifyState(video_id, 1)
        return True

def AddType(operator_id, str_type): #������
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

def DeleteType(operator_id, type_id): #ɾ�����
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        itype = IType()
        itype.Delete(type_id)
        return True

def DeleteComment(operator_id, comment_id): #ɾ������
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

def GetComment(video_id):  #��ȡ��Ƶ����
    commentLib = []
    ivideo = IVideo()
    video = ivideo.SelectById(video_id)
    commentList = AnalysisString(video.comments)
    icomment = IComment()
    for comment in commentList:
        content = icomment.SelectById(comment).content
        commentLib.append(content)
    return commentLib

def GetBsreen(video_id):  #��ȡ��Ƶ��Ļ
    bscreenLib = []
    ivideo = IVideo()
    video = ivideo.SelectById(video_id)
    bscreenList = AnalysisString(video.bsreen)
    ibsreen = IBulletscreen()
    for bsreen in bscreenList:
        content = ibsreen.SelectById(bsreen).content
        bscreenLib.append(content)
    return bscreenLib