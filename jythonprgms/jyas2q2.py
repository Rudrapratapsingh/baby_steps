from javax.swing import JFrame, JTextField, JLabel, JButton, JTable, JPanel
from java.awt import FlowLayout

	
def clickhere(event):
	frame1 = JFrame("Marksheet with Result")
	frame1.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
	frame1.setLocation(200,200)
	frame1.setSize(300,120)
	frame1.setVisible(True)
	frame1.setLayout(FlowLayout())

	lbl1 = JLabel("Name: ")
	lbl1.setBounds(60,0,40,20)
	txt1 = JTextField(10)
	txt1.setBounds(120,0,40,20)

	lbl2 = JLabel("Class: ")
	lbl2.setBounds(60,40,40,20)
	txt2 = JTextField(10)
	txt2.setBounds(120,40,40,20)

	lbl3 = JLabel("Subject1: ")	
	lbl3.setBounds(60,80,40,20)
	txt3 = JTextField(10)
	txt3.setBounds(120,80,40,20)

	lbl4 = JLabel("Subject2: ")
	lbl4.setBounds(60,80,40,20)
	txt4 = JTextField(10)
	txt4.setBounds(120,80,40,20)

	lbl5 = JLabel("Subject3: ")
	lbl5.setBounds(60,80,40,20)
	txt5 = JTextField(10)
	txt5.setBounds(120,80,40,20)

	lbl6 = JLabel("Subject4: ")
	lbl6.setBounds(60,80,40,20)
	txt6 = JTextField(10)
	txt6.setBounds(120,80,40,20)

	lbl7 = JLabel("Subject5: ")
	lbl7.setBounds(60,80,40,20)
	txt7 = JTextField(10)
	txt7.setBounds(120,80,40,20)

	lbl8 = JLabel("Result: ")
	lbl8.setBounds(60,80,40,20)
	txt8 = JTextField(10)
	txt8.setBounds(120,80,40,20)

	n1 = int(txt3.getText())
	n2 = int(txt4.getText())
	n3 = int(txt5.getText())
	n4 = int(txt6.getText())
	n5 = int(txt7.getText())
	n6 = n1 + n2 + n3 + n4 + n5
		
	txt8.setText(str(n6))
	
	frame1.add(lbl1)
	frame1.add(txt1)
	frame1.add(lbl2)
	frame1.add(txt2)
	frame1.add(lbl3)
	frame1.add(txt3)
	frame1.add(lbl4)
	frame1.add(txt4)
	frame1.add(lbl5)
	frame1.add(txt5)
	frame1.add(btn) #
	frame1.add(lbl6)
	frame1.add(txt6)
	frame1.add(lbl7)
	frame1.add(txt7)
	frame1.add(txt8)
	frame1.setVisible(True)


frame = JFrame("Marksheet")
frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
frame.setLocation(200,200)
frame.setSize(300,200)
frame.setVisible(True)
frame.setLayout(FlowLayout())

lbl1 = JLabel("Name: ")
lbl1.setBounds(60,0,40,20)
txt1 = JTextField(10)
txt1.setBounds(120,0,40,20)

lbl2 = JLabel("Class: ")
lbl2.setBounds(60,40,40,20)
txt2 = JTextField(10)
txt2.setBounds(120,40,40,20)

lbl3 = JLabel("Subject1: ")
lbl3.setBounds(60,80,40,20)
txt3 = JTextField(10)
txt3.setBounds(120,80,40,20)

lbl4 = JLabel("Subject2: ")
lbl4.setBounds(60,80,40,20)
txt4 = JTextField(10)
txt4.setBounds(120,80,40,20)

lbl5 = JLabel("Subject3: ")
lbl5.setBounds(60,80,40,20)
txt5 = JTextField(10)
txt5.setBounds(120,80,40,20)

lbl6 = JLabel("Subject4: ")
lbl6.setBounds(60,80,40,20)
txt6 = JTextField(10)
txt6.setBounds(120,80,40,20)

lbl7 = JLabel("Subject5: ")
lbl7.setBounds(60,80,40,20)
txt7 = JTextField(10)
txt7.setBounds(120,80,40,20)
	
btn = JButton("Generate Result", actionPerformed = clickhere)
btn.setBounds(120,60,40,40)

frame.add(lbl1)
frame.add(txt1)
frame.add(lbl2)
frame.add(txt2)
frame.add(lbl3)
frame.add(txt3)
frame.add(lbl4)
frame.add(txt4)
frame.add(lbl5)
frame.add(txt5)
frame.add(btn)
frame.add(lbl6)
frame.add(txt6)
frame.add(lbl7)
frame.add(txt7)
frame.setVisible(True)
frame1.setVisible(False)
