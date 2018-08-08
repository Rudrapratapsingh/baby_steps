from javax.swing import JFrame
from javax.swing import JLabel
from javax.swing import JTextField
from javax.swing import JButton
from java.awt import FlowLayout

frame = JFrame("Hello")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(200,200)
frame.setSize(600,600)
frame.setLayout(FlowLayout())

def clickhere(event):
	n1 = int(txt1.getText())
	n2 = int(txt2.getText())
	s = n1 + n2
	txt3.setText(str(s))
	
lbl1 = JLabel("Phy")
lbl1.setBounds(60,0,50,50)

txt1 = JTextField(10)
txt1.setBounds(200,0,50,50)

lbl2 = JLabel("Math")
lbl2.setBounds(60,100,50,50)

txt2 = JTextField(10)
txt2.setBounds(200,100,50,50)

lbl3 = JLabel("total")
lbl3.setBounds(60,200,50,50)

txt3 = JTextField(10)
txt3.setBounds(200,200,50,50)

btn = JButton("Add", actionPerformed = clickhere)
btn.setBounds(60,300,50,50)

frame.add(lbl1)
frame.add(txt1)
frame.add(lbl2)
frame.add(txt2)
frame.add(btn)
frame.add(lbl3)
frame.add(txt3)

frame.setVisible(True)
