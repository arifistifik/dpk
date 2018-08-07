from ARIFISTIFIK import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n ---  WELCOME  ---\n")

cl = LINE()
#cl = LINE(authTokenDPK="EvBoSHd3NymRnF3lzZdb.0PzLwS72Fl1EGGJMnIN3IW.1U1vPtTqpd/BytwfeUSD95WRIubQG5rPQeunnLZ9/sk=")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = LINEChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("✍Ð₱₭ ฿Ø₮ LOGIN SUCCESS")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
LINE = LINEPoll(cl)
call = cl

Dpk = [cl]
mid = cl.profile.mid
DpkBot=[mid]
Owner=["ud296655acef67cbd5e8208e63629f78b"]
DpkFamily = DpkBot + Dpk + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Wait = {
    "UnsendPesan":False,
    "SpamInvite":False,
    "Contact":False,
    "GName":"ARIFISTIFIK",
    "AutoRespon":True,
    "MentionText":"dîh ηgëtåg äķü mülü... Kămư kë§ëÞîåη ¥åk...???",
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "limit": 5,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"KENAPA BARU SEKARANG KAMU ADD AKU? 😅",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":False,
    "AutojoinTicket":False,
    "AutoReject":True,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":False,
    "Welcome":False,
    "BackupBot":True,
    "WcText": "\nSELAMAT DATANG 😊😊😊\nYUK MULAI KENALAN MA YANG LAIN😅",
    "Leave":True,
    "LvText": "SAMPAI JUMPA LAGI KAWAN 😘",
    "Mic":False,
    "MicDel":False,
    "Adminadd":False,
    "AdminDel":False,
    "Gift":False,
    "readMember":{},
    "readPoint":{},
    "readTime":{},
    "ROM":{},
    "Blacklist":{},
    "Ban":False,
    "Unban":False,
    "Admin": {
        "ud296655acef67cbd5e8208e63629f78b":True #MID ADMIN
    },
}

Mozilla = {
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ],
    "mimic": {
        "copy": False,
        "conpp": False,
        "status": False,
        "target": {}
    }
}

setTime = {}
setTime = Wait['readTime']
mulai = time.time() 
msg_dict = {}

ProfileMe = {
    "displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
ProfileMe["displayName"] = clProfile.displayName
ProfileMe["statusMessage"] = clProfile.statusMessage
ProfileMe["pictureStatus"] = clProfile.pictureStatus

DpkCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""
╔═══════════════════
╠☬➣  MËÑÜ ĦÉĹP  ☬➣  ⏩⏩
╠═══════════════════
╠☬➣me      🇮🇩                     🇮🇩
╠☬➣my name          🇮🇩
╠☬➣my bio        🇮🇩
╠☬➣my picture                    🇮🇩
╠☬➣my cover      🇮🇩
╠☬➣my video                 🇮🇩
╠☬➣speed        🇮🇩
╠☬➣rename              🇮🇩
╠☬➣my bot                          🇮🇩
╠☬➣my team   🇮🇩
╠☬➣stealname [@]        🇮🇩
╠☬➣stealbio [@]  🇮🇩
╠☬➣stealpict [@]                 🇮🇩
╠☬➣stealcover [@]🇮🇩
╠☬➣stealvideo [@]          🇮🇩
╠☬➣stealmid [@]🇮🇩
╠☬➣profile [@]                      🇮🇩
╠☬➣cekmid: [mid]    🇮🇩
╠☬➣banlock [@] 🇮🇩
╠☬➣banlist                        🇮🇩
╠☬➣contact ban 🇮🇩
╠☬➣clear ban              🇮🇩
╠☬➣blocklist    🇮🇩
╠☬➣friendlist                      🇮🇩
╠☬➣friendlist mid   🇮🇩
╠☬➣runtime      🇮🇩
╠☬➣broadcast:                🇮🇩
╠☬➣contactbc:       🇮🇩
╠☬➣adminadd [@]              🇮🇩
╠☬➣admindel [@]      🇮🇩
╠☬➣changename:🇮🇩
╠☬➣changebio:                   🇮🇩
╠☬➣remove pesan 🇮🇩
╠☬➣restart                     🇮🇩
╠☬➣bot logout 🇮🇩
╠☬➣kick [@]                        🇮🇩
╠☬➣status    🇮🇩
╠☬➣clone [@]                     🇮🇩
╠☬➣comeback🇮🇩
╠☬➣mimiclist   🇮🇩
╠☬➣refresh                        🇮🇩
╠☬➣leaveall grup              🇮🇩
╠☬➣rejectall grup   🇮🇩
╠☬➣lurking read           🇮🇩
╠☬➣mentionall    🇮🇩
╠☬➣changewelcome:
╠☬➣changeleave:
╠☬➣memberlist                🇮🇩
╠☬➣my grup    🇮🇩
╠☬➣gcall              
╠☬➣gurl                🇮🇩
╠☬➣gcreator    🇮🇩
╠☬➣invite gcreator    🇮🇩
╠☬➣ginfo    🇮🇩
╠☬➣grup id                🇮🇩
╠☬➣announce    🇮🇩
╠═══════════════════
╠☬➣  ✍Ð₱₭ ฿Ø₮₰ ⃟🇮🇩􏿿 ☬➣   ⏩
╚═══════════════════
"""""

Helpbot ="""
╔═══════════════════
╠☬➣  ĦÉĹP  BŐŤŞ°☬➣ ⏩⏩
╠═══════════════════
╠☬➣spam on [jmlah teks]
╠☬➣admin:add-on             🇮🇩
╠☬➣admin:del-on      🇮🇩
╠☬➣unsend [on/off]    🇮🇩
╠☬➣changepp [on/off]
╠☬➣timeline [on/off]         🇮🇩
╠☬➣autojoin [on/off]
╠☬➣autoreject [on/off]
╠☬➣auto jointicket [on/off]
╠☬➣gift:[on/off]                🇮🇩
╠☬➣copy [on/off] 🇮🇩
╠☬➣steal [on/off]        🇮🇩
╠☬➣contact [on/off]         🇮🇩
╠☬➣mic:add-on  🇮🇩
╠☬➣mic:del-on            🇮🇩
╠☬➣mimic [on/off]            🇮🇩
╠☬➣kick [on,off->kickall]   🇮🇩
╠☬➣invite on/off     🇮🇩
╠☬➣kill [on/off]               🇮🇩
╠☬➣lurking [on/off/reset]
╠☬➣sider [on/off]    🇮🇩
╠☬➣welcome [on/off]    🇮🇩
╠☬➣leave [on/off]    🇮🇩
╠☬➣link [on/off]    🇮🇩
╠☬➣cfotogrup [on/off]
╠☬➣spaminvite [on/off]    🇮🇩
╠═══════════════════
╠☬➣  ✍Ð₱₭ ฿Ø₮₰ ⃟🇮🇩􏿿 ☬➣  ⏩
╚═══════════════════
"""""

Helpmedia ="""
╔═══════════════════
╠☬➣  MËÑÜ M€ÐĪÄ  ☬➣⏩⏩
╠═══════════════════
╠☬➣ topnews
╠☬➣ data birth:
╠☬➣ urban:
╠☬➣ sslink:
╠☬➣ maps:
╠☬➣ cekcuaca:
╠☬➣ jadwalshalat:
╠☬➣ idline:
╠☬➣ say-id:
╠☬➣ say-en:
╠☬➣ say-jp:
╠☬➣ say-ar:
╠☬➣ say-ko:
╠☬➣ apakah:
╠☬➣ kapan:
╠☬➣ wikipedia:
╠☬➣ kalender
╠☬➣ image:
╠☬➣ youtube:
╠☬➣ indonesian:
╠☬➣ english:
╠☬➣ korea:
╠☬➣ japan:
╠☬➣ thailand:
╠☬➣ arab:
╠☬➣ malaysia:
╠☬➣ jawa:
╠═══════════════════
╠☬➣  ✍Ð₱₭ ฿Ø₮₰ ⃟🇮🇩􏿿 ☬➣   ⏩
╚═══════════════════
"""""

#------------------------------------------------ SCRIP DEF ----------------------------------------------------------#

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    year, month = divmod(month,12)
    century, year = divmod(year,100)
    return '\n%02d Abad\n%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik' % (century, year, month, days, hours, mins, secs)

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def LINE_ARIF_USER(arif):
    try:
        if arif.type == 0:
            return
        if arif.type == 13:
            if mid in arif.param3:
              if Wait['autoJoin'] == True:
                    cl.acceptGroupInvitation(arif.param1)
                    print ("ANDA JOIN DI GRUP")
                    pass

        if arif.type == 13:
            if mid in arif.param3:
              if Wait['AutoReject'] == True:
                if arif.param2 not in DpkFamily and arif.param2 not in Wait["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        elif arif.type == 55:
            try:
                if DpkCctv['Point1'][arif.param1]==True:
                    if arif.param1 in DpkCctv['Point2']:  
                        Name = cl.getContact(arif.param2).displayName
                        if Name in DpkCctv['Point3'][arif.param1]:
                            pass
                        else:
                            DpkCctv['Point3'][arif.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithDPK(arif.param1,arif.param2," Hii\n","" + "\n Nyimak yah kak?" )
                                else:
                                    cl.mentionWithDPK(arif.param1,arif.param2," Nah\n","" + "\n Nongol Sini Chat kak ??" )
                            else:
                                cl.mentionWithDPK(arif.param1,arif.param2," Hey\n","" + "\n What Are You Doing?" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if arif.type == 55:
            try:
                if arif.param1 in Wait['readPoint']:
                    if arif.param2 in Wait['readMember'][arif.param1]:
                        pass
                    else:
                        Wait['readMember'][arif.param1] += arif.param2
                    Wait['ROM'][arif.param1][arif.param2] = arif.param2
                else:
                   pass
            except:
                pass   

        if arif.type == 17:
            if Wait["Welcome"] == True:
                if arif.param2 not in Dpk:
                    ginfo = cl.getGroup(arif.param1)
                    cl.mentionWithDPK(arif.param1,arif.param2," Hii","" + "\n " + str(Wait['WcText']))
                    cl.sendMessage(arif.param1, None, contentMetadata={'mid':arif.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if arif.type == 15:
            if Wait["Leave"] == True:
                if arif.param2 not in Dpk:
                    ginfo = cl.getGroup(arif.param1)
                    cl.mentionWithDPK(arif.param1,arif.param2," Hii","" + "\n " + str(Wait['LvText']))
                    cl.sendMessage(arif.param1, None, contentMetadata={'mid':arif.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

        if arif.type == 46:
            if arif.param2 in DpkBot:
                cl.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if arif.type == 26:
            msg = arif.message
            text = msg.text
            dpkText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Wait["autoRead"] == True:
                        cl.sendChatChecked(kirim, msg_id)
                    if kirim in Wait["readPoint"]:
                        if user not in Wait["ROM"][kirim]:
                            Wait["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Wait["UnsendPesan"] == True:
                        msg = arif.message
                        if msg.toType == 0:
                            cl.log(" {} - {} ".format(str(user), str(dpkText)))
                        else:
                            cl.log(" {} - {} ".format(str(kirim), str(dpkText)))
                            msg_dict[msg.id] = {"rider": dpkText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Wait["Timeline"] == True:
                      if msg.contentType == 16:
                          ret_ = "[ INFORMASI TIMELINE ]\n"
                          if msg.contentMetadata["serviceType"] == "GB":
                              contact = cl.getContact(user).displayName
                              auth = "\nPenulis : {}".format(str(contact.displayName))
                          else:
                              auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                              ret_ += auth
                          if "stickerId" in msg.contentMetadata:
                              stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                              ret_ += stck
                          if "mediaOid" in msg.contentMetadata:
                              object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                              if msg.contentMetadata["mediaType"] == "V":
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                      murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                  ret_ += murl
                              else:
                                  if msg.contentMetadata["serviceType"] == "GB":
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  else:
                                      ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                              ret_ += ourl
                          if "text" in msg.contentMetadata:
                              dia = cl.getContact(user)
                              zx = ""
                              zxc = ""
                              zx2 = []
                              xpesan = 'Pengirim: '
                              arifqu = str(dia.displayName)
                              pesan = ''
                              pesan2 = pesan+"@A_DPK\n"
                              xlen = str(len(zxc)+len(xpesan))
                              xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                              zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                              zx2.append(zx)
                              kata = "\n\nText Type : {}".format(str(msg.contentMetadata["text"]))
                              purl = "\n\nLink Post : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                              ret_ += purl
                              ret_ += kata
                              zxc += pesan2
                              pesan = xpesan + zxc + ret_ + ""
                              cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                              url = msg.contentMetadata["postEndUrl"]
                              cl.likePost(url[25:58], url[66:], likeType=1001)

        if arif.type == 65:
          if Wait['UnsendPesan'] == True:
              try:
                  you = arif.param1
                  msg.id = arif.param2
                  user = msg._from
                  if msg.id in msg_dict:
                    if msg_dict[msg.id]["pelaku"]:
                        pelaku = cl.getContact(msg_dict[msg.id]["pelaku"])
                        nama = pelaku.displayName
                        dia = "Detect Pesan Terhapus\n"
                        dia += "\n1. Name : " + nama
                        dia += "\n2. Taken : {}".format(str(msg_dict[msg.id]["createdTime"]))
                        dia += "\n3. Pesannya : {}".format(str(msg_dict[msg.id]["rider"]))
                        cl.mentionWithDPK(you,user," Nah","\n\n" +str(dia))
              except:
                  cl.sendMessage(you, "Return")

        if arif.type in [25,26]:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 7:
                if Wait['IDSticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "STICKER CHECKS\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n\nTHIS IS LINK\n\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.mentionWithDPK(kirim,user,"My Code Sticker\n","" + "\n\n" + str(filler))
                else:
                    pass

        if arif.type == 25:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Wait['Upfoto'] == True:
                if user in Owner:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateProfilePicture(path)
                    cl.mentionWithDPK(kirim,user," Update Picture Success ","")
                    Wait['Upfoto'] = False

        if arif.type == 25:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Wait['UpfotoGroup'] == True:
                if user in DpkFamily or user in Wait["Admin"]:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateGroupPicture(kirim, path)
                    cl.mentionWithDPK(kirim,user," Update Picture Grup Success ","")
                    Wait['UpfotoGroup'] = False

        if arif.type == 5:
            if Wait["autoAdd"] == True:
                if (Wait["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Wait["ContactAdd"][arif.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(arif.param1, "Haii {} " + str(Wait["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(arif.param1, None, contentMetadata={'mid':mid}, contentType=13)

        if arif.type == 5:
            if Wait['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(arif.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, arif.param1)
                    Wait["Blacklist"][arif.param2] = True
                except Exception as e:
                	print (e)

        if arif.type in [25,26]:
          if Wait['Contact'] == True:
              msg = arif.message
              user = msg._from
              kirim = msg.to
              if msg.contentType == 13:
                if 'displayName' in msg.contentMetadata:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendMessage(kirim,"Nama:\n" + msg.contentMetadata["displayName"] + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))
                else:
                    contact = cl.getContact(msg.contentMetadata["mid"])
                    try:
                        cover = cl.getProfileCoverURL(user)
                    except:
                        cover = ""
                    cl.sendText(kirim,"Nama:\n" + contact.displayName + "\n\nMid:\n" + msg.contentMetadata["mid"] + "\n\nBio:\n" + contact.statusMessage + "\n\nPicture URL\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\nCover URL:\n" + str(cover))

        if arif.type == 25:
          if Wait['Invite'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(kirim, _name + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.inviteIntoGroup(kirim,[target])
                                cl.sendText(kirim,"Invite " + _name + "\nSUCCESS..")
                                Wait['Invite'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Wait['Invite'] = False
                                 break

        if arif.type == 25:
          if Wait['Steal'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cl.sendText(kirim,"Nama :\n" + msg.contentMetadata["displayName"] + "\n\nBio :\n" + contact.statusMessage+ "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nSteal Succes..")
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                cl.sendImageWithURL(kirim,image)
                                cover = cl.getProfileCoverURL(target)
                                cl.sendImageWithURL(kirim, cover)
                                Wait['Steal'] = False
                                break                     
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Wait['Steal'] = False
                                 break

        if arif.type == 25:
          if Wait['KillOn'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Kick Via Contact")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            if target not in DpkFamily:
                                try:
                                    cl.kickoutFromGroup(kirim,[target])
                                    Wait['KillOn'] = False
                                    break
                                except:             
                                     cl.sendText(kirim, 'Target Not Found')
                                     Wait['KillOn'] = False
                                     break

        if arif.type == 25:
          if Wait['Gift'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Send Gift")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Wait['Gift'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Target Error')
                                 Wait['Gift'] = False
                                 break

        if arif.type == 25:
          if Wait["Mic"] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                Mozilla["mimic"]["target"][target] = True
                                cl.sendText(kirim,"Target ditambahkan!")
                                Squas['Mic'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if arif.type == 25:
          if Wait["MicDel"] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Mimic Add")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                del Mozilla["mimic"]["target"][target]
                                cl.sendText(kirim,"Target is Dellete!")
                                Wait['MicDel'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Silahkan untuk on kan kembali & Send Contact Again\nKami akan memuat ulang program')
                                 break

        if arif.type == 25:
          if Wait['Copy'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print ("[Target] Stealed")
                            break             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.cloneContactProfile(target)
                                cl.sendText(kirim, "Copy Contact Success")
                                Wait['Copy'] = False
                                break
                            except:             
                                 cl.sendText(kirim, "Contact Error")
                                 Wait['Copy'] = False
                                 break
                                 
                                 
#======= AUTO TAG & CHAT BATAS SCRIP ========
        if arif.type == 26:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Wait['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Wait['MentionText'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithDPK(kirim,user,"","" +str(ret_))
                                  cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                  break

        if arif.type == 26:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in DpkFamily or user not in Wait["Admin"]:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Wait['KickRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "Dont Tag Me","Sorry Dont Tag Me"]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithDPK(kirim,user,"","" +str(ret_))
                                  cl.kickoutFromGroup(kirim,[user])
                                  break

        if arif.type == 25:
          if Wait['SpamInvite'] == True:
            msg = arif.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DpkFamily or user in Wait["Admin"]:
                    korban = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for x in groups.members:
                        if korban in x.displayName:
                            cl.sendText(kirim, korban + " Sudah Berada DiGrup Ini")
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                cl.findAndAddContactsByMid(target)
                                cl.createGroup("LINE SPAM GROUP",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cl.createGroup("LINE SPAM GROUP",[target]) # HANYA SPAM VIA CONTACT
                                cl.createGroup("LINE SPAM GROUP",[target])
                                cl.sendText(kirim,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Wait['SpamInvite'] = False
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Wait['SpamInvite'] = False
                                 break


#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if arif.type == 25 or arif.type == 26:
            msg = arif.message
            text = msg.text
            dpkText = msg.text
            msg_id = msg.id
            kirim = msg.to           
            user = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = kirim
                elif msg.toType == 2:
                    to = kirim
                if msg.contentType == 0:
                    if Wait["autoRead"] == True:
                        cl.sendChatChecked(0, msg_id)
                    elif dpkText is None:
                        return
                    else:               
                        if dpkText.lower() == '_PYTHON3_':
                            cl.sendMessage(0, user)

                        elif dpkText.lower() == "me":
                            if user in DpkFamily or user in Wait["Admin"]:
                                cl.sendMessage(kirim, None, contentMetadata={'mid': user}, contentType=13)
                                cl.mentionWithDPK(kirim,user," Hay","")

                        elif dpkText.lower() == "help":
                            if user in DpkFamily or user in Wait["Admin"]:
                                 cl.sendMessage(kirim, str(Help))

                        elif dpkText.lower() == "help bot":
                            if user in DpkFamily or user in Wait["Admin"]:
                                 cl.sendMessage(kirim, str(Helpbot))

                        elif dpkText.lower() == "help media":
                            if user in DpkFamily or user in Wait["Admin"]:
                                 cl.sendMessage(kirim, str(Helpmedia))

                        elif dpkText.lower() == "speed":
                            if user in DpkFamily or user in Wait["Admin"]:
                                no = time.time()
                                cl.sendText("u65224f4e8812136f01b25275a54b5aef", ' ')
                                elapsed_time = time.time() - no
                                cl.sendText(kirim, "%s" % (elapsed_time))

                        elif dpkText.lower() == "rename":
                            if user in DpkFamily or user in Wait["Admin"]:
                                team1 = cl.getContact(mid).displayName
                                cl.mentionWithDPK(kirim,mid," Ready On ","" + str(" ("+team1+")"))

                        elif dpkText.lower() == "my team":
                            if user in DpkFamily or user in Wait["Admin"]:
                                dpk = ""
                                family = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    dpk += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Wait["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    family += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"DPK FAMILY\n\nOwner:\n"+dpk+"\nAdmin:\n"+family+"\n( %s ) TEAM FAMILY" %(str(len(Owner)+len(Wait["Admin"]))))                                

                        elif dpkText.lower() == "leaveall grup":
                            if user in DpkFamily or user in Wait["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif dpkText in ["Kick on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["KickOn"] = True
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':1}")
                        elif dpkText in ["Kick off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["KickOn"] = False
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':0}")

                        elif "Kickall" in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                              if msg.toType == 2:
                                if Wait["KickOn"]:
                                    _name = msg.text.replace("Kickall","")
                                    gs = cl.getGroup(kirim)
                                    targets = []
                                    for g in gs.members:
                                        if _name in g.displayName:
                                            targets.append(g.mid)
                                    if targets == []:
                                        cl.sendText(kirim,"Target Not found.")
                                    else:
                                        for target in targets:
                                          if target not in DpkFamily and target not in Wait["Admin"]:
                                            try:
                                                klist=[cl]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                            except Exception as error:
                                                cl.sendText(kirim, str(error))

                        elif dpkText.lower().startswith("spam "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                txt = dpkText.split(" ")
                                jmlh = int(txt[2])
                                teks = dpkText.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                                tulisan = jmlh * (teks+"\n")
                                if txt[1] == "on":
                                    if jmlh <= 500:
                                       for x in range(jmlh):
                                           cl.sendText(kirim, teks)
                                    else:
                                       cl.sendText(kirim, "Maksimal 500 SpamTeks!")
                                elif txt[1] == "off":
                                    if jmlh <= 500:
                                        cl.sendText(kirim, tulisan)
                                    else:
                                        cl.sendText(kirim, "Maksimal 500 SpamTeks!")

                        elif "Gcall" in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                              if msg.toType == 2:
                                    group = cl.getGroup(to)
                                    members = [mem.mid for mem in group.members]
                                    call.acquireGroupCallRoute(to)
                                    call.inviteIntoGroupCall(to, contactIds=members)
                                    jmlh = int(Wait["limit"])
                                    cl.sendText(to, "Success melakukan panggilan group")
                                    if jmlh <= 1000:
                                      for x in range(jmlh):
                                         try:
                                            call.acquireGroupCallRoute(to)
                                            call.inviteIntoGroupCall(to, contactIds=members)
                                         except Exception as e:
                                            cl.sendMessage(msg.to,str(e))
                                    else:
                                    	cl.sendMessage(msg.to,"Jumlah melebihi batas")
                            	
                        elif dpkText.lower().startswith("cekmid: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                arifqu = dpkText.replace("Cekmid: ","")
                                cl.sendMessage(kirim, None, contentMetadata={'mid': arifqu}, contentType=13)
                                contact = cl.getContact(arifqu)
                                ganteng = cl.getProfileCoverURL(arifqu)
                                path = str(ganteng)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendText(kirim,"Profile Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendText(kirim,"Cover Picture " + contact.displayName)
                                    cl.sendImageWithURL(kirim,path)
                                except:
                                    pass

                        elif ("Banlock " in dpkText):
                            if user in DpkFamily or user in Wait["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        Wait["Blacklist"][target] = True
                                        cl.sendText(kirim,"Succes Banned ")
                                    except:
                                        pass

                        elif dpkText.lower() == "banlist":
                            if user in DpkFamily or user in Wait["Admin"]:
                                if Wait["Blacklist"] == {}:
                                    cl.sendText(kirim,"Tidak ada yang masuk dalam daftar orang bejat bos😁")
                                else:
                                    mc = "Daftar Blacklist "
                                    num=1
                                    ragets = cl.getContacts(Wait["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n Total %i Masuk dalam katekori Orang Bejat!!! " % len(ragets)
                                    cl.sendText(kirim, mc)

                        elif dpkText.lower().startswith("contact ban"):
                            if user in DpkFamily or user in Wait["Admin"]:
                              if Wait["Blacklist"] == {}:
                                  cl.sendText(kirim,"Tidak ada yang masuk dalam daftar orang bejat bos😁")
                              else:
                                  cl.sendText(kirim,"Contact Blacklist")
                                  h = ""
                                  for i in Wait["Blacklist"]:
                                      h = cl.getContact(i)
                                      cl.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif dpkText.lower().startswith("clear ban"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Blacklist"] = {}
                                cl.sendText(kirim,"ORANG BEJAT SUDAH DIMAAFKAN😁")
                                print ("Clear Ban")

                        elif dpkText.lower() == 'link on':
                            if user in DpkFamily or user in Wait["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif dpkText.lower() == 'link off':
                            if user in DpkFamily or user in Wait["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif dpkText.lower() == 'gurl':
                          if user in DpkFamily or user in Wait["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cl.reissueGroupTicket(kirim)
                                    cl.sendMessage(kirim, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif dpkText.lower() == 'gcreator':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithDPK(kirim,GS,"Group Creator","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithDPK(kirim,W,"Group Creator","")

                        elif "invite gcreator" == dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    group = cl.getGroup(kirim)
                                    GS = group.creator.mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': GS}, contentType=13)
                                    cl.mentionWithDPK(kirim,GS,"Group Creator","")
                                    cl.findAndAddContactsByMid(GS)
                                    cl.inviteIntoGroup(kirim,[GS])
                                    cl.mentionWithDPK(kirim,user,"Invite Done","")
                                    contact = cl.getContact(GS.mid)
                                except:
                                    W = group.members[0].mid
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': W}, contentType=13)
                                    cl.mentionWithDPK(kirim,W,"Group Creator","")
                                    cl.findAndAddContactsByMid(W)
                                    cl.inviteIntoGroup(kirim,[W])
                                    cl.mentionWithDPK(kirim,user,"Invite Done","")

                        elif dpkText.lower() == 'ginfo':
                            if user in DpkFamily or user in Wait["Admin"]:
                                group = cl.getGroup(kirim)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(line.reissueGroupTicket(group.id)))
                                cuki = "INFO GRUP"
                                cuki += "\nNama Group : {}".format(str(group.name))
                                cuki += "\nID Group :\n? {}".format(group.id)
                                cuki += "\nPembuat : {}".format(str(gCreator))
                                cuki += "\nJumlah Member : {}".format(str(len(group.members)))
                                cuki += "\nJumlah Pending : {}".format(gPending)
                                cuki += "\nGroup Qr : {}".format(gQr)
                                cuki += "\nGroup Ticket : {}".format(gTicket)
                                cl.sendMessage(kirim, str(cuki))

                        elif dpkText in ["Memberlist"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                kontak = cl.getGroup(kirim)
                                group = kontak.members
                                num=1
                                msgs="LIST MEMBER\n"
                                for ids in group:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTOTAL MEMBER ( %i )" % len(group)
                                cl.sendText(kirim, msgs)

                        elif dpkText in ["Blocklist"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                blockedlist = cl.getBlockedContactIds()
                                kontak = cl.getContacts(blockedlist)
                                num=1
                                msgs="My Blocked\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.displayName)
                                    num=(num+1)
                                msgs+="\n\nTotal Blocked : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif dpkText in ["Friendlist mid"]: 
                            if user in DpkFamily or user in Wait["Admin"]:
                                gruplist = cl.getAllContactIds()
                                kontak = cl.getContacts(gruplist)
                                num=1
                                msgs="List Mid Friend\n"
                                for ids in kontak:
                                    msgs+="\n%i. %s" % (num, ids.mid)
                                    num=(num+1)
                                msgs+="\n\nTotal Mid Friend : %i" % len(kontak)
                                cl.sendText(kirim, msgs)

                        elif "Grup id" in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                saya = dpkText.replace('Grup id','')
                                gid = cl.getGroup(kirim)
                                cl.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif dpkText.lower() == 'lurking on':
                            if user in DpkFamily or user in Wait["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Wait['readPoint']:
                                        try:
                                            del Wait['readPoint'][kirim]
                                            del Wait['readMember'][kirim]
                                            del Wait['readTime'][kirim]
                                        except:
                                            pass
                                        Wait['readPoint'][kirim] = msg.id
                                        Wait['readMember'][kirim] = ""
                                        Wait['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                        Wait['ROM'][kirim] = {}
                                        with open('sider.json', 'w') as fp:
                                            json.dump(Wait, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(kirim,"Lurking already on")
                                else:
                                    try:
                                        del read['readPoint'][kirim]
                                        del read['readMember'][kirim]
                                        del read['readTime'][kirim]
                                    except:
                                        pass
                                    Wait['readPoint'][kirim] = msg.id
                                    Wait['readMember'][kirim] = ""
                                    Wait['readTime'][kirim] = datetime.now().strftime('%H:%M:%S')
                                    Wait['ROM'][kirim] = {}
                                    with open('sider.json', 'w') as fp:
                                        json.dump(Wait, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(kirim, "Set reading point:\n" + readTime)
                                        
                        elif dpkText.lower() == 'lurking off':
                            if user in DpkFamily or user in Wait["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim not in Wait['readPoint']:
                                    cl.sendMessage(kirim,"Lurking already off..")
                                else:
                                    try:
                                            del Wait['readPoint'][kirim]
                                            del Wait['readMember'][kirim]
                                            del Wait['readTime'][kirim]
                                    except:
                                          pass
                                    cl.sendMessage(kirim, "Delete reading point:\n" + readTime)
                
                        elif dpkText.lower() == 'lurking reset':
                            if user in DpkFamily or user in Wait["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Wait["readPoint"]:
                                    try:
                                        Wait["readPoint"][kirim] = True
                                        Wait["readMember"][kirim] = {}
                                        Wait["readTime"][kirim] = readTime
                                        Wait["ROM"][kirim] = {}
                                    except:
                                        pass
                                    cl.sendMessage(kirim, "Reset reading point:\n" + readTime)
                                else:
                                    cl.sendMessage(kirim, "Lurking on dulu kaka..")
                                    
                        elif dpkText.lower() == 'lurking read':
                            if user in DpkFamily or user in Wait["Admin"]:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if kirim in Wait['readPoint']:
                                    if Wait["ROM"][kirim].items() == []:
                                        cl.sendMessage(kirim,"[ Reader ]:\nNone")
                                    else:
                                        chiya = []
                                        for rom in Wait["ROM"][kirim].items():
                                            chiya.append(rom[1])
                                        cmem = cl.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = 'Pembaca Pesan:\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@A_DPK\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\nLurking time: \n" + readTime
                                    try:
                                        cl.sendMessage(kirim, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    cl.sendMessage(kirim,"Lurking on dulu kaka ??")

                        elif dpkText.lower() == 'sider on':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    del DpkCctv['Point2'][kirim]
                                    del DpkCctv['Point3'][kirim]
                                    del DpkCctv['Point1'][kirim]
                                except:
                                    pass
                                DpkCctv['Point2'][kirim] = msg.id
                                DpkCctv['Point3'][kirim] = ""
                                DpkCctv['Point1'][kirim]=True
                                cl.sendText(kirim,"Sider Set to On..")

                        elif dpkText.lower() == 'sider off':
                            if user in DpkFamily or user in Wait["Admin"]:
                                if kirim in DpkCctv['Point2']:
                                    DpkCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, DpkCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "Off not Going")

                        elif dpkText.lower().startswith("mentionall"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                gname = cl.getGroup(kirim)
                                local = [contact.mid for contact in gname.members]
                                try:
                                    lur = len(local)//20
                                    for fu in range(lur+1):
                                        hdc = u''
                                        sell=0
                                        com=[]
                                        for rid in gname.members[fu*20 : (fu+1)*20]:
                                            com.append({"S":str(sell), "E" :str(sell+6), "M":rid.mid})
                                            sell += 7
                                            hdc += u'@A_DPK\n'
                                            atas = '\n Halo {} '.format(str(gname.name))
                                            atas += '\n Halo {} Family'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif dpkText in ["Welcome on"]:
                          if user in DpkFamily or user in Wait["Admin"]:
                            if user in DpkFamily:
                                Wait['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif dpkText in ["Welcome off"]:
                          if user in DpkFamily or user in Wait["Admin"]:
                            if user in DpkFamily:
                                Wait['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif dpkText.lower().startswith("changewelcome "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                teks = dpkText.split(": ")
                                data = dpkText.replace(teks[0] + ": ","")
                                try:
                                    Wait["WcText"] = data
                                    cl.sendText(kirim,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif dpkText in ["Leave on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif dpkText in ["Leave off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif dpkText.lower().startswith("changeleave "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                teks = dpkText.split(": ")
                                data = dpkText.replace(teks[0] + ": ","")
                                try:
                                    Wait["LvText"] = data
                                    cl.sendText(kirim,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif dpkText.lower() == "runtime":
                            if user in DpkFamily or user in Wait["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Connect to DPK FAMILY\nBot Active\n" + opn)                

                        elif dpkText.lower().startswith("broadcast: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                bc = msg.text.replace("Broadcast: ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    cl.mentionWithDPK(i,user," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif dpkText.lower().startswith("contactbc: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                bc = msg.text.replace("Contactbc: ","")
                                gid = cl.getAllContactIds()
                                for i in gid:
                                    cl.mentionWithDPK(i,user," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif dpkText.lower().startswith("adminadd "):
                            if user in DpkFamily:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Wait["Admin"]:
                                        cl.sendText(kirim, "Sudah Terdaftar di Admin")
                                    else:
                                        try:
                                            Wait["Admin"][target] = True
                                            cl.sendText(kirim, "Terdaftar Menjadi Admin ")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif dpkText.lower().startswith("admindell "):
                            if user in Owner:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target not in Wait["Admin"]:
                                        cl.sendText(kirim, "Belum Terdaftar di Admin")
                                    else:
                                        try:
                                            del Wait["Admin"][target]
                                            cl.sendText(kirim, "Succes Dihapus menjadi admin")
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif dpkText.lower().startswith("changename: "):
                            if user in DpkFamily:
                                name = dpkText.split(": ")
                                change = dpkText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll.displayName = change
                                cl.updateProfile(cll)
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                cl.mentionWithDPK(kirim,owner," Update Name Success","\n Change to " + str(change))

                        elif dpkText.lower().startswith("changebio: "):
                            if user in DpkFamily:
                                proses = dpkText.split(": ")
                                teks = dpkText.replace(proses[0] + ": ","")
                                no1 = cl.getProfile()
                                no1.statusMessage = teks
                                cl.updateProfile(no1)
                                cl.sendText(kirim,"My Bio Change To : " + teks)

                        elif dpkText.lower() == "remove pesan":
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    cl.removeAllMessages(arif.param2)
                                    ginfo = cl.getGroup(kirim)
                                    cl.mentionWithDPK(kirim,user," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif dpkText.lower() == 'restart':
                            if user in DpkFamily:
                                cl.sendText(kirim, 'Restarting Server Prosses..')
                                print ("Restarting Server")
                                restart_program()

                        elif dpkText.lower() == 'bot logout':
                            if user in DpkFamily:
                                cl.mentionWithDPK(kirim,user," Akses Off","")
                                print ("Selfbot Off")
                                exit(1)

                        elif dpkText.lower().startswith("kick "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                targets = []
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    if target in Dpk:
                                        pass
                                    else:
                                        try:
                                            klist=[cl]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Wait["Blacklist"][target] = True
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif dpkText.lower() == 'my grup':
                            if user in DpkFamily or user in Wait["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif dpkText.lower().startswith("rejectall grup"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")

                        elif dpkText.lower() == 'status':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    hasil = "╔══════[ Status ]══════"
                                    if Wait["autoAdd"] == True: hasil += "\n╠ Auto Add ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Auto Add ▶Ø🔴F◀"
                                    if Wait["autoJoin"] == True: hasil += "\n╠ Auto Join ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Auto Join ▶Ø🔴F◀"
                                    if Wait["AutoReject"] == True: hasil += "\n╠ Auto Reject Room ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Auto Reject Room ▶Ø🔴F◀"
                                    if Wait["AutojoinTicket"] == True: hasil += "\n╠ Auto Join Ticket ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Auto Join Ticket ▶Ø🔴F◀"
                                    if Wait["autoRead"] == True: hasil += "\n╠ Auto Read ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Auto Read ▶Ø🔴F◀"
                                    if Wait["AutoRespon"] == True: hasil += "\n╠ Detect Mention ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Detect Mention ▶Ø🔴F◀"
                                    if Wait["KickRespon"] == True: hasil += "\n╠ Detect Mention ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Detect Kick Mention ▶Ø🔴F◀"
                                    if Wait["Contact"] == True: hasil += "\n╠ Check Contact ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Check Contact ▶Ø🔴F◀"
                                    if Wait["Timeline"] == True: hasil += "\n╠ Check Post Timeline ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Check Post ▶Ø🔴F◀"
                                    if Wait["IDSticker"] == True: hasil += "\n╠ Check Sticker ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Check Sticker ▶Ø🔴F◀"
                                    if Wait["UnsendPesan"] == True: hasil += "\n╠ Unsend Message ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Unsend Message ▶Ø🔴F◀"
                                    if Wait["KickOn"] == True: hasil += "\n╠ Kick All Member ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Kick All Member ▶Ø🔴F◀"
                                    if Wait["SpamInvite"] == True: hasil += "\n╠ Spam invite via contact ⏩Ø🔵Ň⏪"
                                    else: hasil += "\n╠ Spam invite Via Contact ▶Ø🔴F◀"
                                    hasil += "\n╚══════[ Status ]══════"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif dpkText in ["Unsend on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['UnsendPesan'] = True
                                cl.sendText(kirim,"Cek UnsendMessage Set to on..")
                        elif dpkText in ["Unsend off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['UnsendPesan'] = False
                                cl.sendText(kirim,"Cek UnsendMessage Set to off..")

                        elif dpkText in ["Changepp on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Upfoto'] = True
                                cl.sendText(kirim,"Send Pict For UpPict")
                        elif dpkText in ["Changepp off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Upfoto'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif dpkText in ["Cfotogrup on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['UpfotoGrup'] = True
                                cl.sendText(kirim,"Send Pict For Change Foto Grup")
                        elif dpkText in ["Cfotogrup off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['UpfotoGrup'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif dpkText in ["Timeline on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Timeline'] = True
                                cl.sendText(kirim,"Cek Post Set to on..")
                        elif dpkText in ["Timeline off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Timeline'] = False
                                cl.sendText(kirim,"Cek Post Set to off..")

                        elif dpkText in ["Autojoin on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif dpkText in ["Autojoin off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif dpkText in ["Autoreject on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif dpkText in ["Autoreject off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif dpkText in ["Admin:add-on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Adminadd"] = True
                                cl.sendText(kirim,"Send Contact to added Admin..")
                        elif dpkText in ["Admin:add-off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Adminadd"] = False
                                cl.sendText(kirim,"Send Contact to added Admin in Off..")

                        elif dpkText in ["Admin:del-on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["AdminDel"] = True
                                cl.sendText(kirim,"Send Contact to Dellete Admin..")
                        elif dpkText in ["Admin:del-off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["AdminDel"] = False
                                cl.sendText(kirim,"Send Contact to Dellete Admin in Off..")

                        elif dpkText in ["Gift:on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Gift"] = True
                                cl.sendText(kirim,"Send Contact to send Gift..")
                        elif dpkText in ["Gift:off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Gift"] = False
                                cl.sendText(kirim,"Send Contact to Gift in Off..")

                        elif dpkText in ["Spaminvite on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["SpamInvite"] = True
                                cl.sendText(kirim,"Send Contact to spam grup..")
                        elif dpkText in ["Spaminvite off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["Gift"] = False
                                cl.sendText(kirim,"Send Contact to send grup Off..")

                        elif dpkText in ["Auto jointicket on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif dpkText in ["Auto jointicket off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(msg.text)
                                n_links=[]
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    if Wait["AutojoinTicket"] == True:
                                        group=cl.findGroupByTicket(ticket_id)
                                        cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                        cl.sendText(kirim,"Success Masuk %s" % str(group.name))

                        elif dpkText in ["Copy on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Copy'] = True
                                cl.sendText(kirim,"Send Contact For Copy User")
                        elif dpkText in ["Copy off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Copy'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif dpkText.lower().startswith("clone "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = cl.getContact(ls)
                                        cl.cloneContactProfile(ls)
                                        cl.sendMessage(kirim, "Berhasil mengclone profile {}".format(contact.displayName))

                        elif dpkText.lower() == 'comeback':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    clProfile.displayName = str(ProfileMe["displayName"])
                                    clProfile.statusMessage = str(ProfileMe["statusMessage"])
                                    clProfile.pictureStatus = str(ProfileMe["pictureStatus"])
                                    cl.updateProfileAttribute(8, clProfile.pictureStatus)
                                    cl.updateProfile(clProfile)
                                    cl.sendMessage(kirim, "Already back to my account")
                                except:
                                    cl.sendMessage(kirim, "Error Come Back")

                        elif dpkText in ["Steal on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Steal'] = True
                                cl.sendText(kirim,"Send Contact For Cek Contact")
                        elif dpkText in ["Steal off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Steal'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif dpkText in ["Contact on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Contact'] = True
                                cl.sendText(kirim,"Contact Set to on")
                        elif dpkText in ["Contact off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Contact'] = False
                                cl.sendText(kirim,"Contact Already Off")

                        elif dpkText in ["Invite on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Invite'] = True
                                cl.sendText(kirim,"Send Contact For Invite Target")
                        elif dpkText in ["Invite off"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait['Invite'] = False
                                cl.sendText(kirim,"Send Contact Set Off")

                        elif dpkText.lower() == 'kill on':
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["KillOn"] = True
                                cl.sendMessage(kirim, "SendContact For Kick Taget")
                        elif dpkText.lower() == 'kill off':
                            if user in DpkFamily or user in Wait["Admin"]:
                                Wait["KillOn"] = False
                                cl.sendMessage(kirim, "SendContact For Kick Taget in Off")

                        elif dpkText in ["Mic:add-on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Target["Mic"] = True
                                cl.sendText(kirim,"Send Contact To Clone Message User")
                        elif dpkText in ["Mic:del-on"]:
                            if user in DpkFamily or user in Wait["Admin"]:
                                Target["MicDel"] = True
                                cl.sendText(kirim,"Send Contact Dellete Clone Message User")
                        elif dpkText.lower().startswith("mimic "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                mic = dpkText.replace(sep[0] + " ","")
                                if mic == "on":
                                    if Mozilla["mimic"]["status"] == False:
                                        Mozilla["mimic"]["status"] = True
                                        cl.sendText(kirim,"Mimic Set to on")
                                elif mic == "off":
                                    if Mozilla["mimic"]["status"] == True:
                                        Mozilla["mimic"]["status"] = False
                                        cl.sendText(kirim,"Mimic Message off")

                        elif dpkText.lower() == 'mimiclist':
                            if user in DpkFamily or user in Wait["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cl.sendText(kirim,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cl.getContact(mi_d).displayName
                                    cl.sendText(kirim,mc + "\nFinish")

                        elif dpkText.lower() == 'refresh':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    Wait['Mic'] = False
                                    Wait['MicDel'] = False
                                    Wait['Gift'] = False
                                    Wait['Steal'] = False
                                    Wait['Invite'] = False
                                    Wait['Contact'] = False
                                    Wait['Copy'] = False
                                    Wait['autoJoin'] = False
                                    Wait['autoAdd'] = False
                                    Wait['AutojoinTicket'] = False
                                    Wait['UnsendPesan'] = False
                                    Wait['AutoReject'] = False
                                    Wait['Timeline'] = False
                                    Wait['Upfoto'] = False
                                    Wait['UpfotoGrup'] = False
                                    Wait['Adminadd'] = False
                                    Wait['AdminDel'] = False
                                    Wait['Welcome'] = False
                                    Wait['Leave'] = False
                                    Wait['Ban'] = False
                                    Wait['Unban'] = False
                                    Wait['KillOn'] = False
                                    Wait['KickOn'] = False
                                    Wait['SpamInvite'] = False
                                    cl.sendText(kirim,"Refresh Success")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif dpkText.lower().startswith("my name"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "MyName : {}".format(contact.displayName))
                        elif dpkText.lower().startswith("my bio"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "My Status : \n{}".format(contact.statusMessage))
                        elif dpkText.lower().startswith("my picture"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif dpkText.lower().startswith("my video"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif dpkText.lower().startswith("my cover"):
                            if user in DpkFamily or user in Wait["Admin"]:
                                channel = cl.getProfileCoverURL(user)          
                                path = str(channel)
                                cl.sendImageWithURL(kirim, path)

                        elif dpkText.lower().startswith("stealname "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                        elif dpkText.lower().startswith("stealbio "):
                          if user in DpkFamily or user in Wait["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    cl.sendMessage(kirim, "[ Status Message ]\n{}".format(str(contact.statusMessage)))
                        elif dpkText.lower().startswith("stealpict "):
                          if user in DpkFamily or user in Wait["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                    cl.sendImageWithURL(kirim, str(path))
                        elif dpkText.lower().startswith("stealvideo "):
                          if user in DpkFamily or user in Wait["Admin"]:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = cl.getContact(ls)
                                    path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                    cl.sendVideoWithURL(kirim, str(path))
                        elif dpkText.lower().startswith("stealcover "):
                          if user in DpkFamily or user in Wait["Admin"]:
                            if cl != None:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        channel = cl.getProfileCoverURL(ls)
                                        path = str(channel)
                                        cl.sendImageWithURL(kirim, str(path))
                        elif dpkText.lower().startswith("stealmid "):
                          if user in DpkFamily or user in Wait["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cl.getContact(u).mid
                                  cl.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cl.sendText(kirim, str(e))
                        elif dpkText.lower().startswith("profile "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    cname = cl.getContact(u).displayName
                                    cmid = cl.getContact(u).mid
                                    cstatus = cl.getContact(u).statusMessage
                                    cpic = cl.getContact(u).picturePath
                                    a = cl.getProfileCoverURL(mid=u)
                                    cl.sendText(kirim, 'Nama : '+cname+'\nMid : '+cmid+'\nBio : '+cstatus+'\nURL Picture : http://dl.profile.line.naver.jp'+cpic)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': cmid}, contentType=13)
                                    cl.sendImageWithURL(kirim, a)
                                    if "videoProfile='{" in str(cl.getContact(u)):
                                        cl.sendVideoWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic+'/vp.small')
                                    else:
                                        cl.sendImageWithURL(kirim, 'http://dl.profile.line.naver.jp'+cpic)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif dpkText.lower().startswith("randomgrup: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                              if msg.toType == 2:
                                  strnum = dpkText.replace("randomgrup: ","")
                                  source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                                  try:
                                      num = int(strnum)
                                      group = cl.getGroup(kirim)
                                      for var in range(0,num):
                                          name = "".join([random.choice(source_str) for x in range(10)])
                                          time.sleep(0.01)
                                          group.name = name
                                          cl.updateGroup(group)
                                  except Exception as e:
                                      cl.sendText(kirim, str(e))

                        elif dpkText.lower() == 'announce':
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    gett = cl.getChatRoomAnnouncements(kirim)
                                    for a in gett:
                                        aa = cl.getContact(a.creatorMid).displayName
                                        bb = a.contents
                                        cc = bb.link
                                        textt = bb.text
                                        cl.sendText(kirim, 'Pemberitahuan Grup\n\nLink: ' + str(cc) + '\nPenulis: ' + str(aa) + '\nTeksnya: ' + str(textt))
                                        break
                                except Exception as e:
                                    cl.sendText(kirim, "Pemberitahuan Grup Tidak Ditemukan")

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif dpkText.lower().startswith("topnews"):
                              if user in DpkFamily or user in Wait["Admin"]:
                                  dpk=requests.get("https://newsapi.org/v2/top-headlines?country=id&apiKey=1214d6480f6848e18e01ba6985e2008d")
                                  data=dpk.text
                                  data=json.loads(data)
                                  hasil = "Top News\n\n"
                                  hasil += "(1) " + str(data["articles"][0]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][0]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][0]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][0]["url"])
                                  hasil += "\n\n(2) " + str(data["articles"][1]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][1]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][1]["author"])   
                                  hasil += "\n     Link : " + str(data["articles"][1]["url"])
                                  hasil += "\n\n(3) " + str(data["articles"][2]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][2]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][2]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][2]["url"])
                                  hasil += "\n\n(4) " + str(data["articles"][3]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][3]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][3]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][3]["url"])
                                  hasil += "\n\n(5) " + str(data["articles"][4]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][4]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][4]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][4]["url"])
                                  hasil += "\n\n(6) " + str(data["articles"][5]["title"])                                                        
                                  hasil += "\n     Sumber : " + str(data["articles"][5]["source"]["name"])
                                  hasil += "\n     Penulis : " + str(data["articles"][5]["author"])
                                  hasil += "\n     Link : " + str(data["articles"][5]["url"])
                                  path = data["articles"][3]["urlToImage"]
                                  cl.sendText(kirim, str(hasil))
                                  cl.sendImageWithURL(kirim, str(path))

                        elif "Data birth: " in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                tanggal = dpkText.replace("Data birth: ","")
                                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                lahir = data["data"]["lahir"]
                                usia = data["data"]["usia"]
                                ultah = data["data"]["ultah"]
                                zodiak = data["data"]["zodiak"]
                                cl.sendText(kirim," I N F O R M A S I \n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n  I N F O R M A S I ")

                        elif dpkText.lower().startswith("urban: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                judul = dpkText.replace(sep[0] + " ","")
                                url = "http://api.urbandictionary.com/v0/define?term="+str(judul)
                                with requests.session() as s:
                                    s.headers["User-Agent"] = random.choice(Mozilla["userAgent"])
                                    r = s.get(url)
                                    data = r.text
                                    data = json.loads(data)
                                    cu = "Urban Result\n\n"
                                    cu += "\nText: "+ data["tags"][0]
                                    cu += ","+ data["tags"][1]
                                    cu += ","+ data["tags"][2]
                                    cu += ","+ data["tags"][3]
                                    cu += ","+ data["tags"][4]
                                    cu += ","+ data["tags"][5]
                                    cu += ","+ data["tags"][6]
                                    cu += ","+ data["tags"][7]
                                    cu += "\n[1]\nAuthor: "+str(data["list"][0]["author"])+"\n"
                                    cu += "\nWord: "+str(data["list"][0]["word"])+"\n"
                                    cu += "\nLink: "+str(data["list"][0]["permalink"])+"\n"
                                    cu += "\nDefinition: "+str(data["list"][0]["definition"])+"\n"
                                    cu += "\nExample: "+str(data["list"][0]["example"])+"\n"
                                    cl.sendText(kirim, str(cu))

                        elif "Sslink: " in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                 website = msg.text.replace("Sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cl.sendImageWithURL(kirim, pictweb)

                        elif dpkText.lower().startswith("maps: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                location = dpkText.lower().replace("maps: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    dpk = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = dpk.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "Check Location\n"
                                        ret_ += "\n Lokasi : " + data[0]
                                        ret_ += "\n Google Maps : " + link
                                        ret_ += "\n\nSearch Location Success"
                                    else:
                                        ret_ = "Searching Location Error or Location Tidak Ditemukan"
                                    cl.sendText(kirim,str(ret_))

                        elif dpkText.lower().startswith("cekcuaca: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                weather = dpkText.lower().replace("cekcuaca: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    dpk = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(weather)))
                                    data = dpk.text
                                    data = json.loads(data)
                                    if "result" not in data:
                                        ret_ = "Cheking Weather\n"
                                        ret_ += "\nSuhu : " + data[1].replace("Suhu : ","")
                                        ret_ += "\nLokasi : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\nKelembaban : " + data[2].replace("Kelembaban : ","")
                                        ret_ += "\nTekanan Udara : " + data[3].replace("Tekanan udara : ","")
                                        ret_ += "\nKecepatan Angin : " + data[4].replace("Kecepatan angin : ","")
                                        ret_ += "\n\nSearching Weather Success"
                                    else:
                                        ret_ = "Checking Weather Error or Not Found Location"
                                    cl.sendText(kirim, str(ret_))

                        elif dpkText.lower().startswith("jadwalshalat: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                shalat = dpkText.lower().replace("jadwalshalat: ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
                                    dpk = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(shalat)))
                                    data = dpk.text
                                    data = json.loads(data)
                                    if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                        ret_ = "Jadwal Shalat\n"
                                        ret_ += "\nLocation : " + data[0]
                                        ret_ += "\n " + data[1]
                                        ret_ += "\n " + data[2]
                                        ret_ += "\n " + data[3]
                                        ret_ += "\n " + data[4]
                                        ret_ += "\n " + data[5]
                                        ret_ += "\n\nJadwal Shalat Wilayah"
                                    else:
                                        ret_ = "Jadwa Shalat Wilayah Error or Not Found Location" 
                                    cl.sendText(kirim, str(ret_))

                        elif "Idline: " in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                 msgg = dpkText.replace('Idline: ','')
                                 conn = cl.findContactsByUserid(msgg)
                                 if True:
                                    cl.sendText(kirim,"Link User : https://line.me/ti/p/~" + msgg)
                                    cl.sendMessage(kirim, None, contentMetadata={'mid': conn.mid}, contentType=13)
                                    contact = cl.getContact(conn.mid)
                                    cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                                    cover = cl.getProfileCoverURL(conn.mid)
                                    cl.sendImageWithURL(kirim, cover)
                                    cl.mentionWithDPK(kirim,conn.mid,"Tag User\n","")

                        elif 'say-id: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-en: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-jp: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ar: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ko: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'apakah: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'kapan: ' in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif "Wikipedia: " in dpkText:
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    wiki = dpkText.lower().replace("Wikipedia: ","")
                                    wikipedia.set_lang("id")
                                    pesan="Title ("
                                    pesan+=wikipedia.page(wiki).title
                                    pesan+=")\n\n"
                                    pesan+=wikipedia.summary(wiki, sentences=1)
                                    pesan+="\n"
                                    pesan+=wikipedia.page(wiki).url
                                    cl.sendText(kirim, pesan)
                                except:
                                    try:
                                        pesan="Over Text Limit! Please Click link\n"
                                        pesan+=wikipedia.page(wiki).url
                                        cl.sendText(kirim, pesan)
                                    except Exception as e:
                                        cl.sendText(kirim, str(e))

                        elif dpkText.lower() == 'kalender':
                            if user in DpkFamily or user in Wait["Admin"]:
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                cl.sendMessage(kirim, readTime)

                        elif "gambar: " in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    query = dpkText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cl.download_image(query)
                                    cl.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))                                    

                        elif "youtube: " in dpkText.lower():
                            if user in DpkFamily or user in Wait["Admin"]:
                                try:
                                    query = dpkText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(kirim, x)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif dpkText.lower().startswith("indonesian: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif dpkText.lower().startswith("english: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif dpkText.lower().startswith("korea: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                    sep = dpkText.split(" ")
                                    isi = dpkText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cl.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif dpkText.lower().startswith("japan: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif dpkText.lower().startswith("thailand: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif dpkText.lower().startswith("arab: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif dpkText.lower().startswith("malaysia: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif dpkText.lower().startswith("jawa: "):
                            if user in DpkFamily or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='jw')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Jawa\n\n" + str(text))

    except Exception as error:
        print (error)

#-------------------------------------------- FINNISHING SCRIP ------------------------------------------------#

while True:
    try:
        Operation = LINE.singleTrace(count=50)
        if Operation is not None:
            for arif in Operation:
                LINE.setRevision(arif.revision)
                thread1 = threading.Thread(target=LINE_ARIF_USER, args=(arif,))#self.OpInterrupt[arif.type], args=(arif,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
