"""MVP for an Informal Stat Tracker"""

class Scorer():
    def __init__(self, type):
        if(type == 'race'):
            self.maxtime = 300
            self.levelScore = 50

    def assignScore(self, id, timeSpent, playerlist):
        for player in playerlist:
            if(player.getID() == id):
                score = max(0, self.maxtime - timeSpent) * self.levelScore
                player.addScore(score)

class Player():
    def __init__(self, id):
        self.id = str(id)
        self.score = 0

    def addScore(self, score):
        self.score = self.score + score

    def getScore(self):
        return str(self.score)

    def getID(self):
        return str(self.id)

class Board():
    def __init__(self, id, players):
        self.id = id
        self.playerList = []
        for player in players:
            newPlayer = Player(player)
            self.playerList.append(newPlayer)

        self.scorer = Scorer('race')

    def addPlayer(self, id):
        newPlayer = Player(id)
        self.playerList.append(newPlayer)

    def removePlayer(self, id):
        for player in playerList:
            if(player.getID == id):
                playerlist.remove(player)

    def reportMatch(self, matchResult):
        for id in matchResult:
            self.scorer.assignScore(id, matchResult[id], self.playerList)

    def getScores(self):
        scoreList = {}
        for player in self.playerList:
            id = str(player.getID())
            score = str(player.getScore())
            print(score + " " + id)
        return scoreList
