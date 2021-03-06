import sys
import os 
import create_view
import interface
def find_acode(conString,connection,curs,a_text):     # finding the airport code
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
    
def find_direct_flight(conString,connection,curs,email,src,dst,dep_date):    # find the directing flight by creating view
    create_view.search_view(conString,connection,curs)
    query = """
	select 
	flightno,
	to_char(dep_date,'dd/mm/yyyy'), 
	src, 
	dst, 
	to_char(dep_time,'HH24:MI'),
	to_char(arr_time, 'HH24:MI'), 
	price,
        fare,
	seats
	from available_flights a
	where a.src='{0}' and
	a.dst='{1}' and
	a.dep_date=to_date('{2}','dd/mm/yyyy')
        order by price
        """
    curs.execute(query.format(src, dst, dep_date))
    flight=curs.fetchall()
    print("Index"+5*" "+"Flightno"+2*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"price"+5*" "+"fare"+6*" "+"seat")
    for i, a in enumerate(flight):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[2]) + (10-len(str(a[2])))*' ' + str(a[3]) + (10-len(str(a[3])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6])+(10-len(str(a[6])))*' '+ str(a[7])+(10-len(str(a[7])))*' '+ str(a[8]))
    return flight
		    
def find_regular_flight(conString,connection,curs,email,src,dst,dep_date):       #find the avilable regular flights by creating view
    create_view.search_view(conString,connection,curs)
    print("Choose one of following option")
    print("1.Sort by price (from low to high)")
    print("2.Sort by number of connections (from low to high)")
    a=input("")
    a=interface.check_int(a,3,"Invalid input")
    query = """select 
    flightno1,
    flightno2,
    to_char(dep_date,'dd/mm/yyyy'), 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    fare1,
    seat2,
    fare2,
    1 no_stop
    from good_connections g_c
    where g_c.src='{0}' and
    g_c.dst='{1}' and
    g_c.dep_date=to_date('{2}','dd/mm/yyyy')
    union
    select 
    flightno,
    '' flightno2,
    to_char(dep_date,'dd/mm/yyyy'), 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    0 layover, 
    price,
    seats,
    fare,
    null seat2,
    null fare2,
    0 no_stop
    from available_flights a
    where a.src='{0}' and
    a.dst='{1}' and
    a.dep_date=to_date('{2}','dd/mm/yyyy')
    """   
    
    if a==1:
        query+"\n order by price"
        curs.execute(query.format(src, dst, dep_date))
        flight=curs.fetchall()	
    else:
        query+"\n order by no_stop"
        curs.execute(query.format(src, dst, dep_date))
        flight=curs.fetchall()
    print("Index"+5*" "+"Flightno1"+1*" "+"Flightno2"+1*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"layover"+3*" "+"price"+5*" "+"seat1"+5*" "+"fare1"+5*" "+"seat2"+5*" "+"fare2"+5*" "+"no_stop")
    for i, a in enumerate(flight):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[1]) + (10-len(str(a[1])))*' ' + str(a[3]) + (10-len(str(a[3])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6]) +(10-len(str(a[6])))*' '+ str(a[7]) + (10-len(str(a[7])))*' '+ str(a[8])+(10-len(str(a[8])))*' '+ str(a[9])+(10-len(str(a[9])))*' '+ str(a[10])+(10-len(str(a[10])))*' '+str(a[11])+(10-len(str(a[11])))*' '+str(a[12])+(10-len(str(a[12])))*' '+str(a[13]))
    return flight
def find_2stop_flight(conString,connection,curs,email,src,dst,dep_date):
    create_view.search_view(conString,connection,curs)
    print("Choose one of following option")
    print("1.Sort by price (from low to high)")
    print("2.Sort by number of connections (from low to high)")
    a=input("")
    a=interface.check_int(a,3,"Invalid input")    
    
    query = """select 
    flightno1,
    flightno2,
    '' flightno3,
    to_char(dep_date,'dd/mm/yyyy'), 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    fare1,
    seat2,
    fare2,
    null seat3,
    null fare3,
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
    to_char(dep_date,'dd/mm/yyyy'),  
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    0 layover, 
    price,
    seats,
    fare,
    null seat2,
    null fare2,
    null seat3,
    null fare3,
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
    to_char(dep_date,'dd/mm/yyyy'), 
    src, 
    dst, 
    to_char(dep_time,'HH24:MI'),
    to_char(arr_time, 'HH24:MI'), 
    layover*1440, 
    price,
    seat1,
    fare1,
    seat2,
    fare2,
    seat3,
    fare3,
    2 no_stop
    from good2_connections g2
    where g2.src='{0}' and
    g2.dst='{1}' and
    g2.dep_date=to_date('{2}','dd/mm/yyyy')
    """    
    
    if a==1:
        query+"\n order by price"
        curs.execute(query.format(src, dst, dep_date))
        flight=curs.fetchall()	
    else:
        query+"\n order by no_stop"
        curs.execute(query.format(src, dst, dep_date))
        flight=curs.fetchall()    
    print("Index"+5*" "+"Flightno1"+1*" "+"Flightno2"+1*" "+"Flightno3"+1*" "+"src"+7*" "+"dst"+7*" "+"Dep_time"+2*" "+"Arr_time"+2*" "+"layover"+3*" "+"price"+5*" "+"seat1"+5*" "+"fare1"+5*" "+"seat2"+5*" "+"fare2"+5*" "+"seat3"+5*" "+"fare3"+5*" "+"no_stop")
    for i, a in enumerate(flight):
		    print(str(i + 1) + (10-len(str(i + 1)))*' ' +a[0] +(10-len(a[0]))*' ' + str(a[1]) + (10-len(str(a[1])))*' ' + str(a[2]) + (10-len(str(a[2])))*' '+ str(a[4]) + (10-len(str(a[4])))*' '+ str(a[5]) + (10-len(str(a[5])))*' '+ str(a[6]) +(10-len(str(a[6])))*' '+ str(a[7]) + (10-len(str(a[7])))*' '+ str(a[8])+(10-len(str(a[8])))*' '+ str(a[9])+(10-len(str(a[9])))*' '+ str(a[10])+(10-len(str(a[10])))*' '+str(a[11])+(10-len(str(a[11])))*' '+ str(a[12])+(10-len(str(a[12])))*' '+ str(a[13])+(10-len(str(a[13])))*' '+ str(a[14])+(10-len(str(a[14])))*' '+ str(a[15])+(10-len(str(a[15])))*' '+ str(a[16]))
    return flight
