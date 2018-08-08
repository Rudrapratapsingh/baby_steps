from javax.swing import JFrame
from javax.swing import JButton
frame =  JFrame("Hello")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

frame.setLocation(100,100)
frame.setSize(300,200)

def clickhere(event):
	print "Clicked"

btn = JButton("Add",actionPerformed = clickhere)
frame.add(btn)
frame.setVisible(True)


