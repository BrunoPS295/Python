# STYLE         TEXT       BACK 
# 0 None      30 White   40 White
# 1 Bold      31 Red     41 Red
# 4 Underline 32 Green   42 Green
# 7 Negative  33 Yellow  43 Yellow
#             34 Blue    44 Blue
#             35 Magenta 45 Magenta
#             36 Cyan    46 Cyan
#             37 Gray    47 Gray

import random
r = [0, 1, 4, 7]
style = r[random.randrange(0,4)]
text = random.randrange(30, 37)
back = random.randrange(40, 47)
print("\033[{};{};{}mStyle:{}\033[m".format(style, text, back,style))
print("\033[{};{};{}mText:{}\033[m".format(style, text, back,text))
print("\033[{};{};{}mBack:{}\033[m".format(style, text, back,back))