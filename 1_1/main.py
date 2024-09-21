class Tank:
    def __init__(self,model,fuel,hp,ammo,x,y):
       self.model = model
       self.fuel = fuel
       self.hp=hp
       self.ammo = ammo
       self.x = x
       self.y = y

tank1 = Tank('T-34',100,100,50,0,0)
print(f'Танк 1: {tank1.model,}Топливо:{tank1.fuel},Здоровье:{tank1.hp},'
      f'Патроны:{tank1.ammo},Координаты:({tank1.x},{tank1.y})')