#search room location in Leuphana

def leuphana( campus, building_num , floor_num, room_num ):
    input("Please enter your area code accordingly \nCampus(Capital), Building Number , Floor Number, Room number")

    if campus == 'HMS':
        print('Hamburg Media School' +','+ 'building {}'.format(building_num) +','+ 'floor {}'.format(floor_num) +','+ 'room {}'.format(room_num))
    elif campus == 'C':
        print('Main Campus' + ','+ 'building {}'.format(building_num) + ',' + 'floor {}'.format(floor_num) + ',' + 'room {}'.format(room_num))
    elif campus == 'VA':
        print('Volgershall / Altbau' + ','+ 'building {}'.format(building_num) + ',' + 'floor {}'.format(floor_num) + ',' + 'room {}'.format(room_num))
    elif campus == 'V':
        print('Volgershall / Neubau' + ','+ 'building {}'.format(building_num) + ',' + 'floor {}'.format(floor_num) + ',' + 'room {}'.format(room_num))
    elif campus == 'W':
        print('Rotes Feld / Wilschenbrucher Weg 84' + ','+ 'building {}'.format(building_num) + ',' + 'floor {}'.format(floor_num) + ',' + 'room {}'.format(room_num))
    elif campus == 'P':
        print('Rotes Feld / Wilschenbrucher  Weg  69 (Pavillon)' + ','+ 'building {}'.format(building_num) + ',' + 'floor {}'.format(floor_num) + ',' + 'room {}'.format(room_num))
    else:
        print('Input Error: No location found')

#Additional Help
        message = float(input("if you need more help, please type: 1 "))
        if message == 1:
            print('please contact the following offices:')
            offices = ['Head of office', 'Administrative Assistant','International Coordinator']
            name = [ 'Sabine Busse', 'Carola Pellenwessel','Eva-Maria Voßhagen']
            phone = ['+49.4131.677-1071','+49.4131.677-1070','+49.4131.677-1073']
            email = ['sabine.busse@uni.leuphana.de', 'carola.pellenwessel@uni.leuphana.de',' eva.vosshagen@uni.leuphana.de']

            i = 0
            while i < 3:
                print(offices[i])
                staff = {"name": name[i], "phone" : phone[i], "email": email[i]}
                print(staff["name"])
                print(staff["phone"])
                print(staff["email"])
                i +=1


leuphana('k',7,3,9)
