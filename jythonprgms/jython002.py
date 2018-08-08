from javax.swing import * #JFrame, Jlabel, JButton, JTable, JPanel
from java.awt import FlowLayout

frame = JFrame("JMenuBar Example:")
frame = setDafaultCloseOperationJFrame.EXIT_ON_CLOSE)
frame.setLocation(100,100)
frame.set(400,300)
frame.setLayout(BorderLayout())

def OnClick(event)
	txt.text = event.getActionCommand()

bar = JMenuBar()
frame.setJMenuBar(bar)

file = JMenu("File")
newfile = JMenuItem("New" ,actionPerformed = OnCLick)
openfile = JMenuItem("Open" ,actionPerformed = OnClick)
savefile = JMenuItem("Save" ,actionPerformed = OnClick)

file.add(newfile)
file.add(openfile)
file.add(savefile)
bar.add(file)

txt = JTextField(10)
frame.add(txt, BorderLayout SOUTH)
frame.setVisible(True)


