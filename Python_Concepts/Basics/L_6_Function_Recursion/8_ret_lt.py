def ele(lt, index=0):
    if(index == len(lt)):
        return
    print(lt[index], end=", ")
    ele(lt,index+1)

sec = [1, 'a', 3, 'c', 5, 6, 7, 8]
(ele(sec))