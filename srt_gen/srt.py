import os
import time

fstr = ""
idx = 1
os.chdir(os.path.abspath(os.path.dirname(__file__)))
with open("./srt_source.txt", encoding="utf8") as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        if line != "":
            ct = time.localtime(time.time())
            timeStr = line[0:8]
            dt = time.strptime(timeStr + "-" + (str)(ct.tm_year), "%H:%M:%S-%Y")
            dtt = time.mktime(dt)
            dtt -= 8
            dt2 = time.localtime(dtt)
            beforeTimeStr = time.strftime("%H:%M:%S", dt2)
            # print(beforeTimeStr + " " + timeStr)
            fstr += (str)(idx) + "\n"
            fstr += "{0} --> {1}\n".format(beforeTimeStr + ",000", timeStr + ",000")
            fstr += line[8:] + "\n\n"
            idx+=1

print(fstr)
with open('./str_output.srt',mode='w+') as f:
    f.write(fstr)
