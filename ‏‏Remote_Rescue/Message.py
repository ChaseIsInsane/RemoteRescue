import keyboard
import json

def serialize(obj):
    return json.dumps(obj).encode()

def deserialize(obj):
    return json.loads(obj)

class Mouse:
    x = 0
    y = 0
    pos = ()
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        
    def GetX(self):
        return self.x
    
    def GetY(self):
        return self.y
    
    def GetPos(self):
        return self.pos
    
    def serialize(self):
        return serialize({
            'type' : 'mouse' ,
            'x' : self.x ,
            'y' : self.y ,
            'pos' : self.pos
        })
    
class Keyboard:
    key = ''
    scan_Codes = None

    def __init__(self, key):
        self.key = key
        self.scan_Codes = keyboard.key_to_scan_codes(self.key)

    def GetKey(self):
        return self.key
    
    def GetScanCodes(self):
        return self.scan_Codes
    
    def SetKey(self, k):
        self.key = k
        self.scan_Codes = keyboard.key_to_scan_codes(self.key)
    
    def serialize(self):
        return serialize({
            'type' : 'keyboard' ,
            'key' : self.key , 
            'scan_Codes' : self.scan_Codes
        })
    
    
    
class ScreenShot:
    image = None
    pixels = None
    size = 0
    size_len = 0
    byte_size_len = None
    size_bytes = None

    def __init__(self, img, pixels):
        self.image = img
        self.pixels = pixels
        self.size = len(self.pixels)
        self.size_len = (self.size.bit_length() + 7) // 8
        self.byte_size_len = bytes([self.size_len])
        self.size_bytes = self.size.to_bytes(self.size_len, 'big')

    def Getimage(self):
        return self.image
    
    def GetPixels(self):
        return self.pixels
    
    def Getsize(self):
        return self.size
    
    def GetSizeLen(self):
        return self.size_len
    
    def GetByteSizeLen(self):
        return self.byte_size_len
    
    def GetSizeBytes(self):
        return self.size_bytes


def main():
    pass

if __name__ == '__main__':
    main()