from random import randint
import random
from tkinter import*
import os
import sys

root = Tk()
root.title("PYJACK")
root.geometry("1000x740+280+10")

# 배경 이미지
bg_img = PhotoImage(file="texture/pyjacktable.png")
d_img = PhotoImage(file="texture/waiter.png")

# 프레임 설정
frame1 =Frame(root,bg="black")
frame1.pack(fill=X,ipadx=0,ipady=0,side=RIGHT)

frame2 =Frame(root,bg="black")
frame2.pack(fill=BOTH,ipadx=100,ipady=0)

frame3 =Frame(root,bg="black")
frame3.pack(fill=X,ipadx=0,ipady=0)

frame4 =Frame(root,bg="black")
frame4.pack(fill=BOTH,ipadx=100,ipady=320)

# 이미지 삽입
dealer = Label(frame2,image=d_img,bg='black')
dealer.pack()
pyjack_bgi = Label(frame3,image = bg_img, bg='black')
pyjack_bgi.pack()

# 플레이 스크린
text2 = Text(frame1,fg="white",bg="black",width=40,height=3)
text2.pack()

# 텍스트 창
text =Text(frame1,width=40,height=33,bg='black',fg='white')
text.pack()

## 배팅 버튼
text3 = Text(frame1,fg="white",bg="black",width=20,height=1)
text3.pack(pady=10)
text3.insert(END,"       Betting")

b_1 = Button(frame1,text="충전",width=20)
b_1.pack(pady=2)

b_2 = Button(frame1,text="x1",width=20)
b_2.pack(pady=2)
b_2.config(state=DISABLED)

b_3 = Button(frame1,text="x2",width=20)
b_3.pack(pady=2)
b_3.config(state=DISABLED)

b_4 = Button(frame1,text="x4",width=20)
b_4.pack(pady=2)
b_4.config(state=DISABLED)

# 게임 버튼 설정
b_hit = Button(frame4, text="HiT",width=20)
b_hit.grid(row=1,column=0,padx=45,ipady=2)

b_stay = Button(frame4, text="STAY", width=20)
b_stay.grid(row=1,column=1,padx=45,ipady=2)

b_replay = Button(frame4, text="REPLAY", width=20)
b_replay.grid(row=1,column=2,padx=45,ipady=2)

b_play = Button(frame4, text="PLAY", width=20)
b_play.grid(row=2,column=1,pady=30,ipady=2)

card_place = PhotoImage(file="texture/card/black.gif")

def card_home(): ## 초기 카드 배치 화면
    img_place1 = Label(frame3,image=card_place, borderwidth=0)
    img_place2 = Label(frame3,image=card_place, borderwidth=0)
    img_place3 = Label(frame3,image=card_place, borderwidth=0)
    img_place4 = Label(frame3,image=card_place, borderwidth=0)
    img_place5 = Label(frame3,image=card_place, borderwidth=0)

    img_place7 = Label(frame3,image=card_place, borderwidth=0)
    img_place8 = Label(frame3,image=card_place, borderwidth=0)
    img_place9 = Label(frame3,image=card_place, borderwidth=0)
    img_place10 = Label(frame3,image=card_place, borderwidth=0)
    img_place11 = Label(frame3,image=card_place, borderwidth=0)
    img_place12 = Label(frame3,image=card_place, borderwidth=0)

    img_place1.place(x=240,y=270)
    img_place2.place(x=300,y=270)
    img_place3.place(x=360,y=270)
    img_place4.place(x=420,y=270)
    img_place5.place(x=480,y=270)

    img_place7.place(x=210,y=100)
    img_place8.place(x=270,y=100)
    img_place9.place(x=330,y=100)
    img_place10.place(x=390,y=100)
    img_place11.place(x=450,y=100)
    img_place12.place(x=510,y=100)

## 전적을 보여주기 위한 변수
com_win = 0    
player_win = 0

## 베팅액
com = 100000
player = 100000
bet_value =2000

dealer_opp = 2
player_opp = 2

## 카드를 뽑아 선택하는 특성을 가진 클래스
class deck(object):
    deck1={'s':13,'c':13,'h':13,'d':13} # 모양별로 카드 수를 지정함
    deck2={1:'s',2:'c',3:'h',4:'d'}
    deck3={1:"a", 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:"j", 12:"q", 13:"k" }
    deck4 =[]
    
    def __init__(self):
        text.insert(END,"\n   카드를 섞었습니다.")
    def getCard(self): # 카드 섞어서 한 개의 카드를 뽑는다(a,1,2,...,j,k,q)

        global deck1 
        global deck2
        global deck3

        while 1:
            i=randint(1,4)
            j=randint(1,13)
            if self.deck1[self.deck2[i]] != 0:
                self.card = self.deck3[j] + self.deck2[i]

                if self.card in deck.deck4:
                    continue

                else:
                    deck.deck4.append(self.card)
                    self.deck1[self.deck2[i]] -= 1
                    self.Filename(self.card)                 
                    break

            else:
                return self.getCard()
        
        return self.deck3[j] ## 숫자 반환


    def Filename(self,x): ## 카드 이름을 저장하고 이미지 불러옴
        
        self.str_x =str(x)
        self.filename ="texture/card/"+ self.str_x +".gif"
        return self.filename

    def cardview_main(self,count): ## 시작버튼 누를 때 카드 위치 지정 
        self.count = count        
        
        if self.count == 1: ## 플레이어 첫번째 카드 위치 및 표시
            self.drawcard1 = PhotoImage(file=self.filename)
            self.viewer1 = Label(frame3,image=self.drawcard1, borderwidth=0)
            self.viewer1.place(x=240,y=270)

        elif self.count == 2: ## 플레이어 두번째 카드 위치 및 표시
            self.drawcard2 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard2, borderwidth=0)
            self.viewer.place(x=300,y=270)
        
        elif self.count == 3: ## 딜러 첫번째 카드 위치 및 표시
            self.drawcard3 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard3, borderwidth=0)
            self.viewer.place(x=210,y=100)

    def cardview_backopen(self,filename_hid): ## 원래 숨겨져있던 카드를 보여주는 것
        self.drawcard = PhotoImage(file=filename_hid)
        self.viewer = Label(frame3,image=self.drawcard, borderwidth=0)
        self.viewer.place(x=270,y=100)

    def cardview_hit(self,a): ## hit할때 카드 보여주는 함수
        
        if a == 360: 
            self.drawcard4 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard4, borderwidth=0)
            self.viewer.place(x=a,y=270)
        elif a == 420: 
            self.drawcard5 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard5, borderwidth=0)
            self.viewer.place(x=a,y=270)
        elif a == 480: 
            self.drawcard6 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard6, borderwidth=0)
            self.viewer.place(x=a,y=270)
        elif a == 540: 
            self.drawcard10 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard10, borderwidth=0)
            self.viewer.place(x=a,y=270)

    def cardview_stay(self,b): ## stay할때 카드 보여주는 함수

        if b == 330: 
            self.drawcard7 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard7, borderwidth=0)
            self.viewer.place(x=b,y=100)
        elif b == 390:
            self.drawcard8 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard8, borderwidth=0)
            self.viewer.place(x=b,y=100)
        elif b == 450: 
            self.drawcard9 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard9, borderwidth=0)
            self.viewer.place(x=b,y=100)
        elif b == 510: 
            self.drawcard11 = PhotoImage(file=self.filename)
            self.viewer = Label(frame3,image=self.drawcard11, borderwidth=0)
            self.viewer.place(x=b,y=100)


        
def cardValue(card): ## 뽑힌 카드 숫자에 점수를 매기는 함수
   global playerTotal
   cardsDict={"a":1 , '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "j":10, "q":10, "k":10 }

   if card=="a":
      if playerTotal<=10:
         return 11
      else:
         return 1
   else:
      return cardsDict[card]

count = 360 
count2 = 330

# 배팅액 점수 환산
def deal_win():
    global com
    global player
    global bet_value
    
    com =com + bet_value
    player = player - bet_value

    if player < 0:
        text.insert(END,"\n   플레이어가 파산하였습니다.")
        text.insert(END,"\n   칩을 충전하십시오.")
    vital()
    
def play_win():
    global com
    global player
    global bet_value
    global dealer_opp
    
    com =com - bet_value
    player = player + bet_value
    if com < 0:
        text.insert(END,"\n   딜러가 파산하였습니다.")
        dealer_opp -= 1

        if dealer_opp == 0:
            text.insert(END,"\n   딜러가 마지막 충전을 사용하였습니다.")
            com = 100000
            text.insert(END,"\n   REPLAY를 눌러주세요.")
        elif dealer_opp >0:
            text.insert(END,"\n   딜러가 총 2회 중 %d회 충전하였습니다."%dealer_opp)
            com = 100000
            text.insert(END,"\n   REPLAY를 눌러주세요.")
        else:
            text.insert(END,"\n   충전이 불가합니다")
            text.insert(END,"\n   게임이 불가합니다.")
    vital()
    
def bet1(event): # 플레이어가 칩 충전
    global com
    global player
    global bet_value
    global player_opp
    player_opp -= 1
    
    if player_opp == 0:
        text.insert(END,"\n   플레이어가 마지막 충전을 했습니다.")
        player = 100000
        text.insert(END,"\n   REPLAY를 눌러주세요.")
        b_1.config(state=DISABLED)
    elif player_opp >0:
        text.insert(END,"\n   %d으로 베팅을 하였습니다."%bet_value)
        player = 100000
        text.insert(END,"\n   총 2회 중 %d회 충전하였습니다."%player_opp)
        text.insert(END,"\n   REPLAY를 눌러주세요.")
    else:
        text.insert(END,"\n   충전이 불가합니다")
        text.insert(END,"\n   게임이 불가합니다.")
    return bet_value

def bet2(event): # x1 배팅
    global com
    global player
    global bet_value
    text.insert(END,"\n   %d으로 베팅을 하였습니다."%bet_value)
    text.insert(END,"\n   REPLAY를 눌러주세요.")
    return bet_value

def bet3(event):  # x2 배팅
    global com
    global player
    global bet_value

    bet_value = bet_value*2
    text.insert(END,"\n   %d으로 베팅을 하였습니다."%bet_value)
    text.insert(END,"\n   REPLAY를 눌러주세요.")
    return bet_value

def bet4(event): # x4 배팅
    global com
    global player
    global bet_value
    bet_value = bet_value*4
    text.insert(END,"\n   %d으로 베팅을 하였습니다."%bet_value)
    text.insert(END,"\n   REPLAY를 눌러주세요.")
    return bet_value

def vital(): # 버튼 활성화
    b_2.config(state=NORMAL)
    b_3.config(state=NORMAL)
    b_4.config(state=NORMAL)  

def hit(event):
      global count ## hit 카드 위치 설정을 위한 변수
      global newDeck
      global playerTotal
      global card_hid
      global filename_hid
      global com_win 
      global player_win

      card=newDeck.getCard()
      playerTotal=playerTotal+ cardValue(card)
      
      newDeck.cardview_hit(count) 
   
      text.insert(END,"\n   당신의 카드는: "+str(card)+" 입니다.")
      
      if playerTotal >21:
         text.insert(END,"\n   ===============================")
         text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
         text.insert(END,"\n   ===============================")
         text.insert(END,"\n   당신은 졌습니다.\n   배팅을 선택하시오")
         deal_win()
         com_win += 1
         newDeck.cardview_backopen(filename_hid) ## 게임 종료 시 숨겨진 카드 확인
         
      elif playerTotal==21:
         pass

      else:
         action()
         
      count += 60 
      
def replay(event):
    global count
    global count2
    global com_win 
    global player_win

    count = 360
    count2 = 330
    card_home()
    main()

def action(): # HIT, STAY 버튼 선택 메시지
   global playerTotal
   global newDeck
   global com_win 
   global player_win
 
   text.insert(END,"\n   -------------------------------")
   text.insert(END,"   \n   HIT 또는 STAY를 눌러주세요.")
   text.insert(END,"\n   -------------------------------")
  
def stay(event):
   global com_win 
   global player_win

   global cardValue
   global computerTotal
   global card
   global count2

   global card_hid
   global filename_hid 

   if 1:
       text.insert(END,"\n   딜러의 두번째 카드는: "+str(card_hid)+" 입니다.")
       newDeck.cardview_backopen(filename_hid)

       while(computerTotal <= 21):
            if computerTotal>16:
                if playerTotal<=21 and playerTotal == computerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   무승부입니다!!!\n   REPLAY를 눌러주세요.")
                        break
                    
                if playerTotal<=21 and computerTotal< playerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   당신은 이겼습니다!!!\n   배팅을 선택하시오.")
                        play_win()
                        player_win += 1 

                        break

                if playerTotal<=21 and computerTotal> playerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   당신은 졌습니다.\n   배팅을 선택하시오")
                        deal_win()
                        com_win += 1
                        break
                    
            else:
                card=newDeck.getCard()
                newDeck.cardview_stay(count2)
                count2 +=60
                computerTotal+=cardValue(card)
                text.insert(END,"\n   딜러의 카드는: "+str(card)+" 입니다.")
                
                if computerTotal>21:
                    text.insert(END,"\n   ===============================")
                    text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                    text.insert(END,"\n   ===============================")
                    text.insert(END,"\n   당신은 이겼습니다!!!\n   배팅을 선택하시오.")
                    play_win()
                    player_win += 1
                    break

                else:
                    if playerTotal<=21 and playerTotal == computerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   무승부입니다!!!\n   REPLAY를 눌러주세요.")
                        break
                    if playerTotal<=21 and computerTotal< playerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   당신은 이겼습니다!!!\n   배팅을 선택하시오.")
                        play_win()
                        player_win += 1
                        break

                    if playerTotal<=21 and computerTotal> playerTotal:
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   딜러 점수:%d  플레이어 점수:%d"%(computerTotal,playerTotal))
                        text.insert(END,"\n   ===============================")
                        text.insert(END,"\n   당신은 졌습니다.\n   배팅을 선택하시오")
                        deal_win()
                        com_win += 1
                        break
            
def main():
    # 승점 계산 변수
    global com_win 
    global player_win

    global newDeck
    global card
    global playerTotal
    global computerTotal

    # 딜러 두번째 카드 숨기기 위한 변수
    global card_hid
    global filename_hid
    global drawcard4
    global viewer

    # 배팅액 변수
    global com
    global player
    global bet_value


    card_home()
    text.delete('1.0',END)
    text2.delete('1.0', END)
    text2.insert(END,"\n   딜러 승 %d : 플레이어 승 %d\n"%(com_win,player_win)) ## 플레이어 전적을 보여줌
    text.insert(END,"\n   딜러 칩 \%d"%com)
    text.insert(END,"\n   플레이어 칩 \%d"%player)
    text.insert(END,"\n   배팅액 \%d"%bet_value)
    text.insert(END,"\n   -------------------------------")
    text.insert(END,"\n   카드를 섞습니다.")

    newDeck=deck() ## newDeck 객체 생성
    playerTotal, computerTotal=0,0
    
    text.insert(END,"\n   Player에게 카드를 나눠줍니다.")
    card=newDeck.getCard()
    newDeck.cardview_main(1) ## 플레이어 첫번째 카드 보여줌
    
    text.insert(END,"\n   당신의 첫번째 카드는: "+ str(card)+" 입니다.")
    playerTotal=playerTotal+ cardValue(card)
    card=newDeck.getCard()
    newDeck.cardview_main(2) # 플레이어 두번째 카드 보여줌

    text.insert(END,"\n   당신의 두번째 카드는: "+ str(card)+" 입니다.")
    playerTotal=playerTotal+ cardValue(card)
    card=newDeck.getCard()
    newDeck.cardview_main(3) # 딜러 첫번째 카드 보여줌

    text.insert(END,"\n   딜러의 첫번째 카드는: "+ str(card)+" 입니다.")
    computerTotal+= cardValue(card)

    ## 딜러 두번째 카드 숨기기 위해 변수 따로 설정
    card_hid=newDeck.getCard()
    filename_hid = newDeck.filename 
    computerTotal += cardValue(card_hid)
    
    drawcard4 = PhotoImage(file="texture/card/back.gif") ## 카드 뒷장을 보여주기 위한 것
    viewer = Label(frame3,image=drawcard4, borderwidth=0)
    viewer.place(x=270,y=100)
    
    action()

    if (newDeck.deck1['s'] + newDeck.deck1['c'] + newDeck.deck1['h'] + newDeck.deck1['d']) == 0: 
        text.insert(END,"\n   카드가 없습니다.")
        text.insert(END,"\n   -------------------------------")

if __name__=='__main__':
    card_home()
    text.insert(END,"\n\n   게임을 시작하려면\n   Play버튼을 눌러주세요.")

def play(event):
   main()


b_hit.bind("<Button-1>",hit)
b_stay.bind("<Button-1>",stay)
b_replay.bind("<Button-1>",replay)
b_play.bind("<Button-1>",play)

b_1.bind("<Button-1>",bet1)
b_2.bind("<Button-1>",bet2)
b_3.bind("<Button-1>",bet3)
b_4.bind("<Button-1>",bet4)

root.configure(bg = "black")

root.mainloop()
