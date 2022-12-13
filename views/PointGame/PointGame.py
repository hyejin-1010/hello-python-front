from js import document

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

  
def doneAnswer (answer) :
  global step, games, lastResult
  game = games[step]

  dialog = document.getElementById('dialog') 
  dialog.style.display = 'flex'

  dialogContent = document.getElementById('dialogContent') 
  hintBox = document.getElementById('hintBox') 
  dialogContent.style.display = 'flex'
  hintBox.style.display = 'none'

  rightBox = document.getElementById('rightBox') 
  wrongBox = document.getElementById('wrongBox') 
  commentaryBox = document.getElementById('commentaryBox') 

  lastResult = game['answer'] == answer
  if lastResult :
    rightBox.style.display = 'block'
    wrongBox.style.display = 'none'
    if 'description' in game :
      commentaryBox.innerHTML = game['description']
    commentaryBox.style.display = 'block'
  else :
    rightBox.style.display = 'none'
    wrongBox.style.display = 'block'
    commentaryBox.style.display = 'none'