from mcturtle import mincraftturtle as t
from mcpi.minecraft import Minecraft
from mcpi import block
mc = Minecraft.create()
x,y,z= mc.player.getPos()

#mc.player.setPos(x,y+100,z)
mc.setBlocks(x+3,y+3,z+3,x+30,y+30,x+30, 46)
pos = mc.player.getPos()

s =t.MinecraftTurtle(mc,pos)
s.forward(15)
