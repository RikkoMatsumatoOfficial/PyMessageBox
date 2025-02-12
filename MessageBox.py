from ctypes import WinDLL as win

MB_ABORTRETRYIGNORE = int(0x00000002)
MB_CANCELTRYCONTINUE = int(0x00000006)
MB_HELP = int(0x00004000)
MB_OK = int(0x0)
MB_OKCANCEL = int(0x1)
MB_RETRYCANCEL = int(0x00000005)
MB_YESNO = int(0x00000004)
MB_YESNOCANCEL = int(0x00000003)
MB_ICONWARNING = int(0x00000030)
MB_ICONINFORMATION = int(0x00000040)
MB_ICONQUESTION = int(0x00000020)
MB_ICONERROR = int(0x00000010)
IDABORT = int(0x3)
IDCANCEL = int(0x2)
IDCONTINUE = int(0x11)
IDIGNORE = int(0x5)
IDNO = int(0x7)
IDOK = int(0x1)
IDRETRY = int(0x4)
IDTRYAGAIN = int(0x10)
IDYES = int(0x6)

def GetDLL_User32():
    User32 = win("User32.dll")
    return User32

def MessageBoxA(hwnd, message, title, buttons):
    return GetDLL_User32().MessageBoxA(hwnd, message, title, buttons)

def MessageBoxA_WithReturnCode(hwnd, message, title, buttons, retcode):
    if(GetDLL_User32().MessageBoxA(hwnd, message, title, buttons) == retcode):
        return True
    else:
        return False