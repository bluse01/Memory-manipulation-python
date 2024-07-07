import ctypes
import struct
from const import * 

kernel32 = ctypes.windll.kernel32

def getProcID(procname):
    procid = None
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0)

    if snapshot != INVALID_HANDLE_VALUE:
        procEntry = PROCESSENTRY32()
        procEntry.dwSize = ctypes.sizeof(PROCESSENTRY32)
        
        if kernel32.Process32First(snapshot, ctypes.byref(procEntry)):
            while True:
                if procEntry.szExeFile.decode("utf-8") == procname:
                    procid = procEntry.th32ProcessID
                    break

                if not kernel32.Process32Next(snapshot, ctypes.byref(procEntry)):
                    break

        kernel32.CloseHandle(snapshot)
    else:
        print("error")

    return procid

    
def getModuleAddress(pid, modulename):
    baseAddress = None
    snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPMODULE | TH32CS_SNAPMODULE32, pid)

    if snapshot != INVALID_HANDLE_VALUE:
        modEntry = MODULEENTRY32()
        modEntry.dwSize = ctypes.sizeof(MODULEENTRY32)

        if kernel32.Module32First(snapshot, ctypes.byref(modEntry)):
            while True:
                if modEntry.szModule.decode("utf-8") == modulename:
                    baseAddress = ctypes.addressof(modEntry.modBaseAddr.contents)
                    break

                if not kernel32.Module32Next(snapshot, ctypes.byref(modEntry)):
                    break

        kernel32.CloseHandle(snapshot)
    else:
        raise ctypes.WinError()

    return baseAddress

def read_process_memory(process_handle, base_address, size):
    buffer = ctypes.create_string_buffer(size)
    bytesRead = ctypes.c_size_t(0)

    if kernel32.ReadProcessMemory(process_handle, base_address, buffer, size, ctypes.byref(bytesRead)):
        return buffer.raw[:bytesRead.value]
    else:
        print("read_process_memory error")

def read_int(process_handle, address):
    buffer = read_process_memory(process_handle, address, 4)
    return struct.unpack('I', buffer)[0]