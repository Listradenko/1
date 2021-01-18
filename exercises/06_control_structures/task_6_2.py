ip_add = input('Введите ip-адрес в формате 10.0.1.1  : ')

ip_list = ip_add.split('.')

int_ip = [int(ip_list[0],10),int(ip_list[1],10),int(ip_list[2],10),int(ip_list[3],10)]

if (int_ip[0] > 1 and int_ip[0] < 223):
    print('unicast')
elif (int_ip[0] > 224 and int_ip[0] < 239):
    print('multicast')
elif (int_ip[0] == 255 and int_ip[1] == 255 and int_ip[2] == 255 and int_ip[3] == 255):
    print('local broadcast')
elif (int_ip[0] == 0 and int_ip[1] == 0 and int_ip[2] == 0 and int_ip[3] == 0):
    print('unassigned')
else:
    print('unused')
