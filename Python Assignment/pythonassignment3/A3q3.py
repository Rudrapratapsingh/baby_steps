dict = {'a':'B','b':'C','c':'D','d':'E','e':'F','f':'G','g':'H','h':'I','i':'J','j':'K','k':'L','l':'M','m':'N','n':'O','o':'P','p':'Q','q':'R','r':'S','s':'T','t':'U','u':'V','v':'W','w':'X','x':'Y','y':'Z','z':'A','A':'b','B':'c','C':'d','D':'e','E':'f','F':'g','G':'h','H':'i','I':'j','J':'k','K':'l','L':'m','M':'n','N':'o','O':'p','P':'q','Q':'r','R':'s','S':'t','T':'u','U':'v','V':'w','W':'x','X':'y','Y':'z','Z':'a','1':'2','2':'3','3':'4','4':'5','5':'6','6':'7','7':'8','8':'9','9':'0','0':'1'}

string = raw_input("Enter any string: ")
list = []
for i in string:
	x = dict.has_key(i);
	if x == True:
		a = dict.get(i);
		list.append(a);
	elif i == ' ':
		b = ' ';
		list.append(b);
s = ''.join(list);
print s
		 
