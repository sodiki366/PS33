class Tank:
    count = 0#общее колчтчество изготовленных танка
    SIZE = 100
    def __init__(self,canvas,x,y,model,ammo,speed):# init - инцилиатор
        self.canvas = canvas#холст
        Tank.count += 1
        self.model = model
        self.hp= 100
        self.xp = 0
        self.ammo = ammo
        self.fuel = 100
        self.speed = speed
        self.x = x
        self.y = y
        if self.x < 0:
           self.x = 0
        if self.y < 0:
            self.y = 0

        self.create()
    def fire(self):
        if self.ammo > 0:
            self.ammo -=1
            print('Стреляю')
    def forward(self):
        if self.fuel > 0:
            self.y += -self.speed
            self.fuel -= 1
            self.repaint()
    def backward(self):
        if self.fuel > 0:
            self.y += self.speed
            self.fuel -= 1
            self.repaint()
    def left(self):
        if self.fuel > 0:
            self.x += -self.speed
            self.fuel -= 1
            self.repaint()
    def right(self):
        if self.fuel > 0:
            self.x += self.speed
            self.fuel -= 1
            self.repaint()
    def create(self):
        self.id = self.canvas.create_rectangle(self.x,self.y,self.x+ Tank.SIZE,self.y+ Tank.SIZE,fill = 'red')
    def repaint(self):
        self.canvas.moveto(self.id, x = self.x , y = self.y)#передвижение танка по холсту

    def __str__(self):
        return(f'Модель:{self.model},Здоровье:{self.hp},Опыт:{self.xp},Пули:{self.ammo}'
              f'Координаты:({self.x} , {self.y})')