class Learning () :

  def __init__(self, data) : 
    self.learningID = data['learningID']              # unique id
    self.Title = data['Title']                        # Learning Title
    self.classID = data['classID']                    # Learning이 속한 Class ID
    self.order = data['order']                        # Ordering
    self.pointGameIDs = data['pointGameIDs'] or []    # Learning에 속한 PointGame ID List
    self.video = data['video']                        # Learning Video 파일 이름

    self.circleID = 'circle_item_{}'.format(self.learningID)

  # Main 페이지에서 Learning을 Circle Item 으로 보여지는데, 그것을 만들어주는 함수 
  def getCircle (self, doneLectures) :  
    lectureDiv = document.createElement('div')
    lineDiv = document.createElement('div')

    # circle 별 class 적용 (index의 짝홀수 여부에 따라 상단/하단 위치에 할 수 있도록 class 적용)
    if self.order % 2 == 0 : 
      lectureDiv.className = 'circle circle-odd'
      lineDiv.className = 'downLine'
    else :
      lectureDiv.className = 'circle circle-even'
      lineDiv.className ='upLine'

    # 이미 완료한 Learning 인지 확인 
    if self.learningID in doneLectures :
      lectureDiv.className += ' done-circle'
    lectureDiv.setAttribute('id', self.circleID)
    # lineDiv.setAttribute('id', self.circleID)

    # Circle 내 텍스트 넣기 
    lectureSpan = document.createElement('span')
    lectureSpan.appendChild(document.createTextNode(self.order))
    lectureSpan.className = 'txt'

    # Circle 내 Hover 텍스트 넣기 
    lectureHoverSpan = document.createElement('span')
    lectureHoverSpan.appendChild(document.createTextNode(self.Title))
    lectureHoverSpan.className = 'txt-hover'

    lectureDiv.appendChild(lectureSpan)
    lectureDiv.appendChild(lectureHoverSpan)
    lectureDiv.appendChild(lineDiv)

    return lectureDiv

class PointGame () :
  def __init__(self, data) : 
    self.pointGameID = data['pointGameID']
    self.title = data['title']                # 문제 타이틀 
    self.type = data['type']                  # 문제 타입 ('input', 'selection', 'ox')
    self.answer = data['answer']              # 문제 정답 
    self.hint = data['hint']                  # 문제 힌트 
    self.earnPoint = data['earnPoint']        # 문제 포인트 
    self.content = data['content'] if 'content' in data else None # 문제 내용
    self.description = data['description'] if 'description' in data else None # 문제 내용
    self.selection = data['selection'] if 'selection' in data else []  # 문제 보기 List (type: 'selection')
