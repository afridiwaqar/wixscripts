import pythoncom
import win32com.client

class NTUser:
    # Uses ADSI to change password under user privileges
    def _ _init_ _(self, userid):
        self.adsiNS = win32com.client.Dispatch('ADsNameSpaces')
        Userpath = "WinNT://<IP>/" + userid + ",adadadad"
        self.adsNTUser = self.adsiNS.GetObject("", Userpath)

    def reset(self, OldPasswd, NewPasswd):
        self.adsNTUser.ChangePassword(OldPasswd, NewPasswd)

    # If you're running under admin privileges, you might use:
        self.adsNTUser.SetPassword(NewPasswd)

def changepass(account, OldPassword, NewPassword):
    try:
        nt = NTUser(account)
        nt.reset(OldPassword, NewPassword)
        print "NT Password change was successful."
        return 1
    except pythoncom.com_error, (hr, msg, exc, arg):
        # Give clearer error messages; avoid stack traces
        scode = exc[5]
        print "NT Password change has failed."

        if scode == 0x8007005:
            print "Your NT Account (%s) is locked out."%account
        elif scode == 0x80070056:
            print "Invalid Old NT Password."
        elif scode == 0x800708ad:
            print "The specified NT Account (%s) does not exist."%account
        elif scode == 0x800708c5:
            print "Your new password cannot be the same as any of your"
            print "previous passwords, and must satisfy the domain's"
            print "password-uniqueness policies."
        else:
            print "ADSI Error - %x: %s, %x\n" % (hr, msg, scode)
        return 0
