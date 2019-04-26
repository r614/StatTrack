import barebones as bs

testBoard = bs.Board('Daily Mini', ['Roshan', 'Arpan', 'Laura', 'Roan'])

matchResult1 = {'Roshan' : 5, 'Arpan' : 200, 'Laura': 50, 'Roan' : 300 }
matchResult2 = {'Roshan' : 300, 'Arpan' : 20, 'Laura': 70, 'Roan' : 1231 }
matchResult3 = {'Roshan' : 120, 'Arpan' : 60, 'Laura': 15, 'Roan' : 40 }
matchResult4 = {'Roshan' : 57, 'Arpan' : 21, 'Laura': 80, 'Roan' : 6 }
matchResult5 = {'Roshan' : 47, 'Arpan' : 32, 'Laura': 59, 'Roan' : 30 }
matchResult6 = {'Roshan' : 24, 'Arpan' : 71, 'Laura': 7, 'Roan' : 90 }
matchResult7 = {'Roshan' : 12, 'Arpan' : 210, 'Laura': 29, 'Roan' : 37 }
matchResult8 = {'Roshan' : 66, 'Arpan' : 90, 'Laura': 37, 'Roan' : 30 }
matchResult9 = {'Roshan' : 90, 'Arpan' : 51, 'Laura': 121, 'Roan' : 20 }
matchResult10 = {'Roshan' : 70, 'Arpan' : 200, 'Laura': 345, 'Roan' : 21 }


testBoard.reportMatch(matchResult1)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult2)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult3)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult4)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult5)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult6)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult7)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult8)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult9)
testBoard.getScores()
print('-------------')

testBoard.reportMatch(matchResult10)
testBoard.getScores()
print('-------------')
