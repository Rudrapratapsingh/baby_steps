from javax.swing import * #JFrame, Jlabel, JButton, JTable, JPanel
from java.awt import FlowLayout

frame = Jframe("Jython001")
frame.setsize(250,200)
panel = JPanel()
panel.setLayout(BoxLayout(panel,BoxLayout,Y_AXIS))
frame.add(panel)
lbl = Jlabel("Select Gender")
lbl1 = Jlabel("Gender selection:-")

def onCheck(event):
	lbl1.txt = ""
	if rb1.isSelected():
		lb1.txt = lbl1.text+"gender selection: male"
	else:
		lbl1.text = lbl1.txt+"gender selection: female"

rb1 = JRadioButton("Male", True, actionPerformed = OnCheck)
rb2 = JRadioButton("Female", actionPerformed = OnCheck)

grp = ButtonGroup()
grp.add(rb1)
grp.add(rb2)

panel.add(Box.createVerticalGive())
panel.add(lbl)
panel.add(rb1)
panel.add(rb2)
panel.add(Box,createRigidArea(Dimension(0,25)))
panel.add(lbl1)

frame.setVisible(True)
