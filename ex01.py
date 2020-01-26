
# exercise two
def baby_smile(a_smile,b_smile):
    if a_smile==True and b_smile==True:
        return 'you are in trouble'
    elif a_smile==False and b_smile==False:
        return 'you are in trouble'
    else:
        return 'babies are good'


# exercise three
def num_sum(value_1,value_2):
    """
    parameters:
        -value_1 : int value
        -value_2 : int value
    Return
    data type is int
    """
    if (value_1==value_2):
        return (value_1+value_2)*2
    else:
        return value_1+value_2


# exercise four
def machine(hour):
    return list(range(hour+1,24))


#exercise 5
def comp(val_1, val_2,para):
    if (val_1 > 0 and val_2 < 0) or (val_1 < 0 and val_2 > 0):
        return True
    elif (para==True) and (val_1 < 0 and val_2 < 0):
        return True
    else:
        return False



#exercise 6
def swap_word(x):
    if (len(x)==1):
        return x
    else:
        return x[-1] + x[1:-1] + x[0]


#exercise 7
def rep_word(w,num=3):
    if (len(w)<3):
        return ('short string')
    elif (len(w)==3):
        return w*num
    else:
        return w[0:num]*num


def rep_word_1(w):
    if len(w)<2 :
        return ('short string')
    elif len(w)==2 :
        return w*3
    else:
        return w[-2:]*3



def zero_list(g_list):
    new_list=[]
    x=len(g_list)*2
    last_el=g_list[-1]

    for i in range(x):
        new_list.append(0)
    new_list[-1]=last_el

    return new_list


def nine_list(n_list):
    my_list_2 = list(set(n_list))







if __name__ == '__main__':
    # var=baby_smile(True,True)
    # print(var)
    #var_1=num_sum(3,3)
    #print(var_1)
    #help(num_sum)
    #var_2=machine(4)
    #print(var_2)
    #var_5=comp(-3,-2,False)
    #print(var_5)
    #var_6=swap_word('code')
    #print(var_6)

    #var_7=rep_word('abcdefgh',5)
    #print(var_7)

    #print(rep_word_1('hellow'))

    #print(zero_list([3,4,6]))

    f=lambda a: a*a
    print(f(12))

    h = lambda x,y: x*x +y
    print(h(3,1))
