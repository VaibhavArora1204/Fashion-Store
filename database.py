#Back-End
import mysql.connector as ms 
conn=ms.connect(host="localhost",user="root",passwd="1234",charset='utf8',database="fash")
mycursor=conn.cursor()

userid=''
userid_verification=[]
data=''

# MODULE NAMED 'database'......

def invalid_id_corr_trousers():
    try:
        order_item_id=int(input('Re-Enter the item id to be ordered:  ')) 
        print("")
        quantity=int(input('Enter the number of items to be entered : '))
        print("")
        price='select price from trousers where id='+str(order_item_id)
        mycursor.execute(price)
        price_cart=mycursor.fetchall()
        price_cart=price_cart[0][0]
        #print(type(price_cart))
        query_name='select name from trousers where id='+str(order_item_id)
        mycursor.execute(query_name)
        name_cart=mycursor.fetchall()
        name_cart=name_cart[0][0]
        #print(type(name_cart))
        final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
        mycursor.execute(final_query)
        conn.commit()
        print("")
        print('Item added to cart :)')
        print("")
        order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_trousers()

def invalid_id_corr_tees():
    try:
        order_item_id=int(input('Re-Enter the item id to be ordered:  ')) 
        print("")
        quantity=int(input('Enter the number of items to be entered : '))
        print("")
        price='select price from tshirts where id='+str(order_item_id)
        mycursor.execute(price)
        price_cart=mycursor.fetchall()
        price_cart=price_cart[0][0]
        #print(type(price_cart))
        query_name='select name from tshirts where id='+str(order_item_id)
        mycursor.execute(query_name)
        name_cart=mycursor.fetchall()
        name_cart=name_cart[0][0]
        #print(type(name_cart))
        final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
        mycursor.execute(final_query)
        conn.commit()
        print("")
        print('Item added to cart :)')
        print("")
        order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_tees()

def invalid_id_corr_shoes():
    try:
        order_item_id=int(input('Re-Enter the item id to be ordered:  ')) 
        print("")
        quantity=int(input('Enter the number of items to be entered : '))
        print("")
        price='select price from shoes where id='+str(order_item_id)
        mycursor.execute(price)
        price_cart=mycursor.fetchall()
        price_cart=price_cart[0][0]
        #print(type(price_cart))
        query_name='select name from shoes where id='+str(order_item_id)
        mycursor.execute(query_name)
        name_cart=mycursor.fetchall()
        name_cart=name_cart[0][0]
        #print(type(name_cart))
        final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
        mycursor.execute(final_query)
        conn.commit()
        print("")
        print('Item added to cart :)')
        print("")
        order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_shoes()

def invalid_id_corr_men_accessories():
    try:
        order_item_id=int(input('Re-Enter the item id to be ordered:  ')) 
        print("")
        quantity=int(input('Enter the number of items to be entered : '))
        print("")
        price='select price from men_accessories where id='+str(order_item_id)
        mycursor.execute(price)
        price_cart=mycursor.fetchall()
        price_cart=price_cart[0][0]
        #print(type(price_cart))
        query_name='select name from men_accessories where id='+str(order_item_id)
        mycursor.execute(query_name)
        name_cart=mycursor.fetchall()
        name_cart=name_cart[0][0]
        #print(type(name_cart))
        final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
        mycursor.execute(final_query)
        conn.commit()
        print("")
        print('Item added to cart :)')
        print("")
        order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_men_accessories()

def invalid_id_corr_women_accessories():
    try:
        order_item_id=int(input('Re-Enter the item id to be ordered:  ')) 
        print("")
        quantity=int(input('Enter the number of items to be entered : '))
        print("")
        price='select price from women_accessories where id='+str(order_item_id)
        mycursor.execute(price)
        price_cart=mycursor.fetchall()
        price_cart=price_cart[0][0]
        #print(type(price_cart))
        query_name='select name from women_accessories where id='+str(order_item_id)
        mycursor.execute(query_name)
        name_cart=mycursor.fetchall()
        name_cart=name_cart[0][0]
        #print(type(name_cart))
        final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
        mycursor.execute(final_query)
        conn.commit()
        print("")
        print('Item added to cart :)')
        print("")
        order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_women_accessories()

def men_tees():

    query_m_t="select * from tshirts where gender='male'"
    mycursor.execute(query_m_t)
    q1=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for q in q1:
         print('%6s'%(q[0]),'%20s'%(q[2]),'%6s'%(q[3]),'%15s'%(q[1]))
    print('==========================================================')

def men_trousers():
    query_m_tr="select * from trousers where gender='male'"
    mycursor.execute(query_m_tr)
    q2=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for w in q2:
        print('%6s'%(w[0]),'%6s'%(w[2]),'%20s'%(w[3]),'%15s'%(w[1]))
    print('==========================================================')

def men_shoes():
    query_m_shoe="select * from shoes where gender='male'"
    mycursor.execute(query_m_shoe)
    q3=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for e in q3:
        print('%6s'%(e[0]),'%20s'%(e[2]),'%6s'%(e[3]),'%15s'%(e[1]))
    print('==========================================================')

def men_accessories():
    query_m_access="select * from men_accessories"
    mycursor.execute(query_m_access)
    q4=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for r in q4:
        print('%6s'%(r[0]),'%20s'%(r[2]),'%6s'%(r[3]),'%15s'%(r[1]))
    print('==========================================================')

def women_tees():
    query_wm_t="select * from tshirts where gender='female'"
    mycursor.execute(query_wm_t)
    a1=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for a in a1:
         print('%6s'%(a[0]),'%6s'%(a[2]),'%20s'%(a[3]),'%15s'%(a[1]))
    print('==========================================================')
      
def women_trousers():
    query_wm_tr="select * from trousers where gender='female'"
    mycursor.execute(query_wm_tr)
    a2=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for s in a2:
         print('%6s'%(s[0]),'%20s'%(s[2]),'%6s'%(s[3]),'%15s'%(s[1]))
    print('==========================================================')

def women_shoes():
    query_wm_shoe="select * from shoes where gender='female'"
    mycursor.execute(query_wm_shoe)
    a3=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for d in a3:
         print('%6s'%(d[0]),'%20s'%(d[2]),'%6s'%(d[3]),'%15s'%(d[1]))
    print('==========================================================')

def women_accessories():
    query_wm_access="select * from women_accessories"
    mycursor.execute(query_wm_access)
    a4=mycursor.fetchall()
    print('==========================================================')
    print('%6s'%('ID'),'%20s'%('PRICE'),'%6s'%('GENDER'),'%15s'%('NAME'))
    print('==========================================================')
    for f in a4:
         print('%6s'%(f[0]),'%20s'%(f[2]),'%6s'%(f[3]),'%15s'%(f[1]))
    print('==========================================================')

def order_items_tees(): 
    #cart=[]
    order_choice=input('Do you wish to buy anything from this section(y/n) ? ')
    #userid='vaibhav@fashion.com'
    try:    
        while order_choice=='y':
            order_item_id=int(input('Enter the item id to be ordered:  ')) 
            print("")
            quantity=int(input('Enter the number of items to be entered : '))
            print("")
            price='select price from tshirts where id='+str(order_item_id)
            mycursor.execute(price)
            price_cart=mycursor.fetchall()
            price_cart=price_cart[0][0]
            #print(type(price_cart))
            query_name='select name from tshirts where id='+str(order_item_id)
            mycursor.execute(query_name)
            name_cart=mycursor.fetchall()
            name_cart=name_cart[0][0]
            #print(type(name_cart))
            final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
            mycursor.execute(final_query)
            conn.commit()
            print("")
            print('Item added to cart :)')
            print("")
            order_choice=input('Do you wish to add more items to be ordered:  ')
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_tees()
    welcome()

def order_items_trousers():
    #cart=[]
    order_choice=input('Do you wish to buy anything from this section(y/n) ? ')
    #userid='vaibhav@fashion.com'
    try:
        while order_choice=='y':
            order_item_id=int(input('Enter the item id to be ordered:  ')) 
            print("")
            quantity=int(input('Enter the number of items to be entered : '))
            print("")
            price='select price from trousers where id='+str(order_item_id)
            mycursor.execute(price)
            price_cart=mycursor.fetchall()
            price_cart=price_cart[0][0]
            #print(type(price_cart))
            query_name='select name from trousers where id='+str(order_item_id)
            mycursor.execute(query_name)
            name_cart=mycursor.fetchall()
            name_cart=name_cart[0][0]
            #print(type(name_cart))
            final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
            mycursor.execute(final_query)
            conn.commit()
            print("")
            print('Item added to cart :)')
            print("")
            order_choice=input('Do you wish to add more items to be ordered:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_trousers()
    welcome()  

def order_items_shoes(): 
    #cart=[]
    order_choice=input('Do you wish to buy anything from this section(y/n) ? ')
    #userid='vaibhav@fashion.com'
    try:
        while order_choice=='y':
            order_item_id=int(input('Enter the item id to be ordered:  ')) 
            print("")
            quantity=int(input('Enter the number of items to be entered : '))
            print("")
            price='select price from shoes where id='+str(order_item_id)
            mycursor.execute(price)
            price_cart=mycursor.fetchall()
            price_cart=price_cart[0][0]
            #print(price_cart)
            #print(type(price_cart))
            query_name='select name from shoes where id='+str(order_item_id)
            mycursor.execute(query_name)
            name_cart=mycursor.fetchall()
            name_cart=name_cart[0][0]
            #print(type(name_cart))
            final_query="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
            mycursor.execute(final_query)
            conn.commit()
            print("")
            print('Item added to cart :)')
            print("")
            order_choice=input('Do you wish to add more items to be ordered:  ')
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_shoes()

    welcome()

def order_items_men_accessories():
    mycursor=conn.cursor()
    order_choice=input('Do you wish to buy anything from this section(y/n) ? ')
    #userid='vaibhav@fashion.com'
    try:
        while order_choice=='y':
            order_item_id=int(input('Enter the item id to be ordered:  ')) 
            print("")
            quantity=int(input('Enter the number of items to be entered : '))
            print("")
            price='select price from men_accessories where id='+str(order_item_id)
            mycursor.execute(price)
            price_cart=mycursor.fetchall()
            price_cart=price_cart[0][0]
            #print(price_cart)
            #print(type(price_cart))
            query_name_men='select name from men_accessories where id='+str(order_item_id)
            mycursor.execute(query_name_men)
            name_cart=mycursor.fetchall()
            name_cart=name_cart[0][0]
            #print(name_cart)
            final_query_men="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
            mycursor.execute(final_query_men)
            conn.commit()
            print("")
            print('Item added to cart :)')
            print("")
            order_choice=input('Do you wish to add more items to be ordered from this section:  ')
    except:  
        print('The item-id entered is wrong!!')
        invalid_id_corr_men_accessories()
    welcome()  

def order_items_women_accessories():
    #cart=[]
    order_choice=input('Do you wish to buy anything from this section(y/n) ? ')
    #userid='vaibhav@fashion.com'
    try:
        while order_choice=='y':
            order_item_id=int(input('Enter the item id to be ordered:  ')) 
            print("")
            quantity=int(input('Enter the number of items to be entered : '))
            print("")
            price='select price from women_accessories where id='+str(order_item_id)
            mycursor.execute(price)
            price_cart=mycursor.fetchall()
            #print(price_cart)
            price_cart=price_cart[0][0]
            #print(type(price_cart))
            query_name_women='select name from women_accessories where id='+str(order_item_id)
            mycursor.execute(query_name_women)
            name_cart=mycursor.fetchall()
            #print(name_cart)
            name_cart=name_cart[0][0]
            #print(type(name_cart))
            final_query_women="insert into cart values({0},'{1}',{2},'{3}',{4})".format(order_item_id,name_cart,quantity,userid,price_cart)
            mycursor.execute(final_query_women)
            conn.commit()
            print("")
            print('Item added to cart :)')
            print("")
            order_choice=input('Do you wish to add more items to be ordered from this section:  ')  
    except:
        print('The item-id entered is wrong!!')
        invalid_id_corr_women_accessories()
    welcome()

def login_creation():
    c1=conn.cursor()
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
        login_id_veri()
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
        print(userid)
        print('Invalid password')
        login_passwd_verification()
    print("")

def login_passwd_verification():
    b=input("enter passwd:")
    print("")
    if b==data:
        print('*********** Access Granted ****************')
        welcome()
    else:
        print('Invalid password.......')
        login_passwd_verification()

def creation_error():
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
        login_creation()
    except:
        print('User-id already exists')
            
    return data,userid

def welcome():
    print("")
    print('select 1 to shop for men products')
    print('select 2 to shop for women products')
    print('Select 3 to show cart bill if any shopping done')
    print('Select 4 to exit the application')
    print("")
    choi=int(input('Enter your choice : '))
    print("")
    if choi==1:
        print("")
        print('select 1 to shop for men tees')
        print('select 2 to shop for men trousers')
        print('select 3 to shop for men shoes')
        print('select 4 to shop for men accessories')
        print("")
        choi_men=int(input('Enter your choice : '))
        print("")
        if choi_men==1:
            men_tees()
            order_items_tees()
        elif choi_men==2:
            men_trousers()
            order_items_trousers()
        elif choi_men==3:
            men_shoes()
            order_items_shoes()
        elif choi_men==4:
            men_accessories()
            order_items_men_accessories()
    elif choi==2:
        print("")
        print('select 1 to shop for women tees')
        print('select 2 to shop for women trousers')
        print('select 3 to shop for women shoes')
        print('select 4 to shop for women accessories')
        print("")
        choi_women=int(input('Enter your choice : '))
        print("")
        if choi_women==1:
            men_tees()
            order_items_tees()
        elif choi_women==2:
            men_trousers()
            order_items_trousers()
        elif choi_women==3:
            men_shoes()
            order_items_shoes()
        elif choi_women==4:
            women_accessories()
            order_items_women_accessories()
    elif choi==3:
        cart()  # not made yet
    
    elif choi==4:
        feedback()
    else:
        print('Wrong input !!')
        welcome()

def login_id_veri():
    global userid_verification
    userid=input("enter user_id:")
    #print(userid_verification)
    #print(userid in userid_verification)
    if (userid in userid_verification):
        print('**************** Access Granted *****************')
        login_passwd_verification()

    elif userid not in userid_verification:
        print('user-id invalid')
        login_id_veri()

def feedback():
    #print("Thank you for your visit at our 'TRENDING FASHION STORE'!!") 
    print("")
    print('Please help us with your feeback :)')
    feedback_input=input("On a scale of 1 to 5, please rate how you found our service:") 
    if feedback_input=='5':
        print("")
        print("We glad you found our service to be pleasing :)")
        print("")
    if feedback_input=='4' or feedback_input=='3':
        print("") 
        print("We are glad to provide you with our services.Hope you have an even better experience next time!")
        print("")
    if feedback_input=='2' or feedback_input=='1':
        print("")
        print("We are sorry that you found our service unsatisfactory :(")
        input("Please provide your valuable feedback for us to improve upon our shortcomings:")
        print("Looking forward to see you shop at our store again!")
        print("")
    else:
        print("Sorry!! You've entered wrong input...")
        feedback()

def cart(): 
    mycursor=conn.cursor()
    enter_user_id=input('Enter your user-id to visit your cart : ')
    cart_query="select id,name,quantity,quantity*price from cart where user_id='%s'"%(enter_user_id,)
    mycursor.execute(cart_query)
    cart_bill=mycursor.fetchall()
    #print(cart_bill)
    print('===========================================================================')
    print('%6s'%('ID'),'%20s'%('QUANTITY'),'%6s'%('PRICE'),'%15s'%('NAME'))
    print('===========================================================================')
    for f in cart_bill:
        print('%6s'%(f[0]),'%20s'%(f[2]),'%6s'%(f[3]),'%15s'%(f[1]))
    print('===========================================================================')
    amt_query= "select sum(price*quantity) from cart where user_id='%s'"%(enter_user_id,)
    mycursor.execute(amt_query)
    total_bill=mycursor.fetchall()
    total_bill=total_bill[0][0]
    print('')
    print('')
    print('Total payable amount is : ',total_bill)
    print("")
    print('Thank you for shopping at our store :)')
    print("")
    feedback()

def order_items(): 
    cart=[]
    order_choice=input('Do you wish buy anything from this section?(y/n)?')
    while order_choice=='y':
        order_item_id=int(input('Enter the item id to be ordered:  ')) 
        cart.append(order_item_id)
        print(cart)
        order_choice=input('Do you wish to add more items to be ordered:  ')
    print('select 1 to shop for men products')
    print('select 2 to shop for women products')
    print('select 3 to shop for women shoes')
    print('Select 4 to exit the application')
    print("")
    choi=int(input('Enter your choice : '))
    print("")
    if choi==1:
        print("")
        print('select 1 to shop for men tees')
        print('select 2 to shop for men trousers')
        print('select 3 to shop for men shoes')
        print('select 4 to shop for men accessories')
        print("")
        choi_men=int(input('Enter your choice : '))
        print("")
        if choi_men==1:
            men_tees()
            order_items()
        elif choi_men==2:
            men_trousers()
            order_items()
        elif choi_men==3:
            men_shoes()
            order_items()
        elif choi_men==4:
            men_accessories()
            order_items()
    if choi==2:
        print("")
        print('select 1 to shop for women tees')
        print('select 2 to shop for women trousers')
        print('select 3 to shop for women shoes')
        print('select 4 to shop for women accessories')
        print("")
        choi_women=int(input('Enter your choice : '))
        print("")
        if choi_women==1:
            men_tees()
            order_items()
        elif choi_women==2:
            men_trousers()
            order_items()
        elif choi_women==3:
            men_shoes()
            order_items()
        elif choi_women==4:
            men_accessories()
            order_items()
    if choi==3:
        cart()

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
            login_id_veri()
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
            login_passwd_verification()
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
            login_creation()
        except:
            print('User-id already exists')
            creation_error()

    return data,userid

login()



