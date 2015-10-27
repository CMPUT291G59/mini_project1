import sys
import os 
import create_view
def find_acode(conString,connection,curs,a_text):
    a_text=a_text.upper()
    print(a_text)
    afind="""
    select *
    from airports a
    where upper(a.acode) like '{0}'
    or upper(a.acode) like '{0}%'
    or upper(a.acode) like '%{0}'
    or upper(a.acode) like '%{0}%'
    or upper(a.name) like '{0}'
    or upper(a.name) like '{0}%'
    or upper(a.name) like '%{0}'
    or upper(a.name) like '%{0}%'
    or upper(a.city) like '{0}'
    or upper(a.city) like '{0}%'
    or upper(a.city) like '%{0}'
    or upper(a.city) like '%{0}%'
    """
    curs.execute(afind.format(a_text))
    a_find=curs.fetchall()
    if a_find==False:
        print("You enter is invalid please try again!!!")
    elif a_find!=False:
        for i, a in enumerate(a_find):
            print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[1]) + (10-len(str(a[1])))*' ' + str(a[2]))
        b=int(input("Choose a airport "))
        a_text=a_find[b-1][0]
        return a_text
    

def find_regular_flight(conString,connection,curs,email,src,dst,dep_date):
    create_view.search_view(conString,connection,curs)
    query = """select 
    flightno1,
    flightno2,
    dep_date, 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    seat2,
    1 no_stop
    from good_connections g_c
    where g_c.src='{0}' and
    g_c.dst='{1}' and
    g_c.dep_date=to_date('{2}','dd/mm/yyyy')
    union
    select 
    flightno,
    '' flightno2,
    dep_date, 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    0 layover, 
    price,
    seats,
    null seat2,
    0 no_stop
    from available_flights a
    where a.src='{0}' and
    a.dst='{1}' and
    a.dep_date=to_date('{2}','dd/mm/yyyy')"""    
    
    curs.execute(query.format(src, dst, dep_date))
    flight=curs.fetchall()
    print("Index"+5*" "+"Flightno1"+1*" "+"Flightno2"+1*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"layover"+3*" "+"price"+5*" "+"seat1"+5*" "+"seat2"+5*" "+"no_stop")
    for i, a in enumerate(flight):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[1]) + (10-len(str(a[1])))*' ' + str(a[3]) + (10-len(str(a[3])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6]) +(10-len(str(a[6])))*' '+ str(a[7]) + (10-len(str(a[7])))*' '+ str(a[8])+(10-len(str(a[8])))*' '+ str(a[9])+(10-len(str(a[9])))*' '+ str(a[10])+(10-len(str(a[10])))*' '+str(a[11]))
    check=input("Do you want to book any flight above? (Y/N) ")
    check=check.upper()
    if check=="Y":
	print(1)
    elif check=="N":
	return
    else:
	print("Invalid input please try again")
def find_2stop_flight(conString,connection,curs,email,src,dst,dep_date):
    create_view.search_view(conString,connection,curs)
    query = """select 
    flightno1,
    flightno2,
    '' flightno3,
    dep_date, 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    seat2,
    null seat3,
    1 no_stop
    from good_connections g_c
    where g_c.src='{0}' and
    g_c.dst='{1}' and
    g_c.dep_date=to_date('{2}','dd/mm/yyyy')
    union
    select 
    flightno,
    '' flightno2,
    '' flightno3,
    dep_date, 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    0 layover, 
    price,
    seats,
    null seat2,
    null seat3,
    0 no_stop
    from available_flights a
    where a.src='{0}' and
    a.dst='{1}' and
    a.dep_date=to_date('{2}','dd/mm/yyyy')
    union
    
    select 
    flightno1,
    flightno2,
    flightno3,
    dep_date,
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    seat2,
    seat3,
    2 no_stop
    from good2_connections g2
    where g2.src='{0}' and
    g2.dst='{1}' and
    g2.dep_date=to_date('{2}','dd/mm/yyyy')
    """    
    
    curs.execute(query.format(src, dst, dep_date))
    flight1=curs.fetchall()
    #print(flight1)
    print("Index"+5*" "+"Flightno1"+1*" "+"Flightno2"+1*" "+"Flightno3"+1*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"layover"+3*" "+"price"+5*" "+"seat1"+5*" "+"seat2"+5*" "+"seat3"+5*" "+"no_stop")
    for i, a in enumerate(flight1):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[1]) + (10-len(str(a[1])))*' ' + str(a[2]) + (10-len(str(a[2])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6]) +(10-len(str(a[6])))*' '+ str(a[7]) + (10-len(str(a[7])))*' '+ str(a[8])+(10-len(str(a[8])))*' '+ str(a[9])+(10-len(str(a[9])))*' '+ str(a[10])+(10-len(str(a[10])))*' '+str(a[11])+(10-len(str(a[11])))*' '+ str(a[12])++(10-len(str(a[12])))*' '+ str(a[13]))
    
    check=input("Do you want to book any flight above? (Y/N) ")
    check=check.upper()
    if check=="Y":
	print(1)
    elif check=="N":
	return
    else:
	print("Invalid input please try again")