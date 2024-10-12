from hitbox import Hitbox

hb1 = Hitbox(x=0,y=100,width=100,height=100)
hb2 = Hitbox(x=150,y=100,width=100,height=100)

print(f'верхняя граница hb1:{hb1.top},'
      f'верхняя граница hb2:{hb2.top}')
print(f'нижняя граница hb1:{hb1.bottom},'
      f'нижняя граница hb2:{hb2.bottom}')
print(f'левая граница hb1:{hb1.left},'
      f'левая граница hb2:{hb2.left}')
print(f'правая граница hb1:{hb1.right},'
      f'правая граница hb2:{hb2.right}')


intersection = hb1.intersects(hb2)
print(intersection)