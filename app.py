import os
import csv
import frame
from glob import glob

def main(dir_name,ch_list,coefficient_1_list,coefficient_0_list,none_select_column,none_valiable_column,offset,id,password):
    #data以下のファイル格納場所
    files = glob(f'{dir_name}/data/*')
    #print(files)
    #offset設定
    offset = int(offset)
    for file in files:
        data = []
        #ファイル名作成用########################################################
        dirname = os.path.basename(file)
        dirname_year = dirname[0:4]
        dirname_month = dirname[4:6]
        dirname = id + '_' + dirname_year + '-' + dirname_month + '-01'
        #以下形式で出力される
        #FL999-99999_0000_2021-01-01
        #####################################################################

        print(coefficient_1_list)
        print(coefficient_0_list)
        #編集用パス指定
        csv_paths = glob(f'{file}/*.csv')
        
        #テスト
        #print("↓csvのpathが出力されるはず")
        #print(csv_paths)

        for csv_path in csv_paths:
            #csv読み込み
            f = open(csv_path, 'r')
            #headerの取得
            header = next(f)
            #リスト形式
            f = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
            #取得したCSVの列数分forを回す
            for row in f:
                #結果の入子
                items = []
                item = []
                #for ch in ch_list:
                for i in range(offset):
                    item = row[i]
                    items += [item]

                for i,ch in enumerate(ch_list):
                    #入れ替えチャンネル指定時、「--」を配列番号と一致させる
                    if type(ch) is str:
                        # try:
                        #     row[i+offset-1] = none_select_column
                        #     ch = i + offset - 1
                        # except:
                        ch = i + offset - 1
                    else:
                        ch = ch + offset - 1 
                    #入れ替え対象のチャンネルが空白の場合
                    try:
                        if isfloat(row[ch]):
                            item = (float(row[ch])*coefficient_1_list[i])+coefficient_0_list[i]
                        else:
                            #row[ch] = none_valiable_column
                            item = none_valiable_column
                    except:
                        #row[ch] = none_valiable_column
                        item = none_valiable_column
                    items += [item]
                data += [items]
        data.insert(0, [id,password])
        path = dir_name+'/'+dirname+'.csv'
        f = open(path, 'w',newline="")
        writer = csv.writer(f)
        writer.writerows(data)
        f.close()
        print(dirname+'：done')
if __name__=="__main__":
    frame.TkinterClass()




# 浮動小数点数値に変換可能かどうかを判定
def isfloat(s): 
    try:
        float(s) 
    except ValueError:
        return False
    else:
        return True