from javax.swing import JFrame, JButton, JTextField
from java.awt import FlowLayout
frame = JFrame("Hello!")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.setSize(200,200)
frame.setLayout(FlowLayout())

def clickhere(event):
	n1 = int(txt.getText())**2
	txt.setText(str(n1))
btn = JButton("Add",actionPerformed = clickhere)
txt = JTextField(10)
frame.add(txt)
frame.add(btn)
frame.setVisible(True)



