# Front-end
import mysql.connector as ms 
import fashion
conn=ms.connect(host="localhost",user="root",passwd="1234",charset='utf8',database="fash")
mycursor=conn.cursor()

userid=''
userid_verification=[]

'''
def login():
    global data
    global userid
    global userid_verification
    c1=conn.cursor()
    c1.execute('use fash')
    print("")
    print("")
    print("======================== WELCOME TO TRENDING FASHION STORE ======================================")
    print(' ')
    from time import gmtime,strftime
    a=strftime("%a,%d%b%y",gmtime())
    print(a)
    print(' ')
    print("1.login")
    print("2.To create account")
    print("")
    print('')
    choice=int(input("Enter your choice : "))
    print(' ')
    if choice==1:
        c1.execute('select user_id from login')
        uid=c1.fetchall()
        for y in uid:
            for j in y:
                userid_verification.append(j)
        print("")
        userid=input("enter user_id:")
        print("")
        print('')
        if (userid in userid_verification):
            print("*********** Access granted ***************")
        else:
            print('User-id invalid.....')
            fashion.login_id_veri()
        c1=conn.cursor()
        c1.execute("select passwd from login where user_id = '"+(userid)+"' ;")
        data=c1.fetchall()
        data=data[0]
        data=list(data)
        data=data[0]
        data=str(data)
        print('')
        print('')
        b=input("Enter passwd : ")
        print("")
        if b==data:
            print('********************** Access Granted *******************************')
        else:
            print('Invalid password')
            fashion.login_passwd_verification()
        print("")
    if choice==2:
        print('To create your account please enter your user id and password')
        c1=conn.cursor()
        v_name=input("Enter your full  name : ")
        print('')
        v_user_id=input("Choose your user id : ")
        print('')
        v_passwd=int(input("Create your password (in integer) : "))
        print('')
        try:
            c1=conn.cursor()
            update="insert into login values('"+v_name+"','"+ v_user_id +"',"+ str(v_passwd)+")"
            c1.execute(update)
            conn.commit()
            print("*************** account created ********************")
            fashion.login_creation()
        except:
            print('User-id already exists')
            fashion.creation_error()

    return data,userid
'''
'''   #welcome
def welcome():
    print("")
    print('Shop for men products ( press 1 )')
    print('Shop for women products ( press 2 )')
    print('Show cart bill if any shopping done ( press 3 )')
    print('To exit the application ( press 4 )')
    print("")
    choi=int(input('Enter your choice : '))
    print("")
    if choi==1:
        print("")
        print('Shop for men tees ( press 1 )')
        print('Shop for men trousers ( press 2 )')
        print('Shop for men shoes ( press 3 )')
        print('Shop for men accessories ( press 4 )')
        print("")
        choi_men=int(input('Enter your choice : '))
        print("")
        if choi_men==1:
            fashion.men_tees()
            fashion.order_items_tees()
        elif choi_men==2:
            fashion.men_trousers()
            fashion.order_items_trousers()
        elif choi_men==3:
            fashion.men_shoes()
            fashion.order_items_shoes()
        elif choi_men==4:
            fashion.men_accessories()
            fashion.order_items_men_accessories()
    elif choi==2:
        print("")
        print('Shop for men tees ( press 1 )')
        print('Shop for men tees ( press 2 )')
        print('Shop for men tees ( press 3 )')
        print('Shop for men tees ( press 4 )')
        print("")
        choi_women=int(input('Enter your choice : '))
        print("")
        if choi_women==1:
            fashion.men_tees()
            fashion.order_items_tees()
        elif choi_women==2:
            fashion.men_trousers()
            fashion.order_items_trousers()
        elif choi_women==3:
            fashion.men_shoes()
            fashion.order_items_shoes()
        elif choi_women==4:
            fashion.women_accessories()
            fashion.order_items_women_accessories()
    elif choi==3:
        fashion.cart()  # not made yet
    
    elif choi==4:
        fashion.feedback()
    else:
        print('Wrong input !!')
        fashion.welcome()
'''


fashion.login()

fashion.welcome()











