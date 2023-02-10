import os
import webbrowser
import sys
import random
import keyboard
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
loop = True
while loop == True:
    plt.rcParams["figure.autolayout"] = True
    s = input("ZTH>>>")
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
    
    
    if "log" in s:
        calc = (eval(find_between( s, "[", "]" )))
        print(calc)

    if "cdir" in s:
        os.mkdir(eval(find_between( s, "[", "]" )))
    if "rand" in s:
        main = int(eval(find_between( s, "[", "]" )))
        print(random.randint(0,main))
    if "rinr" in s:
        main = int(eval(find_between( s, "[", "]" )))
        main2 = int(eval(find_between( s, "<", ">" )))
        print(random.randint(main,main2))
    if "wrto" in s and "[L:" in s and "[L:'" not in s:
        location = (eval(find_between( s, "[L:'", "']" )))
        content = (eval(find_between( s, "<C:'", "'>" )))
        f = open(location, "a")
        f.write(content)
        f.close()
    if "wrto" in s:
        location = (eval(find_between( s, "[L:", "]" )))
        content = (eval(find_between( s, "<C:", ">" )))
        f = open(location, "a")
        f.write(content)
        f.close()
    if "ourl" in s:
        log = (eval(find_between( s, "[", "]" )))
        webbrowser.open_new(log)
    if "pass" in s:
        calc = (eval(find_between( s, "[", "]" )))
        os.system(calc)
    if "dfil" in s:
        calc = (eval(find_between( s, "[", "]" )))
        os.remove(calc)
    if "ddir" in s:
        calc = (eval(find_between( s, "[", "]" )))
        os.removedirs(calc)
    if "size" in s:
        calc = (eval(find_between( s, "[", "]" )))
        main = (sys.getsizeof(calc)," BITS")
        print(main)
        print(len(find_between( s, "[", "]" ))," BYTES")
    if "var" in s and "<'" not in s:
        input_name = find_between( s, "['", "']" ) 
        input_val = (eval(find_between( s, "<", ">" )))
        globals()[input_name] = input_val
    if "var" in s and "<'" in s:
        input_name = find_between( s, "['", "']" ) 
        input_val = (str(find_between( s, "<'", "'>" )))
        globals()[input_name] = input_val
    if "vers" in s:
        github = 'https://github.com/cmspeedrunner/zenith'
        print("\nZenithScript Programming Language\nCmSpeedrunner2023\nOpen Source\nV/0.3\nhttps://github.com/cmspeedrunner/zenith")
    if "2dln" in s:
        opp = (eval(find_between( s, "[", "]" ))) 
        oppf = np.array(opp)
        opp2f = np.sort(oppf)
        plt.title("Line Graph")
        plt.plot(oppf, opp2f, color="red")
        plt.show()
    if "3dsc" in s:
        opp = (eval(find_between( s, "[", "]" ))) 
        opp2 = (eval(find_between( s, "<", ">" ))) 
        opp3 = (eval(find_between( s, "(", ")" ))) 

        fig = plt.figure(figsize = (10,10))
        ax = plt.axes(projection='3d')
        ax.grid()

        ax.scatter(opp, opp2, opp3, c = 'r', s = 50)
        ax.set_title('3D Scatter Plot')
        plt.show()
    if "3dcl" in s:
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
    if "3dsf" in s:
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

    if "3dgr" in s:
        fig = plt.figure(figsize = (12,10))
        ax = plt.axes(projection='3d')
        plt.show()

    if "" in s and "exit" not in s:
        continue
    if "exit" in s:
        break
