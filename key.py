# For Windows
# http://stackoverflow.com/questions/1823762/sendkeys-for-python-3-1-on-windows
# https://stackoverflow.com/a/38888131

import win32api
import win32con
import win32gui
import time, sys
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

# Determine what input to use.
INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

# Key event registers for the flag.
KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

XBUTTON1 = 0x0001
XBUTTON2 = 0x0002

MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_ABSOLUTE = 0x8000
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# msdn.microsoft.com/en-us/library/dd375731
wintypes.ULONG_PTR = wintypes.WPARAM
class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
				
class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))
    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk, MAPVK_VK_TO_VSC, 0)
			
class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))
				
class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD), ("_input", _INPUT))
LPINPUT = ctypes.POINTER(INPUT)

def PressKey(hexKeyCode):
	x = INPUT(type=INPUT_KEYBOARD,
			ki=KEYBDINPUT(wVk=hexKeyCode))
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
	
def ReleaseKey(hexKeyCode):
	x = INPUT(type=INPUT_KEYBOARD,
			ki=KEYBDINPUT(wVk=hexKeyCode, dwFlags=KEYEVENTF_KEYUP))
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
	
def PressMouse(x_value, y_value):
	x = INPUT(type=INPUT_MOUSE,
			mi=MOUSEINPUT(dx=x_value, dy=y_value, dwFlags=MOUSEEVENTF_LEFTDOWN))
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
	
def ReleaseMouse(x_value, y_value):
	x = INPUT(type=INPUT_MOUSE,
			mi=MOUSEINPUT(dx=x_value, dy=y_value, dwFlags=MOUSEEVENTF_LEFTUP))
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))


keyDelay = 0.1
# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
keymap = {	
	"1": 0x31,
	"2": 0x32,
	"3": 0x33,
	"4": 0x34,
	"5": 0x35,
	"6": 0x36,
	"7": 0x37,
	"8": 0x38,
	"9": 0x39,
	"0": 0x30,
	"minus": 0xBD,
	"equals": 0xBB,
	
	"Esc": win32con.VK_ESCAPE,
	"W": 0x57,
	"A": 0x41,
	"S": 0x53,
	"D": 0x44,
	"I": 0x49,
	"Target": 0xC0, # ` ~ key
	"Attack": 0x45, # E key
	"F1": win32con.VK_F1,
	"F2": win32con.VK_F2,
	"F3": win32con.VK_F3,
	"F4": win32con.VK_F4,
	"F5": win32con.VK_F5,
	"F6": win32con.VK_F6,
	"F7": win32con.VK_F7,
	"F8": win32con.VK_F8,
	"F9": win32con.VK_F9,
	"F10": win32con.VK_F10,
	"F11": win32con.VK_F11,
	"F12": win32con.VK_F12,
	"whold": "whold",
	"ahold": "ahold",
	"shold": "shold",
	"dhold": "dhold",
	"self": "self",
	"brionac": win32con.VK_MULTIPLY,
	"fighter": win32con.VK_ADD,
	"chains": win32con.VK_SUBTRACT,
	"music": 0x47,
	"alch": 0xBE,
	"H": 0x48,
	"J": 0x4A,
	"K": 0x4B,
}

# this way has to keep window in focus
def sendKey(button):
	if button == "whold":
		PressKey(keymap["W"])
		time.sleep(keyDelay * 5)
		ReleaseKey(keymap["W"])
	elif(button == "ahold"):
		PressKey(keymap["A"])
		time.sleep(keyDelay * 5)
		ReleaseKey(keymap["A"])
	elif(button == "shold"):
		PressKey(keymap["S"])
		time.sleep(keyDelay * 5)
		ReleaseKey(keymap["S"])
	elif(button == "dhold"):
		PressKey(keymap["D"])
		time.sleep(keyDelay * 5)
		ReleaseKey(keymap["D"])
	elif(button == "self"):
		PressKey(0xA2)
		time.sleep(0.05)
		PressKey(0x45)
		time.sleep(keyDelay * 3)
		ReleaseKey(0xA2)
		time.sleep(0.05)
		ReleaseKey(0x45)
	else:
		PressKey(keymap[button])
		time.sleep(keyDelay)
		ReleaseKey(keymap[button])


def SimpleWindowCheck(windowname):
    window = None
    try:
        window = win32gui.FindWindow(windowName, None)
    except win32gui.error:
        try: 
            window = win32gui.FindWindow(None, windowName)
        except win32gui.error:
            return False
        else:
            return window
    else:
        return window

if __name__ == "__main__":
    windowName = sys.argv[1]
    key = sys.argv[2]

    #winId = SimpleWindowCheck(windowName)
    # winId = None

    #if not (winId):
    #    windowList = []
    #    
    #    def enumHandler(hwnd, list):
    #        if windowName in win32gui.GetWindowText(hwnd):
    #            list.append(hwnd)
        
    #    win32gui.EnumWindows(enumHandler, windowList)
    #    # only the first id, may need to try the others
    #    winId = windowList[0]

    #    # can check with this
    #    for hwnd in windowList:
    #        hwndChild = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    #        # print("window title/id/child id: ", win32gui.GetWindowText(hwnd), "/", hwnd, "/", hwndChild)

    #win32gui.ShowWindow(winId, win32con.SW_SHOWNORMAL)
    #win32gui.SetForegroundWindow(winId)
    sendKey(key)