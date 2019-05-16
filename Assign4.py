
import glob
import re
from textblob import TextBlob
from collections import Counter



tfc = open("tfc.txt", "w+")
tfc_files = glob.glob('/Users/shreyastro/Desktop/Desktop_files/Stevens_Statements/spring_2019/FE595/Assign4/files/*.txt')
with tfc as outfile:
    for file in tfc_files:
        with open(file) as in_file:
            for line in in_file:
                line = str(line)
                line = line.strip()
                if "She's" in line:
                    x = re.split("She", line)
                    if len(x) >= 3:
                        line = ""
                        for i in x:
                            if len(i) > 10:
                                if "She's" not in i:
                                    i = "She" + i
                                if i[0].islower():
                                    if "she's" in i:
                                        i = "S" + i[1:]
                                while not re.search(r'(\w|[.])$', i):
                                    i = i[:-1]
                                    i = i.strip()
                                if re.search(r'\w$', i):
                                    i += "."
                                if re.search(r'They fight crime!', i):
                                    x = re.split("They", i)
                                    i = x[0]
                                    i = i.strip()
                                while re.search(r'^\W', i):
                                    i = i[1:]
                                    i = i.strip()
                                line += i + '\n'
                    else:
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                elif "He's" in line:
                    x = re.split("He", line)
                    if len(x) >= 3:
                        line = ""
                        for j in x:
                            if len(j) > 10:
                                if "He's" not in j:
                                    j = "He" + j
                                if j[0].islower():
                                    if "he's" in j:
                                        j = "H" + j[1:]
                                while not re.search(r'(\w|[.])$', j):
                                    j = j[:-1]
                                    j = j.strip()
                                if re.search(r'\w$', j):
                                    j += "."
                                while re.search(r'^\W', j):
                                    j = j[1:]
                                    j = j.strip()
                                line += j + '\n'
                    else:
                        if line[0].islower():
                            if "she's" in line:
                                line = "S" + line[1:]
                        if re.search(r'\w$', line):
                            line += "."
                        if re.search(r'They fight crime!', line):
                            x = re.split("They", line)
                            line = x[0]
                            line = line.strip()
                        if re.search(r'^\W', line):
                            line = line[1:]
                            line = line.strip()
                else:
                    if line[0].islower():
                        if "she's" in line:
                            line = "S" + line[1:]
                    if re.search(r'\w$', line):
                        line += "."
                    if re.search(r'They fight crime!', line):
                        x = re.split("They", line)
                        line = x[0]
                        line = line.strip()
                    if re.search(r'^\W', line):
                        line = line[1:]
                        line = line.strip()
                line += "\n"
                outfile.write(line)


fulltext = open("tfc.txt", "r")
get_word = fulltext.read()
blob = TextBlob(get_word)
bestman = " "
bestwoman = " "
worstman = " "
worstwoman = " "
woman = ""
man = ""
for i in blob.sentences:
    
    if "She's" in i:
        sentPol = i.polarity
        
        BW = TextBlob(bestwoman).polarity
        WW = TextBlob(worstwoman).polarity
        if sentPol > BW:
            bestwoman = str(i)
        if sentPol < WW:
            worstwoman = str(i)
    else:
        
        sentPol = i.polarity
        BM = TextBlob(bestman).polarity
        WM = TextBlob(worstman).polarity
        if sentPol > BM:
            bestman = str(i)
        if sentPol < WM:
            worstman = str(i)

print("Best: " + bestman + " " + bestwoman + " They fight crime!")
print("Worst: " + worstman + " " + worstwoman + " They fight crime!")

get_lines = get_word.splitlines()
for lines in get_lines:
    if "She's" in lines:
        woman += lines
        woman += "\n"
    elif "He's" in lines:
        man += lines
        man += "\n"

counterW = Counter(woman.splitlines())
print("10 Most Common Female: ")
print(counterW.most_common(10))
counterM = Counter(man.splitlines())
print("10 Most Common Male: ")
print(counterM.most_common(10))