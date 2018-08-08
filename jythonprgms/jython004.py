file = JMenu("File")
msgbtn = JMenuItem("Message",actionPerformed = OnClick)
conbtn = JMenuItem("Message",actionPerformed = OnClick)
inputbtn = JMenuItem("Message",actionPerformed = OnClick)

file.add(msgbtn)
file.add(conbtn)
bar.add(file)

txt = JTextField(10)
frame.add(txt, BorderLayout.SOUTH)
frame.setVisible(True)

