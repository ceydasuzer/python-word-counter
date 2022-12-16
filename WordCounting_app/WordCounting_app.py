import os.path 
import io

def sortby_order(counts):
    reversed_counts = sorted(counts.items(), reverse= True, key =lambda x: x[1])
    print("Dosyadaki kelime sayıları: ")   
    for items in reversed_counts:
        print(items[0], ":" , items[1])

def word_count(str):
     with open(txt_dosya , encoding="latin-1") as textfile:
         str = textfile.read()
         counts = dict()
         words = str.replace(","," ").replace("!"," ").replace("?"," ").replace(":"," ").replace("."," ").lower().split()
         for word in words:
             if word in counts:
                counts[word] += 1
             else:
                counts[word] = 1
         sortby_order(counts)
               
while True: 
        print("Okutmak istediğiniz txt dosyasını girin:  ")
        txt_dosya = input()  
        txt_dosya.lower()
        if (txt_dosya.endswith('.txt')) and (os.path.isfile(txt_dosya)):
            word_count(txt_dosya)
        else:
            print("Dosya adını txt uzantılı olacak şekilde girin ya da başka bir dosya adı deneyin.")
        continue 
 
   

