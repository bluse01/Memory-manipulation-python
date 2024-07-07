import ctypes
from ctypes import wintypes
import ctypes.wintypes
import ctypes.wintypes
from const import *
from func import *

kernel32 = ctypes.windll.kernel32

pid = getProcID("ac_client.exe")
Handle = kernel32.OpenProcess(PROCESS_ALL_ACCESS, 0, ctypes.wintypes.DWORD(pid))
if (Handle):
    base_address = getModuleAddress(ctypes.wintypes.DWORD(pid), "ac_client.exe")
    if (base_address):

        player_address_base = base_address + 0x18AC00
        player_address = read_int(Handle, player_address_base)
        health_value = player_address + 0xEC

        # reads health of the player
        memory = read_int(Handle, health_value)
        print(f"Player Health value: {memory}")