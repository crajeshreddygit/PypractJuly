class RajNews:
    def __init__(self,movienews,sportsnews):
        self.movienews = movienews
        self.sportsnews = sportsnews

    def Allnews(self):
        self.movienews.movienewsInfo()
        self.sportsnews.sportsnewsInfo()

class movienews:
    def movienewsInfo(self):
        print("Movie news")

class sportsnews:
    def sportsnewsInfo(self):
        print("Sports news")
movienews = movienews()
sportsnews = sportsnews()
R = RajNews(movienews,sportsnews)
R.Allnews()
