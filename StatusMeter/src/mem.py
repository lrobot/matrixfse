from ctypes import * 
from ctypes.wintypes import DWORD 

SIZE_T = c_ulong

class _MEMORYSTATUS(Structure):  
    _fields_ = [("dwLength", DWORD),  
    ("dwMemoryLength", DWORD),  
    ("dwTotalPhys", SIZE_T),  
    ("dwAvailPhys", SIZE_T),  
    ("dwTotalPageFile", SIZE_T),  
    ("dwAvailPageFile", SIZE_T),  
    ("dwTotalVirtual", SIZE_T),  
    ("dwAvailVirtualPhys", SIZE_T)]

    def show(self):  
        return (int(getattr(self,"dwTotalPhys")),int(getattr(self,"dwAvailPhys")))

#test routine  
#memstatus = _MEMORYSTATUS()  
#windll.kernel32.GlobalMemoryStatus(byref(memstatus ))  
#total,free= memstatus.show()  
#print total  
#print free
