import sys
import OpenGL
import math
from numpy import *

from OpenGL.GL import *     
from OpenGL.GLU import *    
from OpenGL.GLUT import *

Angle = 0
Incr = 1
EyeY= 150
WingAngle=0
WingIncr= 5
WingFlag=0
key1=0
lightX=0
lightY=120
lightZ=200
wire_frame=False
flat_shading=False
enable_lighting=True
Kar=0.5
Ksr=0.5
Kdr=0.5
u_min=--1
u_max=1
v_min=-1
v_max=1
front=1
back=1000
Kar=0.5
Kdr=0.5
Ksr=0.5
CenterX=0

# Function to create ctpe array
def vec(*args):
      return (GLfloat * len(args))(*args)

# Function to initialize the bird object used in the animation
def create_bird():
      global WingAngle
      global WingIncr
      global WingFlag
      glNewList(1,GL_COMPILE)

      glTranslatef(0, 0, 100)
      glTranslatef(0, -10, 0)
      glPushMatrix()
      glColor3f(1.0,0, 0)
      glutSolidCylinder(5,20,100,100)
      glPopMatrix()

      glPushMatrix()
      glRotated(WingAngle,0,0,1)
      glBegin(GL_TRIANGLES)
      glColor3f(0,0,1)
      glVertex3f(2.5,0,2.5)
      glVertex3f(2.5,0,12.5)
      glVertex3f(20,0,0)
      glEnd()
      glPopMatrix()
      glPushMatrix()
      glTranslate(0, 0, 2.5)
      glRotated(-WingAngle, 0, 0, 1)
      glBegin(GL_TRIANGLES)
      glColor3f(0, 0, 1)
      glVertex3f(-2.5, 0, 2.5)
      glVertex3f(-2.5, 0, 12.5)
      glVertex3f(-20, 0, 0)
      glEnd()
      glPopMatrix()
      glPushMatrix()
      glTranslatef(0, 0, -5)
      glColor3f(0,1,0)
      glutSolidSphere(5,100,100)
      glPopMatrix()

      glEndList()

      if WingAngle==0:
            WingAngle=45

      elif WingAngle==45:
            WingAngle=0

# Function to initialize the flag object in the animation
def create_flag():
      glNewList(2,GL_COMPILE)
      glTranslatef(0,-60,0)
      glColor3f(0, 0, 0)
      glRectf(0, 90, 30, 120)
      glRotatef(-90,1,0,0)
      glColor3f(0.5, 0.35, 0.05)
      glutSolidCylinder(2, 120, 200, 200)
      glColor3f(1.0, 1.0, 1.0)

      glEndList()

# Function to set the window settings for the animation
def display():
      global Angle
      global Incr
      global EyeY
      global CenterX
      global lightX
      global lightY
      global lightZ
      global wire_frame
      global flat_shading
      global enable_lighting
      global Kar
      global Kdr
      global Ksr

      w=glutGet(GLUT_WINDOW_WIDTH)
      h=glutGet(GLUT_WINDOW_HEIGHT)

      glEnable(GL_SCISSOR_TEST)
      glClearColor(0.4,0.4,0.6,0)
      glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glFrustum(-1,1,-1,1,1,1000)
      gluLookAt(0,EyeY,150,CenterX,0,0,0,1,0)
      glMatrixMode(GL_MODELVIEW)
      glCallList(1) 
      glPushMatrix()
      glLoadIdentity()
      glEnable(GL_DEPTH_TEST)
      if enable_lighting:
            glEnable(GL_LIGHTING)
      else:
            glDisable(GL_LIGHTING)
      if wire_frame:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
      else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            glEnable(GL_LIGHT0)
            glLightfv(GL_LIGHT0, GL_POSITION, vec(0, 120, 200, 0))
            glLightfv(GL_LIGHT0, GL_SPECULAR, vec(Ksr, 0.5, 0.5, 0.5))
            glLightfv(GL_LIGHT0, GL_DIFFUSE, vec(Kdr, 0.5, 0.5, 0.5))
            glLightfv(GL_LIGHT0, GL_AMBIENT, vec(Kar, 0.5, 0.5, 0.5))

            glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, vec(0.5, 0, 0.3, 1))
            glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, vec(1, 1, 1, 1))
            glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 50)
            glEnable(GL_NORMALIZE)
            glShadeModel(GL_SMOOTH)
      glCallList(2)
      glPopMatrix()

      glFlush()
      glutSwapBuffers()                 
      
      glLoadIdentity()
      glRotated(Angle,0,1,0)
      Angle = Angle + Incr


# Input handler for the animation
def keyHandler(Key, MouseX, MouseY):
      global Incr
      global key1
      global Kar
      global Kdr
      global Ksr
      if Key == b'F' :
            print ("Speeding Up")
            Incr = Incr + 1
      elif Key == b'f' :
            if Incr ==0:
                  print ("Stopped")
            else:
                  print ("Slowing Down")
                  Incr = Incr - 0.5

      elif Key == b'a' :
            if (Kar > 0):
                  Kar = Kar - 0.5
                  print ("Kar decrease")
                  print(Kar)
            else:
                  Kar = Kar
      elif Key == b'A':
            Kar=Kar+0.5
            print ("Kar increase")
            print(Kar)

      elif Key == b'd':
            if(Kdr>0):
                  Kdr=Kdr-0.5
                  print ("Kdr decrease")
                  print(Kdr)
            else:
                  Kdr=Kdr
      elif Key == b'D':
            Kdr=Kdr+0.5
            print ("Kdr increase")
            print(Kdr)
      elif Key == b's':
            if (Ksr > 0):
                  Ksr = Ksr - 0.5
                  print ("Ksr decrease")
                  print(Ksr)
            else:
                  Kdr = Kdr
      elif Key == b'S':
            Ksr = Ksr + 0.5
            print ("Ksr increase")
            print(Ksr)


      elif Key == b'q' or Key == b'Q':
            print ("Bye")
            sys.exit()
      elif Key == b'w':
            if(key1==1):
                  print ("Stop Waving")
                  key1=0
            elif(key1==0):
                  print("Start Waving")
                  key1=1
      else:
            print(("Invalid Key ",Key))

# Additional input handling for viewing angles
def handleArrowPress(key, MouseX, MouseY):
      global EyeY
      global CenterX
      if key == GLUT_KEY_LEFT:
          CenterX=CenterX-5
          print("clockwise rotation")

      if key == GLUT_KEY_RIGHT:
            CenterX = CenterX +5
            print("counter-clockwise rotation")
      if key == GLUT_KEY_UP:
          EyeY+= 5
          print("eye up")
      if key == GLUT_KEY_DOWN:
          EyeY -= 5
          print("eye down")


def timer(dummy):
      display()
      create_bird()
      glutTimerFunc(30,timer,0)

def reshape(w, h):
      print(("Width=",w,"Height=",h))

def main():
      glutInit(sys.argv)
      glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
      glutInitWindowSize(800, 500)
      glutInitWindowPosition(100, 100)
      glutCreateWindow(b"PyOpenGL Demo")
      glClearColor(1,1,0,0)
      glPolygonMode(GL_FRONT_AND_BACK,GL_FILL)
      glEnable(GL_DEPTH_TEST)
      glDepthFunc(GL_LESS);

      glutDisplayFunc(display)
      glutKeyboardFunc(keyHandler)
      glutSpecialFunc(handleArrowPress)
      glutTimerFunc(300,timer,0)
      glutReshapeFunc(reshape)
      glMatrixMode(GL_PROJECTION)
      glLoadIdentity()
      glMatrixMode(GL_MODELVIEW)
      create_bird()
      create_flag()
      glutMainLoop()

if __name__ == "__main__":
      main()

