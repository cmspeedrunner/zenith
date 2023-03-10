![image](https://user-images.githubusercontent.com/109184310/218226338-9dab63e7-e3f3-40c9-8fc6-abeb5bab4120.png)

# Zenith
## Zenith is a interpreted, one line, Command Line style programming language with high level access to commands to the system, control flow editing, variables, calculations, immense data analysis, conversion and web interaction with interesting, and semi-readable syntax.

# Syntax

`log` - what you might know as the print function, log will display whatever you want to log, make sure you dont use "" and instead you use '' when logging<br>
EG: <b>log['Hello World!']<br></b>
EG: <b>log[5*5+3-3/3]<br></b>

`lg--` - will log something for a number of times<br>
EG: <b>lg--['Hello World!']<500>(DN: True)<br></b>
the [] bracket denotes the value to be logging. The <> bracket denotes how many times you will be logging that value, the () bracket is essentially asking if you want to display the number, DN meaning Display Number, if it is set to true then your output would look like this:<br>
Hello World! 0<br>
Hello World! 1<br>
Hello World! 2<br>
ect...<br>

`get` - send a http post request<br>
EG: <b>get['https://google.com']<text/html><br></b>

`help` - get help on any command<br>
EG: <b>help['log']<text/html><br></b>

`cdir` - this is the create directory function and will create a directory at the path specified<br>
EG: <b>cdir['C:\Users\User\Desktop\New Dir']<br></b>

`rand` - this is the random number function, by default it goes from 0 to your number in range.<br>
EG: <b>rand[50]<br></b>

`rinr` - this is the random in range function, this allows you enter 2 arguments to randomise a number in the range of the 2 args you entered<br>
EG: <b>rinr[50]<100><br></b>

`wrto` - this is the write to function and allows you to write text into or over a file<br>
EG: <b>wrto[L:'C:\Users\User\Desktop\New Dir\My Text File.txt']<C:'Content goes here! I can put anything here!'><br></b>
The L: tag denotes Location and the C: tag denotes the Content within the file.<br>

`ourl` - this is the open url function and will open <br>
EG: <b>ourl['https://google.com']<br></b>

`pass` - this is the pass function and allows you to pass commands to the command line and allows you to control the system from Zenith, you can even run python in it!<br>
EG: <b>pass['shutdown /i']<br></b>
 
`dfil` - this is the delete file function and allows you to delete any file<br>
EG: <b>dfil['C:\Users\User\Desktop\New Dir\My Text File.txt']<br></b>
 
`ddir` - this is the delete directory function and allows you to delete any directory<br>
EG: <b>ddir['C:\Users\User\Desktop\New Dir']<br></b>
 
`size` - this is the size function and allows you to view the memory contained in a string or int<br>
EG: <b>size['Hello World 2023!']<br></b>

`vers` - this will display the version.<br>
EG: <b>vers<br></b>

`zclr` - this is the zenith clear function, you may know it as the cls function.<br>
EG: <b>zclr<br></b>

`up` - this will uppercase text.<br>
EG: <b>up['hello']<br></b>

`low` - this will lowercase text.<br>
EG: <b>low['HELLO']<br></b>
 
`tts` - this will speak out text using tts.<br>
EG: <b>tts['Hello Zenith!']<br></b>
 
`pyth` - allows you to pass python lines through zenith<br>
EG: <b>pyth[print("Hello Zenith!")]</b><br>
EG: <b>pyth[os.system("shutdown /i")]</b><br>
This is a very powerful pass command and you can do the same thing and change the zenith inbuilt variables with the var command<br>
EG: <b>var['Loop']<.False></b> (please ignore the full stop/period markdown wont let me encase this value in angle brackets.<br>
This will break the loop, why am i telling you this? Idk, it gives you more control and i think thats good.<br>

`u2i` - allows you to convert a Url 2 (to) an Image<br>
EG: <b>pyth['https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg']<'Users/User/Desktop/obama.jpg'></b><br>
the first argument is the url, the second is the name and or location to save it to.<br>
 
`html` - allows you to convert a url to pure html<br>
EG: <b>html['https://google.com']</b><br>
 
`what` - print type of value<br>
EG: <b>what[True]</b><br>
RESULT: <b>class: bool</b><br>
EG: <b>what['Yo']</b><br>
RESULT: <b>class: str</b><br>
EG: <b>what[9.9]</b><br>
RESULT: <b>class: float</b><br>
EG: <b>what[1]</b><br>
RESULT: <b>class: int</b><br>
EG: <b>what['Yo',9.9,1,True,]</b><br>
RESULT: <b>class: tuple</b><br>

# Variables
`var` - this will declare a string variable.<br>
EG: <b>var['x']<'Hello World'></b><br>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable<br>
int variables are similar just with no quotes<br>
EG: <b>var['y']<500></b><br>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable<br>
 
 
`log` - can also calculate variables<br>
EG: <b>log[x+y-z*w]</b><br>
providing that you have set up your variables with values, you can concatonate strings with other strings or do calculations<br>
 

# Graphing and plotting (EXPERIMENTAL)
`2dln` - to do a 2d line graph plot.<br>
EG: <b>2dln[1,2,3,4,5,6,7,9]</b><br>
Arrays (which can be saved in variables) are interpreted into the graph here.

`3dsc` - to do a 3d scatter graph<br>
EG: <b>3dsc[1,2,3,4,5,6,7,8,9]<1,2,3,4,5,6,7,8,9>(1,2,3,4,5,6,7,8,9)</b><br>
the first [] bracket arg is the X pos, the second <> arg is the Y pos and the () arg is the Z pos. These arrays link up, make sure all 3 of these indexes have the same number of values in them, otherwise they cant marry or link the numbers together<br>

`3dsf` - to do a 3d coil graph<br>
EG: <b>3dcl[0]<10>(6){2}</b><br>

`3dcl` - to do a 3d surface graph<br>
EG: <b>3dcl[-5]<5.1>(0.2)</b><br>
the [] bracket arg denotes the lowest point and the <> brackets denote the highest, the () brackets denotes the graphics, smaller float point = more polygons. (0 DOES NOT WORK, NEEDS TO BE FLOAT)

`2dsc` - to do a 2d scatter graph<br>
EG: <b>3dcl[1,2,3,4,5,6,7,8,9]<1,2,3,4,5,6,7,8,9></b><br>
the first [] bracket arg is the X pos, the second <> arg is the Y pos. These arrays link up, make sure all 3 of these indexes have the same number of values in them, otherwise they cant marry or link the numbers together<br>

`2dsp` - show a 2d spectural map of any image on your computer<br>
EG: <b>2dsp['Users/User/Desktop/obama.jpg']</b><br>

`brcd` - render and create a barcode from binary<br>
EG: <b>brcd[ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,]</b><br>

`3dsp` - create a 3d spore growing animation<br>
EG: <b>3dsp[50]<0.05></b><br>
the first [] bracket represents how long the spores will grow for, anything >200 will look wacky. the <> brackets represent the spore scale essentially, keep it at 0.05, it is reccomended.
# Control Flow
`is` - give arguments with the is control flow. <br>
EG: <b>is[50==30]</b><br>
### Example:
### ![image](https://user-images.githubusercontent.com/109184310/218225334-6ae1fb3b-75cd-41fd-9e4a-f2180b9c6830.png)

# Important rules to note
A very important rule to note, if you a passing an argument and this argument is not a value but is a command (like `log[rinr[0]<10>]`) you will not be able to do that, you cannot pass zenith commands/codelines through arguments, you can pass any data type, for example `var['a']<True>` though just not zenith commands. You can however pass some python commands through arguments, for example `log[print("hello")]` or `var['random']<random.randint(0,10)>`. I dont reccomend that you pass python commands through these but its just something to note. Its kinda like a backdoor.

