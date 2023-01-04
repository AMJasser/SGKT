class Args():
    def __init__(self, object):
        for x in object.keys():
            setattr(self, x, object[x])