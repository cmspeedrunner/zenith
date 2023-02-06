# Zip
Zip is a interpreted, one line, Command Line style programming language with very low level access to the system with easy, and readable syntax.

# Syntax

log - what you might know as the print function, log will display whatever you want to log, make sure you dont use "" and instead you use '' when logging<br>
EG: <b>log['Hello World!']<br></b>

log. - this will log a message but, as many times as you want, the "." denotes that it can be indefinite<br>
EG: <b>log.['Hello World!']<5><br></b>

calc - this is a simple calculate function<br>
EG: <b>calc[5*5+3-3/3]<br></b>

cdir - this is the create directory function and will create a directory at the path specified<br>
EG: <b>cdir['C:\Users\User\Desktop\New Dir']<br></b>

rand - this is the random number function, by default it goes from 0 to your number in range.<br>
EG: <b>rand[50]<br></b>

rinr - this is the random in range function, this allows you enter 2 arguments to randomise a number in the range of the 2 args you entered<br>
EG: <b>rand[50]<100><br></b>

wrto - this is the write to function and allows you to write text into or over a file<br>
EG: <b>wrto[L:'C:\Users\User\Desktop\New Dir\My Text File.txt']<C:'Content goes here! I can put anything here!'><br></b>
The L: tag denotes Location and the C: tag denotes the Content within the file.<br>

ourl - this is the open url function and will open <br>
EG: <b>ourl['https://google.com']<br></b>

pass - this is the pass function and allows you to pass commands to the command line and allows you to control the system from Zip, you can even run python in it!<br>
EG: <b>pass['shutdown /i']<br></b>
 
dfil - this is the delete file function and allows you to delete any file<br>
EG: <b>dfil['C:\Users\User\Desktop\New Dir\My Text File.txt']<br></b>
 
ddir - this is the delete directory function and allows you to delete any directory<br>
EG: <b>ddir['C:\Users\User\Desktop\New Dir']<br></b>
 
size - this is the size function and allows you to view the memory contained in a string or int<br>
EG: <b>size['Hello World 2023!']<br></b>
