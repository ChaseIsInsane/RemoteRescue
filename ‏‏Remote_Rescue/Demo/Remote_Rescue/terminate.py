dic = {"stop_flag" : False}

def SetStopFlag():
   dic["stop_flag"] = True


def GetStopFlag():
    return dic["stop_flag"]


class RescueException(Exception):
    SetStopFlag()