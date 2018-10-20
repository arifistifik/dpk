# -*- coding: utf-8 -*-
from .auth import Auth
from .models import Models
from .talk import Talk
from .square import Square
from .call import Call
from .timeline import Timeline
from akad.ttypes import Message

class LINE(Auth, Models, Talk, Square, Call, Timeline):

    def __init__(self, authToken=None, passwd=None, certificate=None, systemName=None, appName=None, showQr=False, keepLoggedIn=True):
        
        Auth.__init__(self)
        if not (authToken or authToken and passwd):
            self.loginWithQrCode(keepLoggedIn=keepLoggedIn, systemName=systemName, appName=appName, showQr=showQr)
        if authToken and passwd:
            self.loginWithCredential(_id=authToken, passwd=passwd, certificate=certificate, systemName=systemName, appName=appName, keepLoggedIn=keepLoggedIn)
        elif authToken and not passwd:
            self.loginWithAuthToken(authToken=authToken, appName=appName)

        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        self.groups     = self.talk.getGroupIdsJoined()

        Models.__init__(self)
        Talk.__init__(self)
        Square.__init__(self)
        Call.__init__(self)
        Timeline.__init__(self)