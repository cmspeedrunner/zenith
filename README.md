# Zenith
Zenith is a interpreted, one line, Command Line style programming language with very low level access to the system with easy, and readable syntax.

# Syntax

log - what you might know as the print function, log will display whatever you want to log, make sure you dont use "" and instead you use '' when logging<br>
EG: <b>log['Hello World!']<br></b>
EG: <b>log[5*5+3-3/3]<br></b>

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

pass - this is the pass function and allows you to pass commands to the command line and allows you to control the system from Zenith, you can even run python in it!<br>
EG: <b>pass['shutdown /i']<br></b>
 
dfil - this is the delete file function and allows you to delete any file<br>
EG: <b>dfil['C:\Users\User\Desktop\New Dir\My Text File.txt']<br></b>
 
ddir - this is the delete directory function and allows you to delete any directory<br>
EG: <b>ddir['C:\Users\User\Desktop\New Dir']<br></b>
 
size - this is the size function and allows you to view the memory contained in a string or int<br>
EG: <b>size['Hello World 2023!']<br></b>

vers - this will display the version.
EG: <b>vers<br></b>
 
# Variables
var - this will declare a string variable.<br>
EG: <b>var['x']<'Hello World'></b><br>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable<br>
int variables are similar just with no quotes<br>
EG: <b>var['y']<500></b><br>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable<br>
 
 
log - can also calculate variables<br>
EG: <b>log[x+y-z*w]</b><br>
providing that you have set up your variables with values, you can concatonate strings with other strings or do calculations<br>

# Graphing and plotting (EXPERIMENTAL)
2dln - to do a 2d line graph plot.<br>
EG: <b>2dln[1,2,3,4,5,6,7,9]</b><br>
Arrays (which can be saved in variables) are interpreted into the graph here.

3dsc - to do a 3d scatter graph<br>
EG: <b>3dsc[1,2,3,4,5,6,7,8,9]<1,2,3,4,5,6,7,8,9>(1,2,3,4,5,6,7,8,9)</b><br>
the first [] bracket arg is the X pos, the second <> arg is the Y pos and the () arg is the Z pos. These arrays link up, make sure all 3 of these indexes have the same number of values in them, otherwise they cant marry or link the numbers together<br>

3dcl - to do a 3d coil graph<br>
EG: <b>3dcl[0]<10>(6){2}</b><br>

3dcl - to do a 3d surface graph<br>
EG: <b>3dcl[-5]<5.1>(0.2)</b><br>
the [] bracket arg denotes the lowest point and the <> brackets denote the highest, the () brackets denote the Z occurence




