from javax.swing import * #JFrame, Jlabel, JButton, JTable, JPanel
from java.awt import *


def clickhere1(event):
	frame1 = JFrame("Page 1")
	frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frame1.setLocation(200,200)
	frame1.setSize(300,200)
	frame1.setVisible(True)
	btn = JButton("Page 2", actionPerformed = clickhere2)
	frame1.add(btn)
	frame1.setVisible(True)

def clickhere2(event):
	frame2 = JFrame("Page 2")
	frame2.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frame2.setLocation(200,200)
	frame2.setSize(300,200)
	frame2.setVisible(True)
	btn = JButton("Page 1", actionPerformed = clickhere1)
	frame2.add(btn)
	frame2.setVisible(True)
	frame1.setVisible(False)
clickhere1(event)
	

	

