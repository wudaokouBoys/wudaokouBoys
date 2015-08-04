from AsiaTube.interface import *
from AsiaTube.interface import *

def DeleteVideo(user_id, video_id): # delete video
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

def FollowUser(user_id, leaeder_id): #follow someone
    iuser = IUser()
    user = iuser.SelectById(user_id)
    list = AnalysisString(user.follow)
    if leaeder_id in list:
        return False
    else:
        iuser.UpdateFollow(user_id, leaeder_id)
        iuser.UpdateFollowme(leaeder_id, user_id)
        return True


def Likevideo(video_id): #like video
    ivideo = IVideo()
    video =  ivideo.SelectById(video_id)
    ivideo.AddLikenum(video_id)
    iuser = IUser()
    iuser.AddLikenum(video.upper)
    return

def GetUpHistory(user_id): #get user up video
    iuser = IUser()
    user = iuser.SelectById(user_id)
    uphistoryList = AnalysisString(user.uphistory)
    return uphistoryList

def GetViewHistory(user_id): #get user view history
    iuser = IUser()
    user = iuser.SelectById(user_id)
    viewhistory = AnalysisString(user.viewhistory)
    return viewhistory


#administrator operation

def DeleteUser(operator_id, user_id): #delete user
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

def SetAdmin(operator_id, user_id):  #set administrator
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        iuser.ModifyAdmin(user_id, 1)
        return True

def CheckVideo(operator_id, video_id): #check video
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        ivideo = IVideo()
        ivideo.ModifyState(video_id, 1)
        return True

def AddType(operator_id, str_type): #add type
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

def DeleteType(operator_id, type_id): #delete type
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        itype = IType()
        itype.Delete(type_id)
        return True



def DeleteComment(operator_id, comment_id): #delete comment
    iuser = IUser()
    operator = iuser.SelectById(operator_id)
    if operator.admin == 0:
        return False
    else:
        icomment = IComment()
        icomment.Delete(comment_id)
        return True


#video operation

def GetComment(video_id):  #get video's comment
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

def GetBsreen(video_id):  #get video's bulletscreen
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