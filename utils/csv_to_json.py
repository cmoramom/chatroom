# this class covert the csv data from api to json
# todo finish def covert, return json missing


class CVStoJSON(object):
    data = None

    def __init__(self, data=None):
        self.data = data

    def convert(self):
        s = self.data.split('\n')
        col = s[0].split(',')
        row = s[1].split(',')
        return s
