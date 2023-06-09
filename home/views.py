from django.shortcuts import HttpResponse, render
from home.models import Fare, Kochi_fare, Jaipur_fare, Nagpur_fare
import home.graph as graph


def home(request):
    return render(request, 'home.html')


def add(request):
    return render(request, 'add.html')


def adding(request):
    if request.method == 'GET':
        nam = request.GET.get('name', "")
        value1 = request.GET.get('string', "")
    print(value1)
    ans = value1.strip()
    txt = ans.rsplit(" ")
    print(txt)

    set = Nagpur_fare(station_name=nam, khp=txt[0], nap=txt[1], sap=txt[2], aip=txt[3], ujn=txt[4], jpn=txt[5], cps=txt[6], ajs=txt[7],
                      rhc=txt[8], cgn=txt[9], stb=txt[10], zm=txt[11], kcp=txt[12], gdg=txt[13], kdc=txt[14], nrr=txt[15], aus=txt[16], lmn=txt[
                          17], ban=txt[18], vdn=txt[19], rrr=txt[20], sbn=txt[21], dpc=txt[22], lds=txt[23], sns=txt[24], ioe=txt[25],
                      jrs=txt[26], nps=txt[28], dvs=txt[29], ags=txt[30], cts=txt[31], tpe=txt[32], abs=txt[33], vns=txt[34], pjn=txt[35])
    set.save()
    return render(request, 'adding.html')


def kanpur(request):
    return render(request, 'kanpurfare.html')


def jaipurfare(request):
    return render(request, 'jaipurfare.html')


def jaipurresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")

    print(value1)
    print(value2)
    dict2 = {'Mansarovar': 0, 'New_Aatish_Market': 1, 'Vivek_Vihar': 2, 'Shayam_Nagar': 3, 'Ram_Nagar': 4, 'Civil_Lines': 5,
             'Jaipur_Metro_Station': 6, 'Sindhi_Camp': 7, 'Chandpole': 8, 'Chhoti_Chaupar': 9, 'Badi_Chaupar': 10}
    jpm = Jaipur_fare.objects.all()
    string = "jpm[dict2.get(value1)]." + value2
    fare2 = eval(string)  # fare

    #myresult = mycursor.fetchall()
    # print(myresult[0][0])
    #result = myresult[0][0]

    list7 = ['Mansarovar', 'New_Aatish_Market', 'Vivek_Vihar', 'Shayam_Nagar', 'Ram_Nagar',
             'Civil_Lines', 'Jaipur_Metro_Station', 'Sindhi_Camp', 'Chandpole', 'Chhoti_Chaupar', 'Badi_Chaupar']
    list8 = ['Badi_Chaupar', 'Chhoti_Chaupar', 'Chandpole', 'Sindhi_Camp', 'Jaipur_Metro_Station',
             'Civil_Lines', 'Ram_Nagar', 'Shayam_Nagar', 'Vivek_Vihar', 'New_Aatish_Market', 'Mansarovar']
    list5 = []
    list6 = []
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])

    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)

    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)

    no1 = len(list9)  # length of list for stations up
    no2 = len(list10)  # station down

    list11 = []
    list12 = []
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)

    context = {'value1': value3, 'value2': value4, 'list9': list11,
               'list10': list12, 'result': fare2, 'no1': no1, 'no2': no2}
    return render(request, 'jaipurresult.html', context)


def result(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    # mydb.reconnect()
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT "+value1+" FROM kanpur_fare WHERE STATIONS = '"+value2+"';")
    dict1 = {'IIT_Kanpur': 8, 'Kalyanpur': 7, 'SPM_Hospital': 6, 'Vishwavidyalay': 5,
             'Gurudev_Chauraha': 4, 'Geeta_Nagar': 3, 'Rawatpur': 2, 'Lala_Lajpat_Rai_Hospital': 1, 'Motijheel': 0}
    aks = Fare.objects.all()
    string = "aks[dict1.get(value1)]." + value2
    fare1 = eval(string)  # fare

    #myresult = mycursor.fetchall()
    # print(myresult[0][0])
    #result = myresult[0][0]

    list7 = ['IIT_Kanpur', 'Kalyanpur', 'SPM_Hospital', 'Vishwavidyalay',
             'Gurudev_Chauraha', 'Geeta_Nagar', 'Rawatpur', 'Lala_Lajpat_Rai_Hospital', 'Motijheel']
    list8 = ['Motijheel', 'Lala_Lajpat_Rai_Hospital', 'Rawatpur', 'Geeta_Nagar',
             'Gurudev_Chauraha', 'Vishwavidyalay', 'SPM_Hospital', 'Kalyanpur', 'IIT_Kanpur']
    list5 = []
    list6 = []
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])

    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)

    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)

    no1 = len(list9)  # length of list for stations up
    no2 = len(list10)  # station down

    list11 = []
    list12 = []
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)

    context = {'value1': value3, 'value2': value4, 'list9': list11,
               'list10': list12, 'result': fare1, 'no1': no1, 'no2': no2}

    return render(request, 'result.html', context)


def nagpurfare(request):
    return render(request, 'nagpurfare.html')


def nagpurresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")

    cnt = []
    intc = "No interchange"
    print(value1)
    print(value2)
    fare_list = Nagpur_fare.objects.filter(station_name=value1).values(value2)
    dict1 = fare_list[0].values()
    price = list(dict1)[0]
    print(result)

    aqua = ['pjn', 'vns', 'abs', 'tpe', 'cts', 'ags', 'dvs', 'nps', 'stb',
            'jrs', 'ioe', 'sns', 'lds', 'dpc', 'sbn', 'rrr', 'vdn', 'ban', 'lmn']  # east to west
    aqua_rev = ['lmn', 'ban', 'vdn', 'rrr', 'sbn', 'dpc', 'lds', 'sns', 'ioe',
                'jrs', 'stb', 'nps', 'dvs', 'ags', 'cts', 'tpe', 'abs', 'vns', 'pjn']  # west to east
    org = ['khp', 'nap', 'sap', 'aip', 'ujn', 'jpn', 'cps', 'ajs',
           'rhc', 'cgn', 'stb', 'zm', 'kcp', 'gdg', 'kdc', 'nrr', 'aus']  # south to north
    org_rev = ['aus', 'nrr', 'kdc', 'gdg', 'kcp', 'zm', 'stb', 'cgn',
               'rhc', 'ajs', 'cps', 'jpn', 'ujn', 'aip', 'sap', 'nap', 'khp']  # north to south

    ########################################################################
    if value1 in aqua and value2 in aqua[aqua.index(value1):]:
        for i in range(aqua.index(value1), aqua.index(value2)+1):
            cnt.append(aqua[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    # north
    elif value1 in aqua[0:aqua.index('stb')] and value2 in org[org.index('stb'):]:
        for i in range(aqua.index(value1), aqua.index('stb')):
            cnt.append(aqua[i])
        for j in range(org.index('stb'), org.index(value2)+1):
            cnt.append(org[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in aqua[0:aqua.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
        for i in range(aqua.index(value1), aqua.index('stb')):
            cnt.append(aqua[i])
        for j in range(org_rev.index('stb'), org_rev.index(value2)+1):
            cnt.append(org_rev[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
########################################################################

#######################################################################
    if value1 in aqua_rev and value2 in aqua_rev[aqua_rev.index(value1):]:
        for i in range(aqua_rev.index(value1), aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    # north
    elif value1 in aqua_rev[0:aqua_rev.index('stb')] and value2 in org[org.index('stb'):]:
        for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
            cnt.append(aqua_rev[i])
        for j in range(org.index('stb'), org.index(value2)+1):
            cnt.append(org[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in aqua_rev[0:aqua_rev.index('stb')] and value2 in org_rev[org_rev.index('stb'):]:
        for i in range(aqua_rev.index(value1), aqua_rev.index('stb')):
            cnt.append(aqua_rev[i])
        for j in range(org_rev.index('stb'), org_rev.index(value2)+1):
            cnt.append(org_rev[j])
            intc = "Interchange train from Sitabuldi EW Corridor to Sitabuldi NS Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
####################################################################################

########################################################################################
    if value1 in org and value2 in org[org.index(value1):]:
        for i in range(org.index(value1), org.index(value2)+1):
            cnt.append(org[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    elif value1 in org[0:org.index('stb')] and value2 in aqua[aqua.index('stb'):]:  # west
        for i in range(org.index(value1), org.index('stb')):
            cnt.append(org[i])
        for j in range(aqua.index('stb'), aqua.index(value2)+1):
            cnt.append(aqua[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    elif value1 in org[0:org.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:  # east
        for i in range(org.index(value1), org.index('stb')):
            cnt.append(org[i])
        for j in range(aqua_rev.index('stb'), aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
#####################################################################################

##########################################################################################
    elif value1 in org_rev and value2 in org_rev[org_rev.index(value1):]:
        for i in range(org_rev.index(value1), org_rev.index(value2)+1):
            cnt.append(org_rev[i])
        stn_btw = cnt[1:-1]
        stnbtw_count = len(stn_btw)
        lststn_count = len(cnt[1:])

    # west
    elif value1 in org_rev[0:org_rev.index('stb')] and value2 in aqua[aqua.index('stb'):]:
        for i in range(org_rev.index(value1), org_rev.index('stb')):
            cnt.append(org_rev[i])
        for j in range(aqua.index('stb'), aqua.index(value2)+1):
            cnt.append(aqua[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])

    # east
    elif value1 in org_rev[0:org_rev.index('stb')] and value2 in aqua_rev[aqua_rev.index('stb'):]:
        for i in range(org_rev.index(value1), org_rev.index('stb')):
            cnt.append(org_rev[i])
        for j in range(aqua_rev.index('stb'), aqua_rev.index(value2)+1):
            cnt.append(aqua_rev[j])
            intc = "Interchange train from Sitabuldi NS Corridor to Sitabuldi EW Corridor"
            stn_btw = cnt[1:-1]
            stnbtw_count = len(stn_btw)
            lststn_count = len(cnt[1:])
###################################################################################

    stn_dict = {'pjn': 'Prajapati Nagar', 'vns': 'Vaishnodevi Square', 'abs': 'Ambedkar Square', 'tpe': 'Telephone Exchange', 'cts': 'Chitroli Square', 'ags': 'Agrasen Square', 'dvs': 'Dosar Vaishya Square', 'nps': 'Nagpur Railway Station', 'stb': 'Sitabuldi', 'jrs': 'Jhansi Rani Square', 'ioe': 'Institution of Engineers', 'sns': 'Shankar Nagar Square', 'lds': 'LAD Square', 'dpc': 'Dharampeth College', 'sbn': 'Subhash Nagar Square', 'rrr': 'Rachana Ring Road Junction',
                'vdn': 'Vasudev Nagar', 'ban': 'Bansi Nagar', 'lmn': 'Lokmanya Nagar', 'khp': 'Khapri', 'nap': 'New Airport', 'sap': 'Airport South', 'aip': 'Airport', 'ujn': 'Ujjwal Nagar', 'jpn': 'Jaiprakash Nagar', 'cps': 'Chhatrapati Square', 'ajs': 'Ajni Square', 'rhc': 'Rahate Colony', 'cgn': 'Congress Nagar', 'zm': 'Zero Mile Freedom Park', 'kcp': 'Kasturchand Park', 'gdg': 'Gaddigodam Square', 'kdc': 'Kadbi Square', 'nrr': 'Nari Road', 'aus': 'Automotive Square', 'iew': 'Interchange to Sitabuldi EW Corridor', 'ins': 'Interchange to Sitabuldi NS Corridor'}
    cnt1 = []
    stnbtw_new = []
    for i in cnt:
        cnt1.append(stn_dict.get(i))
    for i in stn_btw:
        stnbtw_new.append(stn_dict.get(i))
    print(stnbtw_new)
    print(stnbtw_count)
    print(lststn_count)
    new_value1 = stn_dict.get(value1)
    new_value2 = stn_dict.get(value2)
    # fare

    context = {'value1': new_value1, 'value2': new_value2,
               'list': stnbtw_new, 'no': stnbtw_count, 'intc': intc, 'fare': price}
    return render(request, 'nagpurresult.html', context)


def kochifare(request):
    return render(request, 'kochifare.html')


def kochiresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")
    # mydb.reconnect()
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT "+value1+" FROM kanpur_fare WHERE STATIONS = '"+value2+"';")
    print(value1)
    print(value2)
    dict1 = {'Aluva': 0, 'Pulinchodu': 1, 'Companypady': 2, 'Ambattukavu': 3, 'Muttom': 4, 'Kalamassery': 5, 'Cochin_University': 6, 'Pathadipalam': 7, 'Edapally': 8, 'Changampuzha': 9, 'Palarivattom': 10, 'JLN_Stadium': 11,
             'Kaloor': 12, 'Lissie': 13, 'MG_Road': 14, 'Maharajas': 15, 'Ernakulam_South': 16, 'Kadavanthra': 17, 'Elamkulam': 18, 'Vytilla': 19, 'Thaikoodam': 20, 'Petta': 21, 'Vadakkekotta': 22, 'SN_Junction': 23}
    lkh = Kochi_fare.objects.all()
    string = "lkh[dict1.get(value1)]." + value2
    fare = eval(string)  # fare

    #myresult = mycursor.fetchall()
    # print(myresult[0][0])
    #result = myresult[0][0]

    list7 = ['Aluva', 'Pulinchodu', 'Companypady', 'Ambattukavu', 'Muttom', 'Kalamassery', 'Cochin_University', 'Pathadipalam', 'Edapally', 'Changampuzha', 'Palarivattom',
             'JLN_Stadium', 'Kaloor', 'Lissie', 'MG_Road', 'Maharajas', 'Ernakulam_South', 'Kadavanthra', 'Elamkulam', 'Vytilla', 'Thaikoodam', 'Petta', 'Vadakkekotta', 'SN_Junction']
    list8 = ['SN_Junction', 'Vadakkekotta', 'Petta', 'Thaikoodam', 'Vytilla', 'Elamkulam', 'Kadavanthra', 'Ernakulam_South', 'Maharajas', 'MG_Road', 'Lissie', 'Kaloor',
             'JLN_Stadium', 'Palarivattom', 'Changampuzha', 'Edapally', 'Pathadipalam', 'Cochin_University', 'Kalamassery', 'Muttom', 'Ambattukavu', 'Companypady', 'Pulinchodu', 'Aluva']
    list5 = []
    list6 = []
    list9 = []
    list10 = []
    for i in range(list7.index(value1)+1, len(list7)):
        list5.append(list7[i])

    if value2 in list5:
        print(list5)
        list9 = list5[:list5.index(value2)]
        print(list9)

    else:
        for i in range(list8.index(value1)+1, len(list8)):
            list6.append(list8[i])
        print(list6)
        list10 = list6[:list6.index(value2)]
        print(list10)

    no1 = len(list9)  # length of list for stations up
    no2 = len(list10)  # station down

    list11 = []
    list12 = []
    for i in list9:
        temp1 = i.split("_")
        list11.append(" ".join(temp1))
    print(list11)

    for i in list10:
        temp2 = i.split("_")
        list12.append(" ".join(temp2))
    print(list12)

    temp3 = value1.split("_")
    value3 = " ".join(temp3)

    temp4 = value2.split("_")
    value4 = " ".join(temp4)

    context = {'value1': value3, 'value2': value4, 'list9': list11,
               'list10': list12, 'result': fare, 'no1': no1, 'no2': no2}
    return render(request, 'kochiresult.html', context)


def chennaifare(request):
    return render(request, 'chennaifare.html')


def chennairesult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")

    print(value1)
    print(value2)

    routes = {
        ('aip', 'mnb'),
        ('mnb', 'aip'),
        ('mnb', 'ngn'),
        ('ngn', 'mnb'),
        ('ngn', 'ald'),
        ('ald', 'ngn'),
        ('ald', 'ekt'),
        ('ekt', 'ald'),
        ('ekt', 'asn'),
        ('asn', 'ekt'),
        ('asn', 'vdp'),
        ('vdp', 'asn'),
        ('vdp', 'arb'),
        ('arb', 'vdp'),
        ('arb', 'cmbt'),
        ('cmbt', 'arb'),
        ('cmbt', 'kym'),
        ('kym', 'cmbt'),
        ('kym', 'trm'),
        ('trm', 'kym'),
        ('trm', 'ant'),
        ('ant', 'trm'),
        ('ant', 'ane'),
        ('ane', 'ant'),
        ('ane', 'snn'),
        ('snn', 'ane'),
        ('snn', 'pyp'),
        ('pyp', 'snn'),
        ('pyp', 'klp'),
        ('klp', 'pyp'),
        ('klp', 'nhp'),
        ('nhp', 'klp'),
        ('nhp', 'egm'),
        ('egm', 'nhp'),
        ('egm', 'mgr'),
        ('mgr', 'egm'),
        ('mgr', 'hgc'),
        ('hgc', 'mgr'),
        ('hgc', 'mnd'),
        ('mnd', 'hgc'),
        ('mnd', 'wmp'),
        ('wmp', 'mnd'),
        ('wmp', 'tgy'),
        ('tgy', 'wmp'),
        ('tgy', 'tdp'),
        ('tdp', 'tgy'),
        ('tdp', 'nwm'),
        ('nwm', 'tdp'),
        ('nwm', 'tgm'),
        ('tgm', 'nwm'),
        ('tgm', 'kdm'),
        ('kdm', 'tgm'),
        ('kdm', 'tvm'),
        ('tvm', 'kdm'),
        ('tvm', 'wim'),
        ('wim', 'tvm'),
        ('mgr', 'ges'),
        ('ges', 'mgr'),
        ('ges', 'lic'),
        ('lic', 'ges'),
        ('lic', 'tsl'),
        ('tsl', 'lic'),
        ('tsl', 'dms'),
        ('dms', 'tsl'),
        ('dms', 'tyn'),
        ('tyn', 'dms'),
        ('tyn', 'ndm'),
        ('ndm', 'tyn'),
        ('ndm', 'sdp'),
        ('sdp', 'ndm'),
        ('sdp', 'ltm'),
        ('ltm', 'sdp'),
        ('ltm', 'gdy'),
        ('gdy', 'ltm'),
        ('gdy', 'ald'),
        ('ald', 'gdy'),
        ('ald', 'stm'),
        ('stm', 'ald')
    }
    dict1 = {'ald': 'Alandur', 'aip': 'Airport', 'mnb': 'Meenambakkam Metro', 'ngn': 'Nanganallur Road', 'ekt': 'Ekkatutthangal', 'asn': 'Ashok Nagar', 'vdp': 'Vadapalani', 'arb': 'Arumbakkam', 'cmbt': 'CMBT Metro Station', 'kym': 'Koyambedu', 'trm': 'Thirumangalam', 'ant': 'Anna Nagar Tower', 'ane': 'Anna Nagar East', 'snn': 'Shenoy Nagar', 'pyp': 'Pachaiyappa', 'klp': 'Kilpauk',
             'nhp': 'Nehru Park', 'egm': 'Egmore Metro', 'mgr': 'Puratchi Thalaivar Dr. MG Ramachandran Central Metro', 'hgc': 'High Court', 'mnd': 'Mannadi', 'wmp': 'Washermanpet', 'tgy': 'Thigayaraya College Metro', 'tdp': 'Tondiarpet Metro', 'nwm': 'New Washermanpet Metro', 'tgm': 'Tollgate Metro', 'kdm': 'Kaladipet Metro', 'tvm': 'Thiruvotriyur Metro', 'wim': 'Wimco Nagar Metro', 'ges': 'Government Estate', 'lic': 'LIC', 'tsl': 'Thousand Light', 'dms': 'AG-DMS', 'tyn': 'Teynampet', 'ndm': 'Nandanam', 'sdp': 'Saidapet', 'ltm': 'Little Mount', 'gdy': 'Guindy', 'stm': 'St Thomas Mount'}
    g = graph.Graph(routes)
    start = value1
    end = value2
    exactroute = g.getshortestpath(start, end)
    namestn = []
    for i in exactroute:
        namestn.append(dict1[i])
    print(namestn)
    change = ''
    if 'Alandur' in namestn:
        index = namestn.index('Alandur')
        if namestn[index-1] == 'St Thomas Mount' and namestn[index+1] == 'Ekkatutthangal':
            change = 'From Alandur, No need to Change trains'
        elif namestn[index-1] == 'St Thomas Mount' and namestn[index+1] == 'Guindy':
            change = 'From Alandur, Change trains from green line to blue line'
        elif namestn[index-1] == 'Nanganallur Road' and namestn[index+1] == 'Guindy':
            change = 'From Alandur, Change to blue line'
        elif namestn[index-1] == 'Nanganallur Road' and namestn[index+1] == 'Ekkatutthangal':
            change='From Alandur, change trains to grey line'
        elif namestn[index-1] == 'Ekkatutthangal' and namestn[index+1] == 'Nanganallur Road':
            change = 'From Alandur, change to Grey line'
        elif namestn[index-1] == 'Ekkatutthangal' and namestn[index+1] == 'St Thomas Mount':
            change = 'From Alandur, change to Green line'
        elif namestn[index-1] == 'Guindy' and namestn[index+1] == 'Nanganallur Road':
            change = 'From Alandur, No need to change trains'
        elif namestn[index-1] == 'Guindy' and namestn[index+1] == 'St Thomas Mount':
            change = 'From Alandur, Change to green line'
            
    change2 = ''
    if 'Puratchi Thalaivar Dr. MG Ramachandran Central Metro' in namestn:
        index = namestn.index('Puratchi Thalaivar Dr. MG Ramachandran Central Metro')
        if namestn[index-1] == 'Egmore Metro' and namestn[index+1] == 'High Court':
            change2 = 'From Central Metro, change to blue line'
        if namestn[index-1]=='Government Estate' and namestn[index+1] == 'High Court':
            change2 = 'From Central Metro, No need to change trains'
        if namestn[index-1] == 'High Court' and namestn[index+1] == 'Egmore Metro':
            change2 = 'From Central Metro, Change to green or grey line'
        if namestn[index-1] == 'High Court' and namestn[index+1] == 'Government Estate':
            change2 = 'From Central Metro, No need to change trains'
        if namestn[index-1] == 'Government Estate' and namestn[index+1] == 'Egmore Metro':
            change2 = 'From Central Metro, Change to green or grey line'
        if namestn[index-1] == 'Egmore Metro' and namestn[index+1] == 'Government Estate':
            change2 = 'From Central Metro, Change to blue line'


    
    first_stn = namestn[0]
    last_stn = namestn[-1]
    namestn.pop(0)
    namestn.pop(-1)
    org = dict[value1]
    dst = dict[value2]
    if len(namestn)+1 <= 1:
        fare = 10
    elif len(namestn)+1 ==2:
        fare = 20
    elif len(namestn)+1 == 3:
        fare = 30
    elif 4 <= len(namestn)+1 <= 8:
        fare = 40
    elif 9 <= len(namestn)+1 <= 13:
        fare = 50
    elif len(namestn) >=14:
        fare = 60
    else:
        fare = 0
        

    
    
    context = {'firststn': first_stn, 'laststn': last_stn, 'stn_in_btw': len(
        namestn), 'org': first_stn, 'dst': last_stn, 'list': namestn, 'fare': fare, 'change':change, 'change2':change2}

    return render(request, 'chennaifareresult.html', context)

def hyderabadfare(request):
    return render(request,'hyderabadfare.html')

def hyderabadresult(request):
    if request.method == 'GET':
        value1 = request.GET.get('origin', "")
        value2 = request.GET.get('dest', "")

    print(value1)
    print(value2)

    routes = {
    ("RDG", "HTC"),
    ("HTC", "RDG"),
    ('HTC', 'DGC'),
    ("DGC", "HTC"),
    ("DGC", "MDP"),
    ("MDP", "DGC"),
    ("MDP", "PDG"),
    ('PDG', 'JHC'),
    ('PDG', 'MDP'),
    ('JHC', 'PDG'),
    ('JHC', 'RJH'),
    ('RJH', 'JHC'),
    ('RJH', 'GCS'),
    ('GCS', 'RJH'),
    ('GCS', 'MDN'),
    ('MDN', 'GCS'),
    ('MDN', 'AMR'),
    ('AMR', 'MDN'),
    ('AMR', 'SRN'),
    ('AMR', 'BGM'),
    ('AMR', 'PJG'),
    ('BGM', 'AMR'),
    ('BGM', 'PKN'),
    ('PKN', 'BGM'),
    ('PKN', 'RSL'),
    ('RSL', 'PKN'),
    ('RSL', 'PRD'),
    ('PRD', 'RSL'),
    ('PRD', 'PRG'),
    ('PRG', 'PRD'),
    ('PRG', 'SEM'),
    ('SEM', 'PRG'),
    ('SEM', 'MTG'),
    ('MTG', 'SEM'),
    ('MTG', 'TNK'),
    ('TNK', 'MTG'),
    ('TNK', 'HBS'),
    ('HBS', 'TNK'),
    ('HBS', 'NGR'),
    ('NGR', 'HBS'),
    ('NGR', 'STD'),
    ('STD', 'NGR'),
    ('STD', 'UPL'),
    ('UPL', 'STD'),
    ('UPL', 'NGL'),
    ('NGL', 'UPL'),
    ('MYP', 'JNC'),
    ('JNC', 'KPH'),
    ('JNC', 'MYP'),
    ('KPH', 'KTP'),
    ('KPH', 'JNC'),
    ('KTP', 'KPH'),
    ('KTP', 'BLN'),
    ('BLN', 'KTP'),
    ('BLN', 'MSP'),
    ('MSP', 'BLN'),
    ('MSP', 'BRN'),
    ('BRN', 'MSP'),
    ('BRN', 'ERG'),
    ('ERG', 'BRN'),
    ('ERG', 'ESI'),
    ('ESI', 'ERG'),
    ('ESI', 'SRN'),
    ('SRN', 'ESI'),
    ('SRN', 'AMR'),
    ('PJG', 'AMR'),
    ('PJG', 'IMM'),
    ('IMM', 'PJG'),
    ('IMM', 'KRT'),
    ('KRT', 'IMM'),
    ('KRT', 'LKD'),
    ('LKD', 'KRT'),
    ('LKD', 'ASM'),
    ('ASM', 'LKD'),
    ('ASM', 'NMP'),
    ('NMP', 'ASM'),
    ('NMP', 'GDB'),
    ('GDB', 'NMP'),
    ('GDB', 'OMC'),
    ('OMC', 'GDB'),
    ('OMC', 'MGB'),
    ('MGB', 'OMC'),
    ('MGB', 'SLB'),
    ('MGB', 'MKP'),
    ('MKP', 'MGB'),
    ('MKP', 'NMR'),
    ('NMR', 'MKP'),
    ('NMR', 'MRB'),
    ('MRB', 'NMR'),
    ('MRB', 'DSK'),
    ('DSK', 'MRB'),
    ('DSK', 'CMS'),
    ('CMS', 'DSK'),
    ('CMS', 'VML'),
    ('VML', 'CMS'),
    ('VML', 'LBN'),
    ('LBN', 'VML'),
    ('JBS', 'PRG'),
    ('PRG', 'JBS'),
    ('PRG','SCW'),
    ('SCW','PRG'),
    ('SCW', 'GHP'),
    ('GHP', 'SCW'),
    ('GHP', 'MSH'),
    ('MSH', 'GHP'),
    ('MSH', 'RTC'),
    ('RTC', 'MSH'),
    ('RTC', 'CKD'),
    ('CKD', 'RTC'),
    ('CKD', 'NYN'),
    ('NYN', 'CKD'),
    ('NYN', 'SLB'),
    ('SLB', 'NYN'),
    
    
    }

    dict2 = {'RDG': 'Raidurg', 'HTC': 'HITEC City', 'DGC': 'Durgam Cheruvu', 'MDP': 'Madhapur', 'PDG': 'Peddamma Gudi', 'JHC': 'Jubilee Hills Check Post', 'RJH': 'Road No. 5 Jubilee Hills', 'GCS': 'Yusufguda', 'MDN': 'Madhura Nagar', 'AMR': 'Ameerpet', 'SRN': 'S R Nagar', 'BGM': 'Begumpet', 'PJG': 'Panjagutta', 'PKN': 'Prakash Nagar', 'RSL': 'Rasoolpura', 'PRD': 'Paradise', 'PRG': 'Parade Ground', 'SEM': 'Secunderabad East Metro Station', 'MTG': 'Mettuguda', 'TNK': 'Tarnaka', 'HBS': 'Habsiguda', 'NGR': 'Ngri', 'STD': 'Stadium', 'UPL': 'Uppal', 'NGL': 'Nagole', 'MYP': 'Miyapur', 'JNC': 'JNTU College', 'KPH': 'KPHB Colony', 'KTP': 'Kukatpally',
         'BLN': 'Dr. BR Ambedkar Balanagar Metro Station', 'MSP': 'Moosapet', 'BRN': 'Bharat Nagar', 'ERG': 'Erragadda', 'ESI': 'ESI Hospital', 'IMM': 'Irrum Manzil', 'KRT': 'Khairatabad', 'LKD': 'Lakdikapul', 'ASM': 'Assembly', 'NMP': 'Nampally', 'GDB': 'Gandhi Bhavan', 'OMC': 'Osmania Medical College', 'MGB': 'MG Bus Station', 'SLB': 'Sultan Bazaar', 'MKP': 'Malakpet', 'NMR': 'New Market', 'MRB': 'Musarambagh', 'DSK': 'Dilsukhnagar', 'CMS': 'Chaitanyapuri Metro', 'VML': 'Victoria Memorial', 'LBN': 'LB Nagar', 'JBS': 'JBS Parade Ground', 'SCW': 'Secunderabad West', 'GHP': 'Gandhi Hospital', 'MSH': 'Musheerabad', 'RTC': 'RTC X Roads', 'CKD': 'Chikkadpally', 'NYN': 'Narayanaguda'}
    
    
    g = graph.Graph(routes)
    start = value1
    end = value2
    exactroute = g.getshortestpath(start, end)
    namestn = []
    for i in exactroute:
        namestn.append(dict2[i])
    print(namestn)
    change = ''
    if 'Ameerpet' in namestn:
        index = namestn.index('Ameerpet') 
        if (namestn[index-1] == 'Madhura Nagar' and namestn[index+1] == 'S R Nagar') or (namestn[index-1] == 'Madhura Nagar' and namestn[index+1] == 'Panjagutta'):
            change = 'Change from blue line to red line in Ameerpet'
        if (namestn[index-1] == 'Begumpet' and namestn[index+1] == 'S R Nagar') or (namestn[index-1] == 'Begumpet' and namestn[index+1] == 'Panjagutta'):
            change = 'Change from blue line to red line in Ameerpet'
        if (namestn[index-1] == 'S R Nagar' and namestn[index+1] == 'Madhura Nagar') or (namestn[index-1] == 'S R Nagar' and namestn[index+1] == 'Begumpet'):
            change = 'Change from red line to blue line in Ameerpet'
        if (namestn[index-1] == 'Panjagutta' and namestn[index+1] == 'Madhura Nagar') or (namestn[index-1] == 'Panjagutta' and namestn[index+1] == 'Begumpet'):
            change = 'Change from red line to blue line in Ameerpet'

    change2 = ''
    if 'Parade Ground' in namestn:
        index = namestn.index('Parade Ground')
        if (namestn[index-1] == 'JBS Parade Ground' and namestn[index+1] == 'Paradise') or (namestn[index-1] == 'JBS Parade Ground' and namestn[index+1] == 'Secunderabad East Metro Station'):
            change2 = 'Change from green line to blue line in Parade Ground'
        if (namestn[index-1] == 'Secunderabad West' and namestn[index+1] == 'Paradise') or (namestn[index-1] == 'Secunderabad West' and namestn[index+1] == 'Secunderabad East Metro Station'):
            change2 = 'Change from green line to blue line in Parade Ground'
        if (namestn[index-1] == 'Paradise' and namestn[index+1] == 'JBS Parade Ground') or (namestn[index-1] == 'Paradise' and namestn[index+1] == 'Secunderabad West'):
            change = 'Change from blue line to green line in Ameerpet'
        if (namestn[index-1] == 'Secunderabad East Metro Station' and namestn[index+1] == 'JBS Parade Ground') or (namestn[index-1] == 'Secunderabad East Metro Station' and namestn[index+1] == 'Secunderabad West'):
            change = 'Change from blue line to green line in Ameerpet'
    first_stn = namestn[0]
    last_stn = namestn[-1]
    namestn.pop(0)
    namestn.pop(-1)
    org = dict[value1]
    dst = dict[value2]

    if len(namestn)+1 <= 1:
        fare = 10
    elif 2 <= len(namestn)+1 <=4:
        fare = 15
    elif 4<= len(namestn)+1 <=6:
        fare = 25
    elif 6 <= len(namestn)+1 <= 8:
        fare = 30
    elif 8 <= len(namestn)+1 <= 10:
        fare = 35
    elif 10 <= len(namestn)+1 <= 14:
        fare = 40
    elif 14 <= len(namestn)+1 <= 18:
        fare = 45
    elif 18 <= len(namestn)+1 <= 22:
        fare = 50
    elif 22 <= len(namestn)+1 <= 26:
        fare = 55
    else:
        fare = 0

    context = {'firststn': first_stn, 'laststn': last_stn, 'stn_in_btw': len(
        namestn), 'org': first_stn, 'dst': last_stn, 'list': namestn, 'change':change,'change2':change2, 'fare':fare }

    return render(request, 'hyderabadresult.html', context)

def timings(request):
    if request.method == 'GET':
        value1 = request.GET.get('cars1', "")
    #mycursor = mydb.cursor()
    #mycursor.execute("SELECT TRIP1, TRIP2, TRIP3, TRIP4, TRIP5 FROM kanpur_tt WHERE STATIONS = '"+value1+"';")
    #myresult = mycursor.fetchall()
    # print(value1)
    # print(myresult)

    return render(request, 'timings.html')
