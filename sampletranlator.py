from englisttohindi.englisttohindi import EngtoHindi
import pandas as pd
import numpy as np
from gtts import gTTS 
import os 
import zipfile
import shutil

def eng_to_hindi(textfile):
    f = open(textfile, "r")
    tx=textfile.split("\\")
    print(tx[-1])
    fname="translated_"+str(tx[-1])
    dir1="audio_hindi_"+fname.replace('.','_')
    dir2="audio_english_"+fname.replace('.','_')
    path1="uploads\\"+dir1
    path2="uploads\\"+dir2
    print(path1)
    isExist = os.path.exists(path1)
    isExistnew = os.path.exists(path2)
    articles=['a','an','the']
    if not isExist:
           os.makedirs(path1)
    if not isExistnew:
           os.makedirs(path2)
    if textfile.endswith(".xlsx"):
        try:
            df = pd.read_excel(textfile,names=['English'],usecols="A")
            print(df.head())
            df=df.dropna()
            df["Hindi"]=np.nan
            for i in df.index:
                a=str(df["English"][i])
                if a!=" ":
                    df["English"][i]=str(df["English"][i]).strip()
                    df["English"][i]=df["English"][i].replace('!',',')
                    df["English"][i]=df["English"][i].replace('.',',')
                    trans = EngtoHindi(df["English"][i])
                    res=trans.convert
                    print(df["English"][i])
                    print(res)
                    df["Hindi"][i]=res
                    myobj = gTTS(text=res, lang='hi', slow=True)
                    myobjeng = gTTS(text=a, lang='en', slow=True)
                    line=df["English"][i]
                    line=line.replace(" ",'')
                    line=line.replace(".",'')
                    line=line.lower()
                    #line=list(line)
                    #for i in line:
                        #if i in articles:
                            #line.remove(i)
                    #line=str(line)
                    #line=line[0:5]
                    line=str(i)+"_"+line[0:5]
                    line=''.join(e for e in line if e.isalnum())
                    audiofile=line+'.mp3'
                    print(audiofile)
                    myobj.save(path1+"\\"+audiofile)
                    myobjeng.save(path2+"\\"+audiofile)

                    zipp="uploads\\"+dir1
                    zipp1="uploads\\"+dir2
                    print(zipp)
                    auddir=dir1+'.zip'
                    auddireng=dir2+'.zip'
                    print(auddir)
                    archived = shutil.make_archive(zipp, 'zip', path1)
                    archivedeng = shutil.make_archive(zipp1, 'zip', path2)
                    print(archived)
                else:
                    continue

            writer = pd.ExcelWriter("uploads\\"+fname)
            df.to_excel(writer)
            writer.close()
            return fname,auddir,auddireng
        except:
            return "file not readable","no audio available","no audio available"

    elif textfile.endswith(".csv"):
        try:
            df = pd.read_csv(textfile,names=['English'],usecols=['English'])
            print(df.head())
            df=df.dropna()
            df["Hindi"]=np.nan
            for i in df.index:
                a=str(df["English"][i])
                if a!=" ":
                    df["English"][i]=str(df["English"][i]).strip()
                    df["English"][i]=df["English"][i].replace('!',',')
                    df["English"][i]=df["English"][i].replace('.',',')
                    trans = EngtoHindi(df["English"][i])
                    res=trans.convert
                    print(df["English"][i])
                    print(res)
                    df["Hindi"][i]=res
                    myobj = gTTS(text=res, lang='hi', slow=True)
                    myobjeng = gTTS(text=a, lang='en', slow=True)
                    line=df["English"][i]
                    line=line.replace(" ",'')
                    line=line.replace(".",'')
                    line=line.lower()
                    #line=list(line)
                    #for i in line:
                        #if i in articles:
                            #line.remove(i)
                    #line=str(line)
                    line=str(i)+"_"+line[0:5]
                    line=''.join(e for e in line if e.isalnum())
                    audiofile=line+'.mp3'
                    print(audiofile)
                    myobj.save(path1+"\\"+audiofile)
                    myobjeng.save(path2+"\\"+audiofile)

                    zipp="uploads\\"+dir1
                    zipp1="uploads\\"+dir2
                    print(zipp)
                    auddir=dir1+'.zip'
                    auddireng=dir2+'.zip'
                    print(auddir)
                    archived = shutil.make_archive(zipp, 'zip', path1)
                    archivedeng = shutil.make_archive(zipp1, 'zip', path2)
                    print(archived)
                else:
                    continue

            df.to_csv("uploads\\"+fname,encoding="utf-8")
            return fname,auddir,auddireng
        except:
            return "file not readable","no audio available","no audio available"
    
    elif textfile.endswith(".txt"):  
        try: 

            f1=open("uploads\\"+fname,"w",encoding="utf-8")
            for line in f:
                line=str(line)
                trans = EngtoHindi(line)
                res = trans.convert
                print(res)      
                print("line: ",line)
                f1.write(res+"\n")
                #print(linenew.pronunciation)
                myobj = gTTS(text=res, lang='hi', slow=True)
                myobjeng = gTTS(text=line, lang='en', slow=True)
                line=line.removesuffix("\n")
                line=line.replace(" ",'')
                line=line[0:5]
                audiofile=line+'.mp3'
                print(audiofile)
                myobj.save(path1+"\\"+audiofile)
                myobjeng.save(path2+"\\"+audiofile)          

                zipp="uploads\\"+dir1
                zipp1="uploads\\"+dir2
                print(zipp)
                auddir=dir1+'.zip'
                auddireng=dir2+'.zip'
                print(auddir)
                archived = shutil.make_archive(zipp, 'zip', path1)
                archivedeng = shutil.make_archive(zipp1, 'zip', path2)
                print(archived)
                
                #os.system("start "+audiofile)
            f1.close()

            ff=open("uploads\\"+fname, "r")
            return fname,auddir,auddireng
        except:
            return "file not readable","no audio available","no audio available"
    else:
        return "File type not supported","no audio available","no audio available"
