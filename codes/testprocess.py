import csv
import numpy as np

np_1 = np.load("./results/ernie-1.0_result.npy", allow_pickle=True)
np_2 = np.load("./results/multi_choice_ernie_predictions.npy", allow_pickle=True)

testpath = "./test.csv"
outpath = "./test_out_2.csv"

txtpath_1 = "./results/ernie_predict.txt"
txtpath_2 = "./results/multi_choice_ernie_testpredict.txt"
txtpath_chaizi = "./results/chaizi_testpredict.txt"

csvReader = csv.reader(open(testpath, encoding="utf-8"))
goalFile = open(outpath, 'w', newline='')
writer = csv.writer(goalFile)

txt_1 = open(txtpath_1, "r")
txt_2 = open(txtpath_2, "r")
txt_chaizi = open(txtpath_chaizi, "r")

cnt = 0
total = 0
for line in csvReader:
    if line[0] == "riddle":
        line.append("predict1")
        line.append("predict2")
        line.append("judge")
    else:
        riddle = line[0][:line[0].find("（")]
        riddle = riddle.replace(" ", "")
        
        p1 = txt_1.readline()
        p2 = txt_2.readline()
        pc = txt_chaizi.readline()
        
        if len(riddle) <= 2:
            line.append(pc[0])
            line.append(pc[0])
            line.append(pc[0])
        else:
            line.append(p1[0])
            line.append(p2[0])
            score1 = np_1[total][int(p1[0])]
            score2 = np_2[total][int(p2[0])]
            if score1 > score2:
                line.append(p1[0])
            else:
                line.append(p2[0])
            if p1 != p2:
                cnt += 1
                print(line[0])
        total += 1
    writer.writerow(line)
    
print(cnt)
txt_1.close()
txt_2.close()
txt_chaizi.close()
goalFile.close()