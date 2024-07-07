import ctypes

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFFF)
TH32CS_SNAPMODULE32 = 0x00000010
TH32CS_SNAPMODULE = 0x00000008
TH32CS_SNAPPROCESS = 0x00000002
INVALID_HANDLE_VALUE = -1

kernel32 = ctypes.windll.kernel32

class PROCESSENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes.DWORD),
        ("cntUsage", ctypes.wintypes.DWORD),
        ("th32ProcessID", ctypes.wintypes.DWORD),
        ("th32DefaultHeapID", ctypes.POINTER(ctypes.c_ulong)),
        ("th32ModuleID", ctypes.wintypes.DWORD),
        ("cntThreads", ctypes.wintypes.DWORD),
        ("th32ParentProcessID", ctypes.wintypes.DWORD),
        ("pcPriClassBase", ctypes.wintypes.LONG),
        ("dwFlags", ctypes.wintypes.DWORD),
        ("szExeFile", ctypes.wintypes.CHAR * 260),
    ]

class MODULEENTRY32(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes.DWORD),
        ("th32ModuleID", ctypes.wintypes.DWORD),
        ("th32ProcessID", ctypes.wintypes.DWORD),
        ("GlblcntUsage", ctypes.wintypes.DWORD),
        ("ProccntUsage", ctypes.wintypes.DWORD),
        ("modBaseAddr", ctypes.POINTER(ctypes.wintypes.BYTE)),
        ("modBaseSize", ctypes.wintypes.DWORD),
        ("hModule", ctypes.wintypes.HMODULE),
        ("szModule", ctypes.wintypes.CHAR * 256),
        ("szExePath", ctypes.wintypes.CHAR * 260),
    ]

kernel32.ReadProcessMemory.argtypes = [
    ctypes.wintypes.HANDLE,       
    ctypes.wintypes.LPCVOID,       
    ctypes.wintypes.LPVOID,      
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]