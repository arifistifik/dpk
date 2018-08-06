from ARIFISTIFIK import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
from multiprocessing import Pool, Process
from ffmpy import FFmpeg
import time, random, asyncio, timeit, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, urllib, urllib.parse, ast, pytz, wikipedia, pafy, youtube_dl, atexit

print ("\n\n ---  START LOGIN TO ✍Ð₱₭ ฿Ø₮ ---\n")

#cl = LINE()
cl = LINE(authTokenDPK="EvHkngrC42BFD7piAiVb.0PzLwS72Fl1EGGJMnIN3IW.n1DfgexSLbx0SRcKLvwEWA8jyBVMUfSlPX4gVqF3Bf4=")
cl.log("YOUR TOKEN : {}".format(str(cl.authToken)))
channel = LINEChannel(cl,cl.server.CHANNEL_ID['LINE_TIMELINE'])
cl.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#line1 = LINE()
line1 = LINE(authTokenDPK="EvUSNiHdBFIksB35Upff.zsjptOGse28bSLj1PuTA7W.zn5fuMcQEaR3TbJcHVrLR7YV1NqmF0CMFCMl6N8WHtk=")
line1.log("YOUR TOKEN : {}".format(str(line1.authToken)))
channel = LINEChannel(line1,line1.server.CHANNEL_ID['LINE_TIMELINE'])
line1.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#line2 = LINE()
line2 = LINE(authTokenDPK="EvObvAgAgIgIjbq7Ojhe.ER7E8i7845TKzN3C6OKW3G.2Jaa5OobZrVLZ82P4jQLQcvXL70u+ug+svKJv49dc4g=")
line2.log("YOUR TOKEN : {}".format(str(line2.authToken)))
channel = LINEChannel(line2,line2.server.CHANNEL_ID['LINE_TIMELINE'])
line2.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

#line3 = LINE()
line3 = LINE(authTokenDPK="Evu2VMUGTcEJPZF2Mfs1.vhYs8JJrCSZTWWlRYI//mq.iuLB11hhOZkTfwL22XL6jhtelTLPiRy70p2KJ/13YK0=")
line3.log("YOUR TOKEN : {}".format(str(line3.authToken)))
channel = LINEChannel(line3,line3.server.CHANNEL_ID['LINE_TIMELINE'])
line3.log("CHANNEL TOKEN : " + str(channel.getChannelResult()))

print ("✍Ð₱₭ ฿Ø₮ LOGIN SUCCESS")

clProfile = cl.getProfile()
clSettings = cl.getSettings()
LINE = LINEPoll(cl)

Dpk = [cl,line1,line2,line3]
mid = cl.profile.mid
MID1 = line1.profile.mid
MID2 = line2.profile.mid
MID3 = line3.profile.mid
DpkBot=[mid,MID1,MID2,MID3]
Owner=["ud296655acef67cbd5e8208e63629f78b","u65224f4e8812136f01b25275a54b5aef"]
DPKfams = DpkBot + Dpk + Owner

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

Wait = {
    "UnsendPesan":True,
    "SpamInvite":False,
    "Contact":False,
    "GName":"ARIFISTIFIK",
    "AutoRespon":True,
    "DpkRespon":"dîh ηgëtåg äķü mülü... Kămư kë§ëÞîåη ¥åk...???",
    "KickRespon":False,
    "KillOn":False,
    "KickOn":False,
    "Upfoto":False,
    "UpfotoBot":False,
    "UpfotoGroup":False,
    "Steal":False,
    "Invite":False,
    "Copy":False,
    "autoAdd":True,
    "PesanAdd":"⏩HAYO KETAHUAN LO ADD GUA 😊⏪",
    "ContactAdd":{},
    "autoBlock":False,
    "autoJoin":True,
    "AutojoinTicket":False,
    "AutoReject":False,
    "autoRead":False,
    "IDSticker":False,
    "Timeline":True,
    "Welcome":False,
    "BackupBot":True,
    "WcText": "ƜЄԼƇƠMЄ ƬƠ MƳ ƑƛMƧ \n Jåňĝąņ ņăķăl ¥ä...?😊ørāņg ňyå bäîķ-băïk ði§īņî\yuķ ķ3ñålåň bïăř bån¥åķ ťëmen-nŷå😅",
    "Leave":False,
    "WvText": "MƯŇĢĶÏÑ ÅĶŰÑ ÐÏÄ ĻÏMỊŤ...😢",
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
    "AddMention":True,
    "Admin": {
        "ud296655acef67cbd5e8208e63629f78b":True,  #MID ADMIN
        "u65224f4e8812136f01b25275a54b5aef":True
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

DpkProtect = {
    'protect':False,
    'linkprotect':False,
    'inviteprotect':False,
    'cancelprotect':False,
    'ProtectCancelled':False,
}

DpkCctv={
    "Point1":{},
    "Point2":{},
    "Point3":{}
}

Help ="""╔═══════════════════
╠☬➣  MËÑÜ ĦÉĹP  ☬➣  ⏩⏩
╠═══════════════════
╠☬➣ [ ŤŘÅÑ$ĻĀŤØŘ ]⏩⏩⏩
╠═══════════════════
╠☬➣ indonesian:
╠☬➣ english:
╠☬➣ korea:
╠☬➣ japan:
╠☬➣ thailand:
╠☬➣ arab:
╠☬➣ malaysia:
╠☬➣ jawa:
╠═══════════════════
╠═══BØŤ$   ÇŐMMÅÑÐ════
╠☬➣ me
╠☬➣ my name
╠☬➣ my bio
╠☬➣ my picture
╠☬➣ my cover
╠☬➣ my video
╠☬➣ speed
╠☬➣ responsename
╠☬➣ my bot
╠☬➣ my team
╠☬➣ spam on [jmlah teks]
╠☬➣ cekmkd: [mid]
╠☬➣ banlock [@]
╠☬➣ banlist
╠☬➣ contact ban
╠☬➣ ban:on
╠☬➣ unban:on
╠☬➣ clear ban
╠☬➣ blocklist
╠☬➣ friendlist
╠☬➣ friendlist mid
╠☬➣ mid [@]
╠☬➣ profile [@]
╠☬➣ runtime
╠☬➣ broadcast:
╠☬➣ contactbc:
╠☬➣ adminadd [@]
╠☬➣ admindel [@]
╠☬➣ admin:add-on
╠☬➣ admin:del-on
╠☬➣ changename:
╠☬➣ changenameall:
╠☬➣ changebio:
╠☬➣ changebioall:
╠☬➣ remove pesan
╠☬➣ restart
╠☬➣ bot logout
╠☬➣ kick [@]
╠☬➣ status
╠☬➣ allprotect on/off
╠☬➣ backup on/off
╠☬➣ unsend on/off
╠☬➣ changepp on/off
╠☬➣ changeppbot on/off
╠☬➣ timeline on/off
╠☬➣ autojoin on/off
╠☬➣ autoreject on/off
╠☬➣ auto jointicket on/off
╠☬➣ gift:on/off
╠☬➣ copy on/off
╠☬➣ clone [@]
╠☬➣ comeback
╠☬➣ steal on/off
╠☬➣ contact on/off
╠☬➣ mic:add-on
╠☬➣ mic:del-on
╠☬➣ mimic on/off
╠☬➣ mimiclist
╠☬➣ refresh
╠═══════════════════
╠☬➣ [ GŘØƯP ÇŐMMÅÑÐ ]   ⏩
╠═══════════════════
╠☬➣ dpk join
╠☬➣ dpk bye
╠☬➣ leaveall grup
╠☬➣ kick [on,off->kickall]
╠☬➣ invite on/off
╠☬➣ kill on/off
╠☬➣ rejectall grup
╠☬➣ lurking on/off/reset
╠☬➣ lurking read
╠☬➣ sider on/off
╠☬➣ tagall
╠☬➣ welcome on/off
╠☬➣ changewelcome: [teks]
╠☬➣ leave on/off
╠☬➣ changeleave: [teks]
╠☬➣ memberlist
╠☬➣ link on/off
╠☬➣ my grup
╠☬➣ bot1 grup
╠☬➣ bot2 grup
╠☬➣ bot3 grup
╠☬➣ gurl
╠☬➣ gcreator
╠☬➣ invite gcreator
╠☬➣ ginfo
╠☬➣ grup id
╠☬➣ cfotogrup on/off
╠☬➣ spaminvite on/off
╠═══════════════════
╠☬➣ [ MËĐÏÄ ÇŐMMÅÑÐ ]   ⏩
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
╠═══════════════════
╠☬➣  ƛƦƖƑƖƧƬƖƑƖƘ  ☬➣   ⏩⏩
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

def LINE_FAST_USER(fast):
    global time
    global ast
    global groupParam
    try:
        if fast.type == 0:
            return
        if fast.type == 5:
            if Wait["autoAdd"] == True:
                if (Wait["PesanAdd"] in [""," ","\n",None]):
                    pass
                else:
                    Wait["ContactAdd"][fast.param2] = True
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} " + str(Wait["PesanAdd"]).format(usr.displayName))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':mid}, contentType=13)

        if fast.type == 5:
            if Wait['autoBlock'] == True:
                try:
                    usr = cl.getContact(op.param2)
                    cl.sendMessage(fast.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(usr.displayName))
                    cl.talk.blockContact(0, fast.param1)
                    Wait["Blacklist"][fast.param2] = True
                except Exception as e:
                	cl.log("[SEND_MESSAGE] ERROR : " + str(e))

#--------------------------------------------- PARAM SCRIP AUTO JOIN BOT & AUTO REJECT ------------------------------------------------#

        if fast.type == 13:
            if mid in fast.param3:
              if Wait['autoJoin'] == True:
                if fast.param2 in DPKfams and fast.param2 in Wait["Admin"]:
                    cl.acceptGroupInvitation(fast.param1)
                    print ("ANDA JOIN DI GRUP")
            if MID1 in fast.param3:
              if Wait['autoJoin'] == True:
                if fast.param2 in DPKfams and fast.param2 in Wait["Admin"]:
                    line1.acceptGroupInvitation(fast.param1)
                    print ("BOT 1 JOIN GRUP")
            if MID2 in fast.param3:
              if Wait['autoJoin'] == True:
                if fast.param2 in DPKfams and fast.param2 in Wait["Admin"]:
                    line2.acceptGroupInvitation(fast.param1)
                    print ("BOT 2 JOIN GRUP")
            if MID3 in fast.param3:
              if Wait['autoJoin'] == True:
                if fast.param2 in DPKfams and fast.param2 in Wait["Admin"]:
                    line3.acceptGroupInvitation(fast.param1)
                    print ("BOT 3 JOIN GRUP")
                    pass

        if fast.type == 13:
            if mid in fast.param3:
              if Wait['AutoReject'] == True:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
            if MID1 in fast.param3:
              if Wait["AutoReject"] == True:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    gid = line1.getGroupIdsInvited()
                    for i in gid:
                        line1.rejectGroupInvitation(i)
            if MID2 in fast.param3:
              if Wait["AutoReject"] == True:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    gid = line2.getGroupIdsInvited()
                    for i in gid:
                        line2.rejectGroupInvitation(i)
            if MID3 in fast.param3:
              if Wait["AutoReject"] == True:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    gid = line3.getGroupIdsInvited()
                    for i in gid:
                        line3.rejectGroupInvitation(i)
                        pass

#------------------- ( 1 ) ------------------------- PEMBATAS SCRIP SIDER & WC LV ------------------------------------------------#

        elif fast.type == 55:
            try:
                if DpkCctv['Point1'][fast.param1]==True:
                    if fast.param1 in DpkCctv['Point2']:  
                        Name = cl.getContact(fast.param2).displayName
                        if Name in DpkCctv['Point3'][fast.param1]:
                            pass
                        else:
                            DpkCctv['Point3'][fast.param1] += "\n~" + Name
                            if " " in Name:
                                nick = Name.split(' ')
                                if len(nick) == 2:
                                    cl.mentionWithDPK(fast.param1,fast.param2," нαι\n","" + "\n ηgιηтιρ αנα gαк вσsєη кαк ???" )
                                else:
                                    cl.mentionWithDPK(fast.param1,fast.param2," ηah\n","" + "\n sєкαяαηg ηgιηтιρ dîåη¥å" )
                            else:
                                cl.mentionWithDPK(fast.param1,fast.param2," нeyø...\n","" + "\n lîåtin åρα кαк?" )
                    else:
                        pass
                else:
                    pass
            except:
                pass

        if fast.type == 55:
            try:
                if fast.param1 in Wait['readPoint']:
                    if fast.param2 in Wait['readMember'][fast.param1]:
                        pass
                    else:
                        Wait['readMember'][fast.param1] += fast.param2
                    Wait['ROM'][fast.param1][fast.param2] = fast.param2
                else:
                   pass
            except:
                pass   

        if fast.type == 17:
            if Wait["Welcome"] == True:
                if fast.param2 not in Dpk:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithDPK(fast.param1,fast.param2," Hii","" + "\n " + str(Wait['WcText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS JOIN THE GROUP")

        if fast.type == 15:
            if Wait["Leave"] == True:
                if fast.param2 not in Dpk:
                    ginfo = cl.getGroup(fast.param1)
                    cl.mentionWithDPK(fast.param1,fast.param2," Hii","" + "\n " + str(Wait['LvText']))
                    cl.sendMessage(fast.param1, None, contentMetadata={'mid':fast.param2}, contentType=13)
                    print ("MEMBER HAS LEFT THE GROUP")

#--------------------------------------------- PARAM SCRIP FOR BACKUP BOT ------------------------------------------------#

        if fast.type == 19:
          if Wait["BackupBot"] == True:
            if mid in fast.param3:
              if fast.param2 in DpkBot:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    pass
                else:
                    Wait["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        line1.findAndAddContactsByMid(fast.param3)
                        line1.kickoutFromGroup(fast.param1,[fast.param2])
                        line1.inviteIntoGroup(fast.param1,[fast.param3])
                        cl.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            line2.findAndAddContactsByMid(fast.param3)
                            line2.kickoutFromGroup(fast.param1,[fast.param2])
                            line2.inviteIntoGroup(fast.param1,[fast.param3])
                            cl.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                line3.findAndAddContactsByMid(fast.param3)
                                line3.kickoutFromGroup(fast.param1,[fast.param2])
                                line3.inviteIntoGroup(fast.param1,[fast.param3])
                                cl.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = line1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    line1.updateGroup(x)
                                    Line = line1.reissueGroupTicket(fast.param1)
                                    cl.acceptGroupInvitationByTicket(fast.param1,Line)
                                    line1.acceptGroupInvitationByTicket(fast.param1,Line)
                                    line2.acceptGroupInvitationByTicket(fast.param1,Line)
                                    line3.acceptGroupInvitationByTicket(fast.param1,Line)
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    cl.updateGroup(x)
                                    line1.kickoutFromGroup(fast.param1,[fast.param2])
                                    Line = cl.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return
            
            if MID1 in fast.param3:
              if fast.param2 in DpkBot:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    pass
                else:
                    Wait["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        line2.findAndAddContactsByMid(fast.param3)
                        line2.kickoutFromGroup(fast.param1,[fast.param2])
                        line2.inviteIntoGroup(fast.param1,[fast.param3])
                        line1.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            line3.findAndAddContactsByMid(fast.param3)
                            line3.kickoutFromGroup(fast.param1,[fast.param2])
                            line3.inviteIntoGroup(fast.param1,[fast.param3])
                            line1.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                cl.findAndAddContactsByMid(fast.param3)
                                cl.kickoutFromGroup(fast.param1,[fast.param2])
                                cl.inviteIntoGroup(fast.param1,[fast.param3])
                                line1.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = line2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    line2.updateGroup(x)
                                    Line = line2.reissueGroupTicket(fast.param1)
                                    line1.acceptGroupInvitationByTicket(fast.param1,Line)
                                    x = line1.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    line1.updateGroup(x)
                                    line2.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = line1.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if MID2 in fast.param3:
              if fast.param2 in DpkBot:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    pass
                else:
                    Wait["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        line2.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            line1.findAndAddContactsByMid(fast.param3)
                            line1.kickoutFromGroup(fast.param1,[fast.param2])
                            line1.inviteIntoGroup(fast.param1,[fast.param3])
                            line2.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                line3.findAndAddContactsByMid(fast.param3)
                                line3.kickoutFromGroup(fast.param1,[fast.param2])
                                line3.inviteIntoGroup(fast.param1,[fast.param3])
                                line2.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Line = cl.reissueGroupTicket(fast.param1)
                                    line2.acceptGroupInvitationByTicket(fast.param1,Line)
                                    x = line2.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    line2.updateGroup(x)
                                    line3.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = line2.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

            if MID3 in fast.param3:
              if fast.param2 in DpkBot:
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    pass
                else:
                    Wait["Blacklist"][fast.param2] = True
                    f=codecs.open('st2__b.json','w','utf-8')
                    json.dump(Wait, f, sort_keys=True, indent=4,ensure_ascii=False)
                    try:
                        cl.findAndAddContactsByMid(fast.param3)
                        cl.kickoutFromGroup(fast.param1,[fast.param2])
                        cl.inviteIntoGroup(fast.param1,[fast.param3])
                        line3.acceptGroupInvitation(fast.param1)
                    except:
                        try:
                            line1.findAndAddContactsByMid(fast.param3)
                            line1.kickoutFromGroup(fast.param1,[fast.param2])
                            line1.inviteIntoGroup(fast.param1,[fast.param3])
                            line3.acceptGroupInvitation(fast.param1)
                        except:
                            try:
                                line2.findAndAddContactsByMid(fast.param3)
                                line2.kickoutFromGroup(fast.param1,[fast.param2])
                                line2.inviteIntoGroup(fast.param1,[fast.param3])
                                line3.acceptGroupInvitation(fast.param1)
                            except:
                                try:
                                    x = cl.getGroup(fast.param1)
                                    x.preventedJoinByTicket = False
                                    cl.updateGroup(x)
                                    Line = cl.reissueGroupTicket(fast.param1)
                                    line3.acceptGroupInvitationByTicket(fast.param1,Line)
                                    x = line3.getGroup(fast.param1)
                                    x.preventedJoinByTicket = True
                                    line2.updateGroup(x)
                                    cl.kickoutFromGroup(fast.param1,[fast.param2])
                                    Ticket = line3.reissueGroupTicket(fast.param1)
                                except:
                                    pass
                return

        if fast.type == 13:
          if fast.param3 in Wait["Blacklist"]: # AUTO KICK BLACKLIST
            if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                random.choice(Dpk).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Dpk).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Dpk).updateGroup(G)
                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat, Please suruh dia tobat....\n")

#---------------------------------- SCRIP PROTECT GRUP -------------------------------------#

        if fast.type == 19:
            if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                if fast.param2 in DpkBot:
                    pass
                elif DpkProtect["protect"] == True:
                    random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Wait["Blacklist"][fast.param2] = True
                    random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")

        if fast.type == 11:
            if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                if fast.param2 in DpkBot:
                    pass
                elif DpkProtect["linkprotect"] == True:
                    Wait["Blacklist"][fast.param2] = True
                    G = random.choice(Dpk).getGroup(fast.param1)
                    G.preventedJoinByTicket = True
                    random.choice(Dpk).updateGroup(G)
                    random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                    Wait["Blacklist"][fast.param2] = True

        if fast.type == 13:
          if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
            if fast.param2 in DpkBot:
                pass
            elif DpkProtect["inviteprotect"] == True:
                Wait["Blacklist"][fast.param2] = True
                random.choice(Dpk).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param3])
                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")
                G = random.choice(Dpk).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Dpk).updateGroup(G)
                if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                    if fast.param2 in DpkBot:
                        pass
                    elif DpkProtect["inviteprotect"] == True:
                        Wait["Blacklist"][fast.param2] = True
                        random.choice(Dpk).cancelGroupInvitation(fast.param1,[fast.param3])
                        random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                        random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param3])
                        random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                        random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")
                        G = random.choice(Dpk).getGroup(fast.param1)
                        G.preventedJoinByTicket = True
                        random.choice(Dpk).updateGroup(G)
                        if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                            if fast.param2 in DpkBot:
                                pass
                            elif DpkProtect["cancelprotect"] == True:
                                Wait["Blacklist"][fast.param2] = True
                                random.choice(Dpk).cancelGroupInvitation(fast.param1,[fast.param3])
                                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param3])
                                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")
                                G = random.choice(Dpk).getGroup(fast.param1)
                                G.preventedJoinByTicket = True
                                random.choice(Dpk).updateGroup(G)

        if fast.type == 32:
            if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                if fast.param2 in DpkBot:
                    pass
                elif DpkProtect["ProtectCancelled"] == True:
                    random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                    cl.findAndAddContactsByMid(fast.param3)
                    cl.inviteIntoGroup(fast.param1,[fast.param3])
                    Wait["Blacklist"][fast.param2] = True
                    random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                    random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")

        if fast.type == 19:
            if fast.param3 in Wait["Admin"]:        # JIKA ADMIN KE KICK
              if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                  random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                  line1.findAndAddContactsByMid(fast.param3)
                  line1.inviteIntoGroup(fast.param1,[fast.param3])
                  G = random.choice(Dpk).getGroup(fast.param1)
                  G.preventedJoinByTicket = True
                  random.choice(Dpk).updateGroup(G)
                  Wait["Blacklist"][fast.param2] = True
                  line1.sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                  line1.sendMessage(fast.param1, "Masuk dalam daftar orang bejat (*-_-)/")

        if fast.type == 13:
          if fast.param2 and fast.param3 in Wait["Blacklist"]: # AUTO KICK BLACKLIST
            if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
                random.choice(Dpk).cancelGroupInvitation(fast.param1,[fast.param3])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param3])
                G = random.choice(Dpk).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Dpk).updateGroup(G)
                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat, Please suruh dia tobat....\n")

        if fast.type == 17:
          if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
            if fast.param2 in Wait["Blacklist"]: # AUTO KICK BLACKLIST
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Dpk).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Dpk).updateGroup(G)
                Wait["Blacklist"][op.param2] = True
                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat, Please suruh dia tobat....\n")

        if fast.type == 55:
          if fast.param2 not in DPKfams and fast.param2 not in Owner and fast.param2 not in Wait["Admin"]:
            if fast.param2 in Wait["Blacklist"]: # AUTO KICK BLACKLIST
                random.choice(Dpk).kickoutFromGroup(fast.param1,[fast.param2])
                G = random.choice(Dpk).getGroup(fast.param1)
                G.preventedJoinByTicket = True
                random.choice(Dpk).updateGroup(G)
                Wait["Blacklist"][op.param2] = True
                random.choice(Dpk).sendMessage(fast.param1, None, contentMetadata={'mid': fast.param2}, contentType=13)
                random.choice(Dpk).sendMessage(fast.param1, "Masuk dalam daftar orang bejat, Please suruh dia tobat....\n")

        if fast.type == 46:
            if fast.param2 in DpkBot:
                cl.removeAllMessages()
                line1.removeAllMessages()
                line2.removeAllMessages()
                line3.removeAllMessages()

#------------------- ( 2 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 26:
            msg = fast.message
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
                        line1.sendChatChecked(kirim, msg_id)
                        line2.sendChatChecked(kirim, msg_id)
                        line3.sendChatChecked(kirim, msg_id)
                    if kirim in Wait["readPoint"]:
                        if user not in Wait["ROM"][kirim]:
                            Wait["ROM"][kirim][user] = True
                    if user in Mozilla["mimic"]["target"] and Mozilla["mimic"]["status"] == True and Mozilla["mimic"]["target"][user] == True:
                        text = msg.text
                        if text is not None:
                            cl.sendMessage(kirim,text)
                    if Wait["UnsendPesan"] == True:
                        msg = fast.message
                        if msg.toType == 0:
                            cl.log(" {} - {} ".format(str(user), str(dpkText)))
                        else:
                            cl.log(" {} - {} ".format(str(kirim), str(dpkText)))
                            msg_dict[msg.id] = {"rider": dpkText, "pelaku": user, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    if Wait["Timeline"] == True:
                       if msg.contentType == 16:
                            ret_ = "Info Postingan\n"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(user)
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                            else:
                                auth = "\n Penulis : {}".format(str(contact.displayName))
                                ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                dia = cl.getContact(user)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = 'Pengirim: '
                                xteam = str(dia.displayName)
                                pesan = ''
                                pesan2 = pesan+"@ARIFISTIFIK\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                                zx2.append(zx)
                                kata = "\n Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += kata
                                zxc += pesan2
                                pesan = xpesan + zxc + ret_ + ""
                                cl.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)

        if fast.type == 65:
          if Wait['UnsendPesan'] == True:
              try:
                  you = fast.param1
                  msg.id = fast.param2
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

        if fast.type in [25,26]:
            msg = fast.message
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

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Wait['Upfoto'] == True:
                if user in Owner:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateProfilePicture(path)
                    cl.mentionWithDPK(kirim,user," Update Picture Success ","")
                    Wait['Upfoto'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Wait['UpfotoBot'] == True:
                if user in DPKfams or user in Wait["Admin"]:
                    path1 = line1.downloadObjectMsg(msg.id)
                    path2 = line2.downloadObjectMsg(msg.id)
                    path3 = line3.downloadObjectMsg(msg.id)
                    line1.updateProfilePicture(path1)
                    line2.updateProfilePicture(path2)
                    line3.updateProfilePicture(path3)
                    line1.mentionWithDPK(kirim,user," Update Picture Success ","")
                    line2.mentionWithDPK(kirim,user," Update Picture Success ","")
                    line3.mentionWithDPK(kirim,user," Update Picture Success ","")
                    Wait['UpfotoBot'] = False

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 1:
              if Wait['UpfotoGroup'] == True:
                if user in DPKfams or user in Wait["Admin"]:
                    path = cl.downloadObjectMsg(msg.id)
                    cl.updateGroupPicture(kirim, path)
                    cl.mentionWithDPK(kirim,user," Update Picture Grup Success ","")
                    Wait['UpfotoGroup'] = False

        if fast.type in [25,26]:
          if Wait['Contact'] == True:
              msg = fast.message
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

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                try:
                    if user in DPKfams or user in Wait["Admin"]:
                      if Wait["Ban"] == True:
                        if msg.contentMetadata["mid"] in Wait["Blacklist"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Sudah di daftar Blacklist"))
                            Wait['Ban'] = False
                        else:
                            Wait["Blacklist"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Added in Blacklist"))
                            Wait['Ban'] = False
                      if Wait["Unban"] == True:
                        if msg.contentMetadata["mid"] in Wait["Blacklist"]:
                            del Wait["Blacklist"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Succes dellete in Blacklist"))
                            Wait['Unban'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Nothing in Blacklist"))
                            Wait['Unban'] = False
                      if Wait["Adminadd"] == True:
                        if msg.contentMetadata["mid"] in Wait["Admin"]:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Sudah di daftar Admin"))
                            Wait['Adminadd'] = False
                        else:
                            Wait["Admin"][msg.contentMetadata["mid"]] = True
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Added in Admin"))
                            Wait['Adminadd'] = False
                      if Wait["AdminDel"] == True:
                        if msg.contentMetadata["mid"] in Wait["Admin"]:
                            del Wait["Admin"][msg.contentMetadata["mid"]]
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Succes dellete in Admin"))
                            Wait['AdminDel'] = False
                        else:
                            name = msg.contentMetadata["displayName"]
                            cl.sendMessage(kirim, name + str(" Nothing in Admin"))
                            Wait['AdminDel'] = False
                except Exception as error:
                    cl.sendText(kirim, str(error))

        if fast.type == 25 or fast.type == 26:
          if Wait['Invite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = cl.getGroup(kirim)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            cl.sendText(msg.to, _name + " Sudah Berada DiGrup Ini")
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

        if fast.type == 25 or fast.type == 26:
          if Wait['Steal'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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

        if fast.type == 25 or fast.type == 26:
          if Wait['KillOn'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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
                            if target not in DPKfams:
                                try:
                                    cl.kickoutFromGroup(kirim,[target])
                                    Wait['KillOn'] = False
                                    break
                                except:             
                                     cl.sendText(kirim, 'Target Not Found')
                                     Wait['KillOn'] = False
                                     break

        if fast.type == 25 or fast.type == 26:
          if Wait['Gift'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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
                                line1.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                line2.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                line3.sendMessage(target, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58','PRDTYPE': 'THEME','MSGTPL': '12'}, contentType = 9)
                                Wait['Gift'] = False
                                break
                            except:             
                                 cl.sendText(kirim, 'Target Error')
                                 Wait['Gift'] = False
                                 break

        if fast.type == 25 or fast.type == 26:
          if Wait["Mic"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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

        if fast.type == 25 or fast.type == 26:
          if Wait["MicDel"] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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

        if fast.type == 25 or fast.type == 26:
          if Wait['Copy'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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
        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in mid and msg.toType == 2:
                if "MENTION" in msg.contentMetadata.keys() != None:
                    if Wait['AutoRespon'] == True:
                        contact = cl.getContact(user)
                        cName = contact.displayName
                        balas = [cName + "\n" + str(Wait['DpkRespon'])]
                        ret_ = "" + random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if mention['M'] in mid:
                                  cl.mentionWithDPK(kirim,user,"","" +str(ret_))
                                  cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                                  break

        if fast.type == 26:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 0 and user not in DPKfams or user not in Wait["Admin"]:
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

        if fast.type == 25 or fast.type == 26:
          if Wait['SpamInvite'] == True:
            msg = fast.message
            user = msg._from
            kirim = msg.to
            if msg.contentType == 13:
                if user in DPKfams or user in Wait["Admin"]:
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
                                line1.findAndAddContactsByMid(target)
                                line2.findAndAddContactsByMid(target)
                                line3.findAndAddContactsByMid(target)
                                cl.createGroup("LINE SPAM GROUP",[target]) # KALAU MAU BUAT BANYAK SILAHKAN TAMBAHIN SESUKA KALIAN :>
                                cl.createGroup("LINE SPAM GROUP",[target]) # HANYA SPAM VIA CONTACT
                                cl.createGroup("LINE SPAM GROUP",[target])
                                line1.createGroup("LINE SPAM GROUP",[target])
                                line1.createGroup("LINE SPAM GROUP",[target])
                                line1.createGroup("LINE SPAM GROUP",[target])
                                line2.createGroup("LINE SPAM GROUP",[target])
                                line2.createGroup("LINE SPAM GROUP",[target])
                                line2.createGroup("LINE SPAM GROUP",[target])
                                line3.createGroup("LINE SPAM GROUP",[target])
                                line3.createGroup("LINE SPAM GROUP",[target])
                                line3.createGroup("LINE SPAM GROUP",[target])
                                cl.sendText(kirim,"Spam Invite ke " + korban + "\nSUCCESS..")
                                Wait['SpamInvite'] = False
                            except:             
                                 cl.sendText(kirim, 'Contact error')
                                 Wait['SpamInvite'] = False
                                 break


#------------------- ( 3 ) ------------------------- PEMBATAS SCRIP ------------------------------------------------#

        if fast.type == 25 or fast.type == 26:
            msg = fast.message
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
                        if dpkText.lower() == 'PROSES TRANSISI':
                            cl.sendMessage(0, user)

                        elif dpkText.lower() == "me":
                            if user in DPKfams or user in Wait["Admin"]:
                                cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                                cl.mentionWithDPK(kirim,mid," Hay","")

                        elif dpkText.lower() == "help":
                            if user in DPKfams or user in Wait["Admin"]:
                                 cl.sendMessage(kirim, str(Help))

                        elif dpkText.lower() == "speed":
                            if user in DPKfams or user in Wait["Admin"]:
                                no = time.time()
                                cl.sendText("u805e9f30ea4da7b64a14e0f9cea0767c", ' ')
                                elapsed_time = time.time() - no
                                cl.sendText(kirim, "%s" % (elapsed_time))
                                no1 = time.time()
                                line1.sendText("u805e9f30ea4da7b64a14e0f9cea0767c", ' ')
                                elapsed_time = time.time() - no1
                                line1.sendText(kirim, "%s" % (elapsed_time))
                                no2 = time.time()
                                line2.sendText("u805e9f30ea4da7b64a14e0f9cea0767c", ' ')
                                elapsed_time = time.time() - no2
                                line2.sendText(kirim, "%s" % (elapsed_time))
                                no3 = time.time()
                                line3.sendText("u805e9f30ea4da7b64a14e0f9cea0767c", ' ')
                                elapsed_time = time.time() - no3
                                line3.sendText(kirim, "%s" % (elapsed_time))

                        elif dpkText.lower() == "responsename":
                            if user in DPKfams or user in Wait["Admin"]:
                                dpk1 = cl.getContact(mid).displayName
                                dpk2 = line1.getContact(MID1).displayName
                                dpk3 = line2.getContact(MID2).displayName
                                dpk4 = line3.getContact(MID3).displayName
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                cl.mentionWithDPK(kirim,owner," Ready On ","" + str(" ("+dpk1+")"))
                                line1.mentionWithDPK(kirim,owner," Ready On ","" + str(" ("+dpk2+")"))
                                line2.mentionWithDPK(kirim,owner," Ready On ","" + str(" ("+dpk3+")"))
                                line3.mentionWithDPK(kirim,owner," Ready On ","" + str(" ("+dpk4+")"))

                        elif dpkText.lower() == "my bot":
                            if user in DPKfams or user in Wait["Admin"]:
                               cl.sendMessage(kirim, None, contentMetadata={'mid': mid}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': MID1}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': MID2}, contentType=13)
                               cl.sendMessage(kirim, None, contentMetadata={'mid': MID3}, contentType=13)

                        elif dpkText.lower() == "my team":
                            if user in DPKfams or user in Wait["Admin"]:
                                dpk = ""
                                fams = ""
                                wa = 0
                                wi = 0
                                for m_id in Owner:
                                    wa = wa + 1
                                    end = '\n'
                                    dpk += str(wa) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in Wait["Admin"]:
                                    wi = wi + 1
                                    end = '\n'
                                    fams += str(wi) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendText(kirim,"DPK FAMS\n\nOwner:\n"+dpk+"\nAdmin:\n"+fams+"\n( %s ) TEAM FAMS" %(str(len(Owner)+len(Wait["Admin"]))))                                

                        elif dpkText.lower() == "dpk join":
                            if user in DPKfams or user in Wait["Admin"]:
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = False
                                cl.updateGroup(X)
                                invsend = 0
                                Line = cl.reissueGroupTicket(kirim)
                                line1.acceptGroupInvitationByTicket(kirim,Line)
                                line2.acceptGroupInvitationByTicket(kirim,Line)
                                line3.acceptGroupInvitationByTicket(kirim,Line)
                                X = cl.getGroup(kirim)
                                X.preventedJoinByTicket = True
                                cl.updateGroup(X)
                                X.preventedJoinByTicket(X)
                                cl.updateGroup(X)

                        elif dpkText.lower() == "dpk bye":
                            if user in DPKfams or user in Wait["Admin"]:
                                ginfo = cl.getGroup(kirim)
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                line1.mentionWithDPK(kirim,owner," Oke ","\n Good Bye" + str(" ("+ginfo.name+")"))
                                line3.leaveGroup(kirim)
                                line2.leaveGroup(kirim)
                                line1.leaveGroup(kirim)
                                cl.leaveGroup(kirim)

                        elif dpkText.lower() == "leaveall grup":
                            if user in DPKfams or user in Wait["Admin"]:
                                gid = cl.getGroupIdsJoined()
                                gid = line1.getGroupIdsJoined()
                                gid = line2.getGroupIdsJoined()
                                gid = line3.getGroupIdsJoined()
                                for i in gid:
                                    cl.leaveGroup(i)
                                    line1.leaveGroup(i)
                                    line2.leaveGroup(i)
                                    line3.leaveGroup(i)
                                    print ("Kicker Leave All group")

                        elif dpkText in ["Kick on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["KickOn"] = True
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':1}")
                        elif dpkText in ["Kick off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["KickOn"] = False
                                cl.sendText(kirim,"Status:\n{''cancel'':0,''kick'':0}")

                        elif "Kickall" in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
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
                                          if target not in DPKfams and target not in Wait["Admin"]:
                                            try:
                                                klist=[cl,line1,line2,line3]
                                                kicker=random.choice(klist)
                                                kicker.kickoutFromGroup(kirim,[target])
                                                print (kirim,[g.mid])
                                            except Exception as error:
                                                cl.sendText(kirim, str(error))

                        elif "Spam " in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
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

                        elif "Cekmid: " in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
                                ardian = dpkText.replace("Cekmid: ","")
                                cl.sendMessage(kirim, None, contentMetadata={'mid': ardian}, contentType=13)
                                contact = cl.getContact(ardian)
                                ganteng = cl.getProfileCoverURL(ardian)
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                if Wait["Blacklist"] == {}:
                                    cl.sendText(kirim,"ORANG BEJAT SUDAH TOBAT JADI  DOSANYA TERAMPUNI BOS")
                                else:
                                    mc = "DAFTAR ORANG-ORANG BEJAT NI BOS "
                                    num=1
                                    ragets = cl.getContacts(Wait["Blacklist"])
                                    for mi_d in ragets:
                                        mc+="\n%i. %s" % (num, mi_d.displayName)
                                        num=(num+1)
                                    mc+="\n\n Total %i ORANG BEJAT " % len(ragets)
                                    cl.sendText(kirim, mc)

                        elif dpkText in ["Contact ban"]:
                            if user in DPKfams or user in Wait["Admin"]:
                              if Wait["Blacklist"] == {}:
                                  cl.sendText(kirim,"Tidak Ada Yang masuk dalam daftar orang bejat")
                              else:
                                  cl.sendText(kirim,"Contact Yang masuk dalam daftar orang bejat")
                                  h = ""
                                  for i in Wait["Blacklist"]:
                                      h = cl.getContact(i)
                                      cl.sendMessage(kirim, None, contentMetadata={'mid': i}, contentType=13)

                        elif dpkText in ["Clear ban"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Blacklist"] = {}
                                cl.sendText(kirim,"Aku sudah memaafkan orang-orang bajat itu..")
                                print ("Clear Ban")

                        elif dpkText in ["Ban:on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Ban"] = True
                                cl.sendText(kirim,"Kirimkan kontak orang bejat yang dimaksud...")
                        elif dpkText in ["Unban:on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Unban"] = True
                                cl.sendText(kirim,"Kirimkan kontak orang bejat yang sudah tobat...")

                        elif dpkText.lower() == 'link on':
                            if user in DPKfams or user in Wait["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = False
                                    cl.updateGroup(group)

                        elif dpkText.lower() == 'link off':
                            if user in DPKfams or user in Wait["Admin"]:
                                if msg.toType == 2:
                                    group = cl.getGroup(kirim)
                                    group.preventedJoinByTicket = True
                                    cl.updateGroup(group)

                        elif dpkText.lower() == 'gurl':
                          if user in DPKfams or user in Wait["Admin"]:
                            if msg.toType == 2:
                                grup = cl.getGroup(kirim)
                                if grup.preventedJoinByTicket == False:
                                    set = cl.reissueGroupTicket(kirim)
                                    cl.sendMessage(kirim, "Group Ticket : \nhttps://line.me/R/ti/g/{}".format(str(set)))
                                else:
                                    cl.sendMessage(kirim, "Ketik Link on Dulu kaka")

                        elif dpkText.lower() == 'gcreator':
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                saya = dpkText.replace('Grup id','')
                                gid = cl.getGroup(kirim)
                                cl.sendText(kirim, "ID Grup : \n" + gid.id + "\nName Grup : \n" + str(gid.name))

                        elif 'mid ' in dpkText.lower():
                          if user in DPKfams or user in Wait["Admin"]:
                              try:
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  cmid = cl.getContact(u).mid
                                  cl.sendText(kirim, str(cmid))
                              except Exception as e:
                                  cl.sendText(kirim, str(e))

                        elif "Profile" in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                contact = cl.getContact(key1)
                                cover = cl.getProfileCoverURL(key1)
                                path = str(cover)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                try:
                                    cl.sendText(kirim,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                                    cl.sendImageWithURL(kirim,image)
                                    cl.sendImageWithURL(kirim,path)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif dpkText.lower() == 'lurking on':
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                                        pesan2 = pesan+"@ARIFISTIFIK\n"
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                if kirim in DpkCctv['Point2']:
                                    DpkCctv['Point1'][kirim]=False
                                    cl.sendText(kirim, DpkCctv['Point3'][kirim])
                                else:
                                    cl.sendText(kirim, "Off not Going")

                        elif dpkText.lower().startswith("tagall"):
                            if user in DPKfams or user in Wait["Admin"]:
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
                                            atas = '\n HAI {} '.format(str(gname.name))
                                            atas += '\n Hai {} Semuanya'.format(str(len(local)))
                                        cl.sendMessage(kirim, text=hdc + str(atas), contentMetadata={u'MENTION': json.dumps({'MENTIONEES':com})}, contentType=0)
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif dpkText in ["Welcome on"]:
                          if user in DPKfams or user in Wait["Admin"]:
                            if user in DPKfams:
                                Wait['Welcome'] = True
                                cl.sendText(kirim,"Cek Welcome Already ON")
                        elif dpkText in ["Welcome off"]:
                          if user in DPKfams or user in Wait["Admin"]:
                            if user in DPKfams:
                                Wait['Welcome'] = False
                                cl.sendText(kirim,"Cek Welcome Already Off")

                        elif "changewelcome: " in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                teks = dpkText.split(": ")
                                data = dpkText.replace(teks[0] + ": ","")
                                try:
                                    Wait["WcText"] = data
                                    cl.sendText(kirim,"Name Welcome Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif dpkText in ["Leave on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Leave'] = True
                                cl.sendText(kirim,"Cek Leave Already ON")
                        elif dpkText in ["Leave off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Leave'] = False
                                cl.sendText(kirim,"Cek Leave Already Off")

                        elif "changeleave: " in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                teks = dpkText.split(": ")
                                data = dpkText.replace(teks[0] + ": ","")
                                try:
                                    Wait["LvText"] = data
                                    cl.sendText(kirim,"Name Leave Change to:\n" +str("(" +data+ ")"))
                                except:
                                    cl.sendText(kirim,"Name Error")

                        elif dpkText.lower() == "runtime":
                            if user in DPKfams or user in Wait["Admin"]:
                                eltime = time.time() - mulai                                
                                opn = " "+waktu(eltime)
                                cl.sendText(kirim,"Connect to DPK FAMS\nBot Active\n" + opn)                

                        elif "Broadcast: " in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
                                bc = msg.text.replace("Broadcast: ","")
                                gid = cl.getGroupIdsJoined()
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                for i in gid:
                                    cl.mentionWithDPK(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif "Contactbc: " in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
                                bc = msg.text.replace("Contactbc: ","")
                                gid = cl.getAllContactIds()
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                for i in gid:
                                    cl.mentionWithDPK(i,owner," BROADCAST BY:","\n" + str(" ("+bc+")"))

                        elif "adminadd " in dpkText.lower():
                            if user in DPKfams:
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

                        elif "admindell " in dpkText.lower():
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

                        elif "changename: " in dpkText.lower():
                            if user in DPKfams:
                                name = dpkText.split(": ")
                                change = dpkText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll.displayName = change
                                cl.updateProfile(cll)
                                owner = "ud296655acef67cbd5e8208e63629f78b"
                                cl.mentionWithDPK(kirim,owner," Update Name Success","\n Change to " + str(change))

                        elif "changebio: " in dpkText.lower():
                            if user in DPKfams:
                                proses = dpkText.split(": ")
                                teks = dpkText.replace(proses[0] + ": ","")
                                no1 = cl.getProfile()
                                no1.statusMessage = teks
                                cl.updateProfile(no1)
                                cl.sendText(kirim,"My Bio Change To : " + teks)

                        elif "changenameall: " in dpkText.lower():
                            if user in DPKfams:
                                name = dpkText.split(": ")
                                change = dpkText.replace(name[0] + ": ","")
                                cll = cl.getProfile()
                                cll1 = line1.getProfile()
                                cll2 = line2.getProfile()
                                cll3 = line3.getProfile()
                                cll.displayName = change
                                cll1.displayName = change
                                cll2.displayName = change
                                cll3.displayName = change
                                cl.updateProfile(cll)
                                line1.updateProfile(cll1)
                                line2.updateProfile(cll2)
                                line3.updateProfile(cll3)
                                cl.mentionWithDPK(kirim,user," Update Name Success","\n Change to " + str(change))
                                line1.mentionWithDPK(kirim,user," Update Name Success","\n Change to " + str(change))
                                line2.mentionWithDPK(kirim,user," Update Name Success","\n Change to " + str(change))
                                line3.mentionWithDPK(kirim,user," Update Name Success","\n Change to " + str(change))

                        elif "changebioall: " in dpkText.lower():
                            if user in DPKfams:
                                proses = dpkText.split(": ")
                                teks = dpkText.replace(proses[0] + ": ","")
                                no = cl.getProfile()
                                no1 = line1.getProfile()
                                no2 = line2.getProfile()
                                no3 = line3.getProfile()
                                no.statusMessage = teks
                                no1.statusMessage = teks
                                no2.statusMessage = teks
                                no3.statusMessage = teks
                                cl.updateProfile(no)
                                line1.updateProfile(no1)
                                line2.updateProfile(no2)
                                line3.updateProfile(no3)
                                cl.sendText(kirim,"My Bio Change To : " + teks)
                                line1.sendText(kirim,"My Bio Change To : " + teks)
                                line2.sendText(kirim,"My Bio Change To : " + teks)
                                line3.sendText(kirim,"My Bio Change To : " + teks)

                        elif dpkText.lower() == "remove pesan":
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    cl.removeAllMessages(fast.param2)
                                    line1.removeAllMessages(fast.param2)
                                    line2.removeAllMessages(fast.param2)
                                    line3.removeAllMessages(fast.param2)
                                    ginfo = cl.getGroup(kirim)
                                    owner = "ud296655acef67cbd5e8208e63629f78b"
                                    cl.mentionWithDPK(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    line1.mentionWithDPK(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    line2.mentionWithDPK(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                    line3.mentionWithDPK(kirim,owner," Remove Message Success ","\n In Grup" + str(" ("+ginfo.name+")"))
                                except:
                                    pass

                        elif dpkText.lower() == 'restart':
                            if user in DPKfams:
                                cl.sendText(kirim, 'Restarting Server Prosses..')
                                print ("Restarting Server")
                                restart_program()

                        elif dpkText.lower() == 'bot logout':
                            if user in DPKfams:
                                cl.mentionWithDPK(kirim,user," Akses Off","")
                                print ("Selfbot Off")
                                exit(1)

                        elif "kick " in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
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
                                            klist=[cl,line1,line2,line3]
                                            kicker=random.choice(klist)
                                            kicker.kickoutFromGroup(kirim,[target])
                                            Wait["Blacklist"][target] = True
                                        except Exception as e:
                                            cl.sendText(kirim, str(error))

                        elif dpkText.lower() == 'my grup':
                            if user in DPKfams or user in Wait["Admin"]:
                                groups = cl.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = cl.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                cl.sendText(kirim, str(ret_))

                        elif dpkText.lower() == 'bot1 grup':
                            if user in DPKfams or user in Wait["Admin"]:
                                groups = line1.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = line1.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                line1.sendText(kirim, str(ret_))

                        elif dpkText.lower() == 'bot2 grup':
                            if user in DPKfams or user in Wait["Admin"]:
                                groups = line2.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = line2.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                line2.sendText(kirim, str(ret_))

                        elif dpkText.lower() == 'bot3 grup':
                            if user in DPKfams or user in Wait["Admin"]:
                                groups = line3.groups
                                ret_ = "GRUP JOIN"
                                no = 0 + 1
                                for gid in groups:
                                    group = line3.getGroup(gid)
                                    ret_ += "\n\n{}. {} ".format(str(no), str(group.name))
                                    no += 1
                                ret_ += "\n\nTOTAL {} GRUP JOIN".format(str(len(groups)))
                                line3.sendText(kirim, str(ret_))

                        elif dpkText.lower().startswith("rejectall grup"):
                            if user in DPKfams or user in Wait["Admin"]:
                                ginvited = cl.getGroupIdsInvited()
                                ginvited = line1.getGroupIdsInvited()
                                ginvited = line2.getGroupIdsInvited()
                                ginvited = line3.getGroupIdsInvited()
                                if ginvited != [] and ginvited != None:
                                    for gid in ginvited:
                                        cl.rejectGroupInvitation(gid)
                                        line1.rejectGroupInvitation(gid)
                                        line2.rejectGroupInvitation(gid)
                                        line3.rejectGroupInvitation(gid)
                                    cl.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    line1.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    line2.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                    line3.sendMessage(kirim, "Succes Cancell {} Invite Grup".format(str(len(ginvited))))
                                else:
                                    cl.sendMessage(kirim, "Nothing Invited")
                                    line1.sendMessage(kirim, "Nothing Invited")
                                    line2.sendMessage(kirim, "Nothing Invited")
                                    line3.sendMessage(kirim, "Nothing Invited")

                        elif dpkText.lower() == 'status':
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    hasil = "╔══════[ Status ]"
                                    if Wait["autoAdd"] == True: hasil += "\n╠ Auto Add 🔵[on]"
                                    else: hasil += "\n╠ Auto Add 🔴[off]"
                                    if Wait["autoJoin"] == True: hasil += "\n╠ Auto Join 🔵[on]"
                                    else: hasil += "\n╠ Auto Join 🔴[off]"
                                    if Wait["AutoReject"] == True: hasil += "\n╠ Auto Reject Room 🔵[on]"
                                    else: hasil += "\n╠ Auto Reject Room 🔴[off]"
                                    if Wait["AutojoinTicket"] == True: hasil += "\n╠ Auto Join Ticket 🔵[on]"
                                    else: hasil += "\n╠ Auto Join Ticket 🔴[off]"
                                    if Wait["autoRead"] == True: hasil += "\n╠ Auto Read 🔵[on]"
                                    else: hasil += "\n╠ Auto Read 🔴[off]"
                                    if Wait["AutoRespon"] == True: hasil += "\n╠ Detect Mention 🔵[on]"
                                    else: hasil += "\n╠ Detect Mention 🔴[off]"
                                    if Wait["KickRespon"] == True: hasil += "\n╠ Detect Mention 🔵[on]"
                                    else: hasil += "\n╠ Detect Kick Mention 🔴[off]"
                                    if Wait["Contact"] == True: hasil += "\n╠ Check Contact 🔵[on]"
                                    else: hasil += "\n╠ Check Contact 🔴[off]"
                                    if Wait["Timeline"] == True: hasil += "\n╠ Check Post Timeline 🔵[on]"
                                    else: hasil += "\n╠ Check Post 🔴[off]"
                                    if Wait["IDSticker"] == True: hasil += "\n╠ Check Sticker 🔵[on]"
                                    else: hasil += "\n╠ Check Sticker 🔴[off]"
                                    if Wait["UnsendPesan"] == True: hasil += "\n╠ Unsend Message 🔵[on]"
                                    else: hasil += "\n╠ Unsend Message 🔴[off]"
                                    if DpkProtect["protect"] == True: hasil += "\n╠ Protect Grup 🔵[on]"
                                    else: hasil += "\n╠ Protect Grup 🔴[off]"
                                    if DpkProtect["linkprotect"] == True: hasil += "\n╠ Protect Link Grup 🔵[on]"
                                    else: hasil += "\n╠ Protect Link Grup 🔴[off]"
                                    if DpkProtect["inviteprotect"] == True: hasil += "\n╠ Protect Invite Grup 🔵[on]"
                                    else: hasil += "\n╠ Protect Invite Grup 🔴[off]"
                                    if DpkProtect["cancelprotect"] == True: hasil += "\n╠ Protect Cancel Grup 🔵[on]"
                                    else: hasil += "\n╠ Protect Cancel Grup 🔴[off]"
                                    if DpkProtect["ProtectCancelled"] == True: hasil += "\n╠ Protect Cancel Member 🔵[on]"
                                    else: hasil += "\n╠ Protect Cancel Member 🔴[off]"
                                    if Wait["BackupBot"] == True: hasil += "\n╠ Backup Bot 🔵[on]"
                                    else: hasil += "\n╠ Backup Bot 🔴[off]"
                                    if Wait["KickOn"] == True: hasil += "\n╠ Kick All Member 🔵[on]"
                                    else: hasil += "\n╠ Kick All Member 🔴[off]"
                                    if Wait["SpamInvite"] == True: hasil += "\n╠ Spam invite via contact 🔵[on]"
                                    else: hasil += "\n╠ Spam invite Via Contact 🔴[off]"
                                    hasil += "\n╚══════[ Status ]"
                                    cl.sendMessage(kirim, str(hasil))
                                except Exception as error:
                                    cl.sendMessage(kirim, str(error))

                        elif dpkText in ["Allprotect on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    DpkProtect['protect'] = True
                                    DpkProtect['linkprotect'] = True
                                    DpkProtect['inviteprotect'] = True
                                    DpkProtect['cancelprotect'] = True
                                    DpkProtect['ProtectCancelled'] = True
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"AllProtect Already On in Grup : " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))
                        elif dpkText in ["Allprotect off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    DpkProtect['protect'] = False
                                    DpkProtect['linkprotect'] = False
                                    DpkProtect['inviteprotect'] = False
                                    DpkProtect['cancelprotect'] = False
                                    DpkProtect['ProtectCancelled'] = False
                                    grup = cl.getGroup(kirim)
                                    cl.sendText(kirim,"AllProtect Already Off in Grup : " +str(grup.name))
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif dpkText in ["Backup on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['BackupBot'] = True
                                cl.sendText(kirim,"Backup Bot Ready On")
                        elif dpkText in ["Backup off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['BackupBot'] = False
                                cl.sendText(kirim,"Backup Bot Nonactive")

                        elif dpkText in ["Unsend on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UnsendPesan'] = True
                                cl.sendText(kirim,"Cek UnsendMessage Set to on..")
                        elif dpkText in ["Unsend off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UnsendPesan'] = False
                                cl.sendText(kirim,"Cek UnsendMessage Set to off..")

                        elif dpkText in ["Changepp on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Upfoto'] = True
                                cl.sendText(kirim,"Send Pict For UpPict")
                        elif dpkText in ["Changepp off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Upfoto'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif dpkText in ["Changeppbot on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UpfotoBot'] = True
                                line1.sendText(kirim,"Send Pict For UpPict")
                                line2.sendText(kirim,"Send Pict For UpPict")
                                line3.sendText(kirim,"Send Pict For UpPict")
                        elif dpkText in ["Changeppbot off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UpfotoBot'] = False
                                line1.sendText(kirim,"Send Pict Already Off")
                                line2.sendText(kirim,"Send Pict Already Off")
                                line3.sendText(kirim,"Send Pict Already Off")

                        elif dpkText in ["Cfotogrup on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UpfotoGrup'] = True
                                cl.sendText(kirim,"Send Pict For Change Foto Grup")
                        elif dpkText in ["Cfotogrup off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['UpfotoGrup'] = False
                                cl.sendText(kirim,"Send Pict Already Off")

                        elif dpkText in ["Timeline on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Timeline'] = True
                                cl.sendText(kirim,"Cek Post Set to on..")
                        elif dpkText in ["Timeline off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Timeline'] = False
                                cl.sendText(kirim,"Cek Post Set to off..")

                        elif dpkText in ["Autojoin on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['autoJoin'] = True
                                cl.sendText(kirim,"Join Set To On..")
                        elif dpkText in ["Autojoin off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['autoJoin'] = False
                                cl.sendText(kirim,"Join Set To Off..")

                        elif dpkText in ["Autoreject on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['AutoReject'] = True
                                cl.sendText(msg.to,"Reject Set To On..")
                        elif dpkText in ["Autoreject off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['AutoReject'] = False
                                cl.sendText(msg.to,"Reject Set To Off..")

                        elif dpkText in ["Admin:add-on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Adminadd"] = True
                                cl.sendText(kirim,"Send Contact to added Admin..")
                        elif dpkText in ["Admin:add-off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Adminadd"] = False
                                cl.sendText(kirim,"Send Contact to added Admin in Off..")

                        elif dpkText in ["Admin:del-on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["AdminDel"] = True
                                cl.sendText(kirim,"Send Contact to Dellete Admin..")
                        elif dpkText in ["Admin:del-off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["AdminDel"] = False
                                cl.sendText(kirim,"Send Contact to Dellete Admin in Off..")

                        elif dpkText in ["Gift:on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Gift"] = True
                                cl.sendText(kirim,"Send Contact to send Gift..")
                        elif dpkText in ["Gift:off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Gift"] = False
                                cl.sendText(kirim,"Send Contact to Gift in Off..")

                        elif dpkText in ["Spaminvite on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["SpamInvite"] = True
                                cl.sendText(kirim,"Send Contact to spam grup..")
                        elif dpkText in ["Spaminvite off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["Gift"] = False
                                cl.sendText(kirim,"Send Contact to send grup Off..")

                        elif dpkText in ["Auto jointicket on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["AutojoinTicket"] = True
                                cl.sendText(kirim,"Join Ticket Set To On")
                        elif dpkText in ["Auto jointicket off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["AutojoinTicket"] = False
                                cl.sendText(kirim,"Join Ticket Set To Off")
                        elif '/ti/g/' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Copy'] = True
                                cl.sendText(kirim,"Send Contact For Copy User")
                        elif dpkText in ["Copy off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Copy'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif dpkText.lower().startswith("clone "):
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Steal'] = True
                                cl.sendText(kirim,"Send Contact For Cek Contact")
                        elif dpkText in ["Steal off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Steal'] = False
                                cl.sendText(kirim,"Send Contact Already Off")

                        elif dpkText in ["Contact on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Contact'] = True
                                cl.sendText(kirim,"Contact Set to on")
                        elif dpkText in ["Contact off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Contact'] = False
                                cl.sendText(kirim,"Contact Already Off")

                        elif dpkText in ["Invite on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Invite'] = True
                                cl.sendText(kirim,"Send Contact For Invite Target")
                        elif dpkText in ["Invite off"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait['Invite'] = False
                                cl.sendText(kirim,"Send Contact Set Off")

                        elif dpkText.lower() == 'kill on':
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["KillOn"] = True
                                cl.sendMessage(kirim, "SendContact For Kick Taget")
                        elif dpkText.lower() == 'kill off':
                            if user in DPKfams or user in Wait["Admin"]:
                                Wait["KillOn"] = False
                                cl.sendMessage(kirim, "SendContact For Kick Taget in Off")

                        elif dpkText in ["Mic:add-on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Target["Mic"] = True
                                cl.sendText(kirim,"Send Contact To Clone Message User")
                        elif dpkText in ["Mic:del-on"]:
                            if user in DPKfams or user in Wait["Admin"]:
                                Target["MicDel"] = True
                                cl.sendText(kirim,"Send Contact Dellete Clone Message User")
                        elif "mimic" in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                if Mozilla["mimic"]["target"] == {}:
                                    cl.sendText(kirim,"Tidak Ada Target")
                                else:
                                    mc = "Mimic List"
                                    for mi_d in Mozilla["mimic"]["target"]:
                                        mc += "\n? "+cl.getContact(mi_d).displayName
                                    cl.sendText(kirim,mc + "\nFinish")

                        elif dpkText.lower() == 'refresh':
                            if user in DPKfams or user in Wait["Admin"]:
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
                                    Wait['UpfotoBot'] = False
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

                        elif dpkText.lower() == 'bot on':
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    Wait['Mic'] = False
                                    Wait['MicDel'] = False
                                    Wait['Gift'] = True
                                    Wait['Steal'] = False
                                    Wait['Invite'] = False
                                    Wait['Contact'] = False
                                    Wait['Copy'] = False
                                    Wait['autoJoin'] = True
                                    Wait['autoAdd'] = True
                                    Wait['AutojoinTicket'] = True
                                    Wait['UnsendPesan'] = True
                                    Wait['AutoReject'] = False
                                    Wait['Timeline'] = False
                                    Wait['Upfoto'] = False
                                    Wait['UpfotoBot'] = False
                                    Wait['UpfotoGrup'] = False
                                    Wait['Adminadd'] = False
                                    Wait['AdminDel'] = False
                                    Wait['Welcome'] = True
                                    Wait['Leave'] = True
                                    Wait['Ban'] = False
                                    Wait['Unban'] = False
                                    Wait['KillOn'] = False
                                    Wait['KickOn'] = False
                                    Wait['SpamInvite'] = False
                                    cl.sendText(kirim,"Bot mode on")
                                except Exception as e:
                                    cl.sendText(kirim, str(error))

                        elif dpkText.lower().startswith("my name"):
                            if user in DPKfams or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "MyName : {}".format(contact.displayName))
                        elif dpkText.lower().startswith("my bio"):
                            if user in DPKfams or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendMessage(kirim, "My Status : \n{}".format(contact.statusMessage))
                        elif dpkText.lower().startswith("my picture"):
                            if user in DPKfams or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendImageWithURL(kirim,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                        elif dpkText.lower().startswith("my video"):
                            if user in DPKfams or user in Wait["Admin"]:
                                contact = cl.getContact(user)
                                cl.sendVideoWithURL(kirim,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                        elif dpkText.lower().startswith("my cover"):
                            if user in DPKfams or user in Wait["Admin"]:
                                channel = cl.getProfileCoverURL(user)          
                                path = str(channel)
                                cl.sendImageWithURL(kirim, path)

#------------------------------------------ SOCIAL MEDIA ----------------------------------------------------#

                        elif dpkText.lower().startswith("topnews"):
                              if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                 website = msg.text.replace("Sslink: ","")
                                 response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                                 data = response.json()
                                 pictweb = data['result']
                                 cl.sendImageWithURL(kirim, pictweb)

                        elif dpkText.lower().startswith("maps: "):
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-id: ','')
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-en: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-en: ','')
                                    tts = gTTS(text=isi, lang='en', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-jp: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-jp: ','')
                                    tts = gTTS(text=isi, lang='ja', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ar: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-ar: ','')
                                    tts = gTTS(text=isi, lang='ar', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'say-ko: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    isi = dpkText.lower().replace('say-ko: ','')
                                    tts = gTTS(text=isi, lang='ko', slow=False)
                                    tts.save('temp.mp3')
                                    cl.sendAudio(kirim, 'temp.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'apakah: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    txt = ['iya','tidak','bisa jadi','mungkin saja','tidak mungkin','au ah gelap']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif 'kapan: ' in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    txt = ['kapan kapan','besok','satu abad lagi','Hari ini','Tahun depan','Minggu depan','Bulan depan','Sebentar lagi']
                                    isi = random.choice(txt)
                                    tts = gTTS(text=isi, lang='id', slow=False)
                                    tts.save('temp2.mp3')
                                    cl.sendAudio(kirim, 'temp2.mp3')
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

                        elif "Wikipedia: " in dpkText:
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
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
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    query = dpkText.replace("gambar: ", "")
                                    query = query.replace(" ", "+")
                                    gambar = cl.download_image(query)
                                    cl.sendImageWithURL(kirim, gambar)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))                                    

                        elif "youtube: " in dpkText.lower():
                            if user in DPKfams or user in Wait["Admin"]:
                                try:
                                    query = dpkText.replace("youtube: ", "")
                                    query = query.replace(" ", "+")
                                    x = cl.youtube(query)
                                    cl.sendText(kirim, x)
                                except Exception as e:
                                    cl.sendText(kirim, str(e))

#--------------------------------- TRANSLATOR -------------------------------------------------#

                        elif dpkText.lower().startswith("indonesian: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='id')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Indonesian\n\n" + str(text))

                        elif dpkText.lower().startswith("english: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='en')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator English\n\n" + str(text))

                        elif dpkText.lower().startswith("korea: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                    sep = dpkText.split(" ")
                                    isi = dpkText.replace(sep[0] + " ","")
                                    translator = Translator()
                                    hasil = translator.translate(isi, dest='ko')
                                    text = hasil.text
                                    cl.sendMessage(kirim, "Translator Korea\n\n" + str(text))

                        elif dpkText.lower().startswith("japan: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ja')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Japan\n\n" + str(text))

                        elif dpkText.lower().startswith("thailand: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='th')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Thailand\n\n" + str(text))

                        elif dpkText.lower().startswith("arab: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ar')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Saudi Arabia\n\n" + str(text))

                        elif dpkText.lower().startswith("malaysia: "):
                            if user in DPKfams or user in Wait["Admin"]:
                                sep = dpkText.split(" ")
                                isi = dpkText.replace(sep[0] + " ","")
                                translator = Translator()
                                hasil = translator.translate(isi, dest='ms')
                                text = hasil.text
                                cl.sendMessage(kirim, "Translator Malaysia\n\n" + str(text))

                        elif dpkText.lower().startswith("jawa: "):
                            if user in DPKfams or user in Wait["Admin"]:
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
            for fast in Operation:
                LINE.setRevision(fast.revision)
                thread1 = threading.Thread(target=LINE_FAST_USER, args=(fast,))#self.OpInterrupt[fast.type], args=(fast,)
                thread1.start()
                thread1.join()
    except Exception as error:
        print (error)
