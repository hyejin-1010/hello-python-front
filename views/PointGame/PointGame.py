from js import document, localStorage
from pyodide.http import pyfetch

def initView () :
    global games
    game = games[step]
    title = document.getElementById('titlePointGame')
    title.innerHTML = '포인트 게임 {}단계'.format(step + 1)
    stepDiv = document.getElementById('step')
    stepDiv.innerHTML = '{}/3'.format(step + 1)
    pointDiv = document.getElementById('point')
    pointDiv.innerHTML = '{}포인트'.format(game.earnPoint)

    questionTitle = document.getElementById('questionTitle')
    questionTitle.innerHTML = game.title
    questionContent = document.getElementById('questionContent')

    if game.content :
      questionContent.style.display = 'block'
      questionContent.innerHTML = game.content
    else :
      questionContent.style.display = 'none'
    inputAnswerBox = document.getElementById('inputAnswerBox')
    selectionAnswerBox = document.getElementById('selectionAnswerBox')
    oxAnswerBox = document.getElementById('oxAnswerBox')

    if game.type == 'input' :
      selectionAnswerBox.style.display = 'none'
      oxAnswerBox.style.display = 'none'
      inputAnswerBox.style.display = 'flex'
    elif game.type == 'OX' :
      selectionAnswerBox.style.display = 'none'
      inputAnswerBox.style.display = 'none'
      oxAnswerBox.style.display = 'flex'
    else :
      selectionAnswerBox.style.display = 'grid'
      inputAnswerBox.style.display = 'none'
      oxAnswerBox.style.display = 'none'

      for i in range(len(game.selection)) :
        selection = game.selection[i]
        selectionEl = document.getElementById('selection{}Content'.format(i + 1))
        selectionEl.innerHTML = selection

def reducePoint () :
  global step
  if games[step].earnPoint > 0 :
    games[step].earnPoint -= 1
    pointDiv = document.getElementById('point')
    pointDiv.innerHTML = '{}포인트'.format(games[step].earnPoint)
  
async def doCorrectAnswer (game) :
  document.getElementById('rightBox') .style.display = 'block'
  document.getElementById('wrongBox') .style.display = 'none'
  commentaryBox = document.getElementById('commentaryBox') 
  if game.description :
    commentaryBox.innerHTML = game.description
  commentaryBox.style.display = 'block'

  userid = localStorage.getItem('hp-user-id')
  response = await pyfetch(url="http://127.0.0.1:5001/addPoint", method="POST", body=json.dumps({ 'userid': userid, 'point': games[step].earnPoint }))
  response_dict = await response.json()

async def doneAnswer (answer) :
  global step, games, lastResult
  game = games[step]

  dialogContent = document.getElementById('dialogContent') 
  hintBox = document.getElementById('hintBox') 
  dialogContent.style.display = 'flex'
  hintBox.style.display = 'none'

  dialog = document.getElementById('dialog') 
  dialog.style.display = 'flex'

  commentaryBox = document.getElementById('commentaryBox') 
  lastResult = game.answer == answer
  if lastResult :
    await doCorrectAnswer(game)
  else : # 오답인 경우 
    document.getElementById('rightBox') .style.display = 'none'
    document.getElementById('wrongBox') .style.display = 'block'
    commentaryBox.style.display = 'none'
    reducePoint()

