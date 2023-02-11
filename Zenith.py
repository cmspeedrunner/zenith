import os
import webbrowser
import sys
import requests
import random
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from PIL import Image
import urllib.request
import matplotlib.image as mpimg
import matplotlib.animation as animation
import matplotlib.cm as cm
from matplotlib.collections import LineCollection
from matplotlib.ticker import MultipleLocator
import pyperclip
import pyttsx3
import colorama
colorama.init()
engine = pyttsx3.init()

####defining very important dict####
loa = {
"log": """what you might know as the print function, log will display whatever you want to log, make sure you dont use "" and instead you use '' when logging
EG: log['Hello World!']
EG: log[5*5+3-3/3]""",

"lg--": """will log something for a number of times
EG: lg--['Hello World!']<500>(DN: True)
the [] bracket denotes the value to be logging. The <> bracket denotes how many times you will be logging that value, the () bracket is essentially asking if you want to display the number""",

"var": """this will declare a string variable.
EG: var['x']<'Hello World'>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable
int variables are similar just with no quotes
EG: var['y']<500>
the [] brackets denote the variable name and the <> brackets denote the content inside the variable""",

"get": """send a http post request
EG: get['https://google.com']<text/html>""",

"rand": """this is the random number function, by default it goes from 0 to your number in range.
EG: rand[50]""",

"cdir": """this is the create directory function and will create a directory at the path specified
EG: cdir['C:/Users/User/Desktop/New Dir']""",

"rinr": """this is the random in range function, this allows you enter 2 arguments to randomise a number in the range of the 2 args you entered
EG: rinr[50]<100>""",

"wrto": """his is the write to function and allows you to write text into or over a file
EG: wrto[L:'C:/Users/User/Desktop/New Dir/My Text File.txt']<C:'Content goes here! I can put anything here!'>
The L: tag denotes Location and the C: tag denotes the Content within the file.""",

"ourl": """this is the open url function and will open
EG: ourl['https://google.com']""",

"pass": """this is the pass function and allows you to pass commands to the command line and allows you to control the system from Zenith, you can even run python in it!
EG: pass['shutdown /i']""",

"dfil": """this is the delete file function and allows you to delete any file
EG: dfil['C:/Users/User/Desktop/New Dir/My Text File.txt']""",

"ddir": """this is the delete directory function and allows you to delete any directory
EG: ddir['C:/Users/User/Desktop/New Dir']""",

"size": """this is the size function and allows you to view the memory contained in a string or int
EG: size['Hello World 2023!']""",

"vers": """this will display the version.
EG: vers""",

"zclr": """this is the zenith clear function, you may know it as the cls function.
EG: zclr""",

"up": """this will uppercase text.
EG: up['hello']""",

"low": """this will lowercase text.
EG: low['HELLO']""",

"tts": """this will speak out text using tts.
EG: tts['Hello Zenith!']""",

"pyth": """allows you to pass python lines through zenith
EG: pyth[print("Hello Zenith!")]
EG: pyth[os.system("shutdown /i")]""",

"u2i": """ allows you to convert a Url 2 (to) an Image
EG: pyth['https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg']<'Users/User/Desktop/obama.jpg'>
the first argument is the url, the second is the name and or location to save it to.""",

"html": """allows you to convert a url to pure html
EG: html['https://google.com']""",

"what": """print type of value
EG: what[True]""",

"2dln": """to do a 2d line graph plot.
EG: 2dln[1,2,3,4,5,6,7,9]
Arrays (which can be saved in variables) are interpreted into the graph here.""",

"3dsc": """to do a 3d scatter graph
EG: 3dsc[1,2,3,4,5,6,7,8,9]<1,2,3,4,5,6,7,8,9>(1,2,3,4,5,6,7,8,9)
the first [] bracket arg is the X pos, the second <> arg is the Y pos and the () arg is the Z pos. These arrays link up, make sure all 3 of these indexes have the same number of values in them, otherwise they cant marry or link the numbers together""",

"3dsf": """to do a 3d surface graph
EG: 3dcl[-5]<5.1>(0.2)
the [] bracket arg denotes the lowest point and the <> brackets denote the highest, the () brackets denotes the graphics, smaller float point = more polygons. (0 DOES NOT WORK, NEEDS TO BE FLOAT)""",

"3dcl": """to do a 3d coil graph
EG: 3dcl[0]<10>(6){2}""",

"2dsc": """ to do a 2d scatter graph
EG: 3dcl[1,2,3,4,5,6,7,8,9]<1,2,3,4,5,6,7,8,9>
the first [] bracket arg is the X pos, the second <> arg is the Y pos. These arrays link up, make sure all 3 of these indexes have the same number of values in them, otherwise they cant marry or link the numbers together""",

"2dsp": """show a 2d spectural map of any image on your computer
EG: 2dsp['Users/User/Desktop/obama.jpg']""",

"brcd": """render and create a barcode from binary
EG: brcd[ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1,]""",

"3dsp": """create a 3d spore growing animation
EG: 3dsp[50]<0.05>
the first [] bracket represents how long the spores will grow for, anything >200 will look wacky. the <> brackets represent the spore scale essentially, keep it at 0.05, it is reccomended.""",

"is": """give arguments with the is control flow.
EG: is[50==30]""",

"help": """literally the command your running lmao""",

}


loop = True
while loop == True:
    plt.rcParams["figure.autolayout"] = True
    s = input("ZNTH>>>")
    s2 = s.split('[')

    def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

    def find_between_r( s, first, last ):
        try:
            start = s.rindex( first ) + len( first )
            end = s.rindex( last, start )
            return s[start:end]
        except ValueError:
            return ""

    if "help" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        print("")
        print(loa[calc])
        print("")
    if "lg--" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        num = (eval(find_between( s, "<", ">" )))
        disp = (eval(find_between( s, "(DN:", ")" )))
        if disp == False:
            for i in range(num):
                print(calc)
        if disp == True:
            for i in range(num):
                print((calc),(" "),(i))
        print(calc)
    if "get" in s2: 
        url = (eval(find_between( s, "[", "]" )))
        payload = {(eval(find_between( s, "<", ">" )))}

        response = requests.get(url, params=payload)
        response_json = response.json()
        for i in response_json:
            print(i, "\n")
    if "html" in s2:
        url = (eval(find_between( s, "[", "]" )))
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()

        mystr = mybytes.decode("utf8")
        fp.close()
        pyperclip.copy(mystr)

        print(mystr)
        print("\n\nHTML+ COPIED TO CLIPBOARD (NOT THIS BIT)")
    if "u2i" in s2:
        url = (eval(find_between( s, "[", "]" )))
        name = (eval(find_between( s, "<", ">" )))
        urllib.request.urlretrieve(
         url,
         name)
  
        img = Image.open(name)
        img.show()
    if "log" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        print(calc)
    
    if "cdir" in s2:
        os.mkdir(eval(find_between( s, "[", "]" )))
    if "rand" in s2:
        main = int(eval(find_between( s, "[", "]" )))
        print(random.randint(0,main))
    if "rinr" in s2:
        main = int(eval(find_between( s, "[", "]" )))
        main2 = int(eval(find_between( s, "<", ">" )))
        print(random.randint(main,main2))
    if "wrto" in s2 and "[L:" in s2 and "[L:'" not in s2:
        location = (eval(find_between( s, "[L:'", "']" )))
        content = (eval(find_between( s, "<C:'", "'>" )))
        f = open(location, "a")
        f.write(content)
        f.close()
    if "wrto" in s2:
        location = (eval(find_between( s, "[L:", "]" )))
        content = (eval(find_between( s, "<C:", ">" )))
        f = open(location, "a")
        f.write(content)
        f.close()
    if "rule" in s2:
        print("""
A very important rule to note, if you a passing an argument and this argument is not a value but is a command (like log['hello']) you will not be able to do that, you cannot pass zenith commands/codelines through arguments, you can pass any data type though just not zenith commands. You can however pass some python commands through arguments, for example log[print("hello")] or var['random']<random.randint(0,10). I dont reccomend that you pass python commands through these but its just something to note. Its kinda like a backdoor.
        """)
    if "ourl" in s2:
        log = (eval(find_between( s, "[", "]" )))
        webbrowser.open_new(log)
    if "pass" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        os.system(calc)
    if "dfil" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        os.remove(calc)
    if "ddir" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        os.removedirs(calc)
    if "size" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        main = (sys.getsizeof(calc)," BITS")
        print(main)
    if "what" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        print(type(calc))
    if "var" in s2 and "<'" not in s2:
        input_name = find_between( s, "['", "']" ) 
        input_val = (eval(find_between( s, "<", ">" )))
        globals()[input_name] = input_val

    if "up" in s2:
        value = (eval(find_between( s, "[", "]" )))
        main = value.upper()
        print(main)
    if "low" in s2:
        value = (eval(find_between( s, "[", "]" )))
        main = value.lower()
        print(main)
    if "tts" in s2:
        value = (eval(find_between( s, "[", "]" )))
        engine.say(value)
        engine.runAndWait()
    if "var" in s2 and "<'" in s2:
        input_name = find_between( s, "['", "']" ) 
        input_val = (str(find_between( s, "<'", "'>" )))
        globals()[input_name] = input_val
    if "vers" in s2:
        github = 'https://github.com/cmspeedrunner/zenith'
        print("\nZenithScript Programming Language\nCmSpeedrunner2023\nOpen Source\nV/0.4\nhttps://github.com/cmspeedrunner/zenith")
    if "2dln" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        oppf = np.array(opp)
        opp2f = np.sort(oppf)
        plt.title("Line Graph")
        plt.plot(oppf, opp2f, color="red")
        plt.show()
    if "3dsc" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        opp2 = (eval(find_between( s, "<", ">" ))) 
        opp3 = (eval(find_between( s, "(", ")" ))) 

        fig = plt.figure(figsize = (10,10))
        ax = plt.axes(projection='3d')
        ax.grid()

        ax.scatter(opp, opp2, opp3, c = 'r', s = 50)
        ax.set_title('3D Scatter Plot')
        plt.show()
    if "3dcl" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        opp2 = (eval(find_between( s, "<", ">" ))) 
        opp3 = (eval(find_between( s, "(", ")" ))) 
        opp4 = (eval(find_between( s, "{", "}" )))
        fig = plt.figure(figsize = (8,8))
        ax = plt.axes(projection='3d')
        ax.grid()
        t = np.arange(opp, opp2*opp3, opp4)
        x = np.sin(t)
        y = np.cos(t)
        

        ax.plot3D(x, y, t)

        plt.show()
    if "3dsf" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        opp2 = (eval(find_between( s, "<", ">" ))) 
        opp3 = (eval(find_between( s, "(", ")" ))) 
        fig = plt.figure(figsize = (12,10))
        ax = plt.axes(projection='3d')

        x = np.arange(opp, opp2, opp3)
        y = np.arange(opp, opp2, opp3)

        X, Y = np.meshgrid(x, y)
        Z = np.sin(X)*np.cos(Y)

        surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.cividis)

        fig.colorbar(surf, shrink=0.5, aspect=8)
        plt.show()

    if "3dgr" in s2:
        fig = plt.figure(figsize = (12,10))
        ax = plt.axes(projection='3d')
        plt.show()
    if "2dsc" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        opp2 = (eval(find_between( s, "<", ">" )))
        x = np.array([opp])
        y = np.array([opp2])
        plt.scatter(x, y)
        plt.show()
    if "2dht" in s2:
        opp = (eval(find_between( s, "[", "]" ))) 
        fig = plt.figure(opp)
        img = mpimg.imread(opp)
        
        fig = fig.add_subplot(2, 2, 1)
        fig.imshow(img, cmap = "Blues")
        fig.axis('on')
        ax1 = plt.subplot(2, 2, 2)
        img = np.ravel(img)
        img = img[np.nonzero(img)]  # Ignore the background
        img = img / (2**16 - 1)  # Normalize
        ax1.hist(img, bins=100)
        ax1.xaxis.set_major_locator(MultipleLocator(0.4))
        ax1.minorticks_on()
        ax1.set_yticks([])
        ax1.set_xlabel('Intensity (a.u.)')
        ax1.set_ylabel('Density')
        plt.show()
    if "brcd" in s2:
        main = (eval(find_between( s, "[", "]" )))
        code = np.array([main])

        pixel_per_bar = 4
        dpi = 100

        fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
        ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
        ax.set_axis_off()
        ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
              interpolation='nearest')
        plt.show()
    if "3dsp" in s2:
        main = (eval(find_between( s, "[", "]" )))
        main2 = (eval(find_between( s, "<", ">" )))
        np.random.seed(19680801)
        def random_walk(num_steps, max_step=main2):
            start_pos = np.random.random(3)
            steps = np.random.uniform(-max_step, max_step, size=(num_steps, 3))
            walk = start_pos + np.cumsum(steps, axis=0)
            return walk
        def update_lines(num, walks, lines):
            for line, walk in zip(lines, walks):
                # NOTE: there is no .set_data() for 3 dim data...
                line.set_data(walk[:num, :2].T)
                line.set_3d_properties(walk[:num, 2])
            return lines
        num_steps = main
        walks = [random_walk(num_steps) for index in range(40)]
        fig = plt.figure()
        ax = fig.add_subplot(projection="3d")
        lines = [ax.plot([], [], [])[0] for _ in walks]
        ax.set(xlim3d=(0, 1), xlabel='X')
        ax.set(ylim3d=(0, 1), ylabel='Y')
        ax.set(zlim3d=(0, 1), zlabel='Z')
        ani = animation.FuncAnimation(
        fig, update_lines, num_steps, fargs=(walks, lines), interval=100)
        plt.show()
    if "zclr" in s2:
        os.system("cls")
    if "pyth" in s2:
        input_val = (eval(find_between( s, "[", "]" )))
        globals()[""] = input_val
    if "is" in s2:
        calc = (eval(find_between( s, "[", "]" )))
        mainy = print(calc)
    if "" in s2 and "exit" not in s2:
        continue
    
    if "exit" in s2:
        break
