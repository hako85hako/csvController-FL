
import numpy

def changeRW(ch_list_path,offset):
    #目的としては連想配列の作成
    #配列の数がそのまま新CSVのindex番号に使用
    #[[元CSVでのindex、0次係数、1次係数],...]
    #入れ替えチャネルの指定
    fin = open(ch_list_path, "r")
    #fout = open('result.csv', "w")
    ch_list = []

    for line in numpy.array([s.strip('\n').split(',') for s in fin]).T:
        ch_list += [line]  
    fin.close()

    for ch_set in ch_list:
        if isint(ch_set[0]):
            #目的とするチャンネル番号を設定(offset処理)を行う
            ch_set[0] = ch_set[0]+int(offset)
        if ch_set[1]:
            if not isint(ch_set[1]):
                ch_set[1] = 1
        else:
            ch_set[1] = 1
        
        if ch_set[2]:
            if not isint(ch_set[2]):
                ch_set[2] = 0
        else:
            ch_set[2] = 0
    return ch_set

if __name__=="__main__":
    changeRW('test.csv',8)


# int型に変換可能かどうかを判定
def isint(s): 
    try:
        int(s) 
    except ValueError:
        return False
    else:
        return True