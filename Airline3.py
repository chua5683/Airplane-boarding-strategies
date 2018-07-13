import random
import numpy
#personal_space=1.2
#ctpp=2
#space_needed=1
#availble_seats=[[(i+1)*20,1] for i in range(30)]+[[(i+1)*20,2] for i in range(30)]+[[(i+1)*20,3] for i in range(30)]+[[(i+1)*20,4] for i in range(30)]+[[(i+1)*20,5] for i in range(30)]+[[(i+1)*20,6] for i in range(30)]
availble_seats=[[i,0] for i in range(30)]+[[i,1] for i in range(30)]+[[i,2] for i in range(30)]+[[i,3] for i in range(30)]+[[i,4] for i in range(30)]+[[i,5] for i in range(30)]
random.shuffle(availble_seats)


#availble_seats=[[(i+1)*20,1] for i in range(30)]+[[(i+1)*20,2] for i in range(30)]+[[(i+1)*20,3] for i in range(30)]+[[(i+1)*20,-1] for i in range(30)]+[[(i+1)*20,-2] for i in range(30)]+[[(i+1)*20,-3] for i in range(30)]
#random.shuffle(availble_seats)
def board(seatList,step,personal_space,ctpp,space_needed,speedList,bagList):
    global matrix
    w=max([x[0] for x in seatList])+1
    h=max([x[1] for x in seatList])+1
    matrix= [[0 for x in range(w)] for y in range(h)] 
    peopleList=[]
    for i in range(len(seatList)):
         #this is random seating
        peopleList.append(person(0-i, speedList[i], seatList[i],bagList[i]))
    t=0
    while sum([not(i.seated) for i in peopleList])>0: #we board until everyone is seated
        t+=step #step the time
        for k in range(len(peopleList)): #go through each person in the list
            peopleList[k].move(peopleList,k,step,space_needed,personal_space,ctpp) #and do a "Move" (which might actually mean don't go anywhere)
    return t

def someone_there(pos,peopleList,personal_space):
    for i in peopleList:
        if pos>i.xpos-personal_space and not(i.seated): #if there is no one there or there is someone there but they are already seated
            return True
    return False
'''
def makecPeople(n): #this should make a list of people with all the attributes described above
    peopleList=[]
    availble_seats=list(range(n))
    for i in range(n):
        random.shuffle(availble_seats)
        peopleList.append(personc(0-i, 45 , [(1+availble_seats[i])*15,1],10))
    return peopleList
'''
class person:
    def __init__(self, xpos,speed, seat, bagspeed):#first initallize all attributes of the person        
        self.xpos=xpos
        self.speed=speed
        self.seat=seat
        self.bagspeed=bagspeed
        self.loading=False #when you enter you are not loading yet
        self.climbing=False
        self.climbtime=0
        self.seated=False #and you are not seated yet
        self.wait=0 #this will count bag loading time
    def move(self,peopleList,index,step,space_needed,personal_space,ctpp): #Here we define the rules of moving
        split=int((len(matrix)+1)/2)
        if not(self.seated):
            newpos=self.xpos+self.speed*step #if they move, this is where they end up
            if self.loading: #if you are in a loading stage :
                self.wait=self.wait+step #you're wait counts
                if self.wait>=self.bagspeed: #when you finish waiting :
                    if self.climbing==False:
                        if self.seat[1]<split:
                            ppr=sum(numpy.array(matrix)[self.seat[1]+1:split,self.seat[0]])
                        else:
                            ppr=sum(numpy.array(matrix)[split:self.seat[1],self.seat[0]])
                        if ppr > 0:
                            self.climbing=True
                            self.climbtot=ppr*ctpp

                        else:
                            self.seated=True #you get seated
                            matrix[self.seat[1]][self.seat[0]]=1
                            if self.seat[1]<split:
                                j=0
                            else:
                                j=1
                    else:
                        self.climbtime+=step
                        if self.climbtime>=self.climbtot:
                            matrix[self.seat[1]][self.seat[0]]=1
                            self.seated=True #you get seated
                            if self.seat[1]<split:
                                j=0
                            else:
                                j=1
            else:
                if self.seat[0]-space_needed-self.xpos<.001:
                    if not(someone_there(self.seat[0],peopleList[:index],personal_space)):  
                        self.loading=True
                else:
                    if not(someone_there(newpos,peopleList[:index],personal_space)): #if there is no one in front of you :
                        self.xpos=newpos #move forward

#board(availble_seats,.2)

