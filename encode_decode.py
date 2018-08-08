import base64
import sys

inputstr=raw_input()
encoded = base64.b64encode(inputstr)
print "encoded stream: ",encoded


decoded = base64.b64decode(encoded)
print "decoded str of above encoded code: ",decoded

