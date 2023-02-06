import os
import webbrowser
import sys
import random
loop = True
while loop == True:
    s = input("ZIP--->")
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
    if "calc" in s:
        calc = int((eval(find_between( s, "[", "]" ))))
        print(calc)
    if "log" in s:
        log = ((find_between( s, "['", "']" )))
        print(log)
    if "log." in s:
        num = find_between( s, "<", ">" )
        main = int(num)
        for int in range(main):
            eval = find_between( s, "['", "']" )
            print(eval)
    if "cdir" in s:
        os.mkdir(find_between( s, "['", "']" ))
    if "rand" in s:
        main = int(find_between( s, "[", "]" ))
        print(random.randint(0,main))
    if "rinr" in s:
        main = int(find_between( s, "[", "]" ))
        main2 = int(find_between( s, "<", ">" ))
        print(random.randint(main,main2))
    if "wrto" in s:
        location = (find_between( s, "[L:'", "']" ))
        content = (find_between( s, "<C:'", "'>" ))
        f = open(location, "a")
        f.write(content)
        f.close()
    if "ourl" in s:
        log = ((find_between( s, "['", "']" )))
        webbrowser.open_new(log)
    if "pass" in s:
        os.system(find_between( s, "['", "']" ))
    if "dfil" in s:
        os.remove(find_between( s, "['", "']" ))
    if "ddir" in s:
        os.removedirs(find_between( s, "['", "']" ))
    if "size" in s:
        main = (sys.getsizeof(find_between( s, "['", "']" ))," BITS")
        print(main)
        print(len(find_between( s, "['", "']" ))," BYTES")

    if "" in s and "exit" not in s:
        continue
    if "exit" in s:
        break

    
