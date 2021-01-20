ip_add = input('Введите ip-адрес в формате 10.0.1.1  : ')
count_dot = ip_add.count('.') # получаем кол-во точек в строке
ip_list = ip_add.split('.')
dot1 = ip_add.find('.') # получаем индекс первой точки
dt1 = (dot1+1)
first_bit = ip_add[0:dot1] # получаем первое число 
f_bit = ip_add[0:(dot1)]
second_bit = ip_add[(dt1):] # отрезаем первый бит(число) с точкой от адреса
dot2 = second_bit.find('.') # получаем индекс второй точки
sec_bit = second_bit[0:dot2] # получаем второе число
dt2 = (dot2+1)
third_bit = second_bit[(dt2):] # отрезаем первых два бита адреса с точкой от адреса 
dot3 = third_bit.find('.') # получаем индекс 3 точки
th_bit = third_bit[0:dot3] # получаем 3 число 
dt3 = (dot3+1)
fourth_bit = third_bit[dt3:] # получаем четвертое число
q = len(ip_list)
#ip = False
while True:
    if q != 4:
        print("Неправильный IP-адрес")
    elif (not first_bit.isdigit() or not sec_bit.isdigit() or not th_bit.isdigit() and not fourth_bit.isdigit()):
        print("Неправильный IP-адрес")
    elif (int(first_bit,10) < 0 and int(first_bit,10) >= 255) and (int(sec_bit,10) < 0 and int(sec_bit,10) >= 255) and (int(th_bit,10) < 0 and int(th_bit,10) >= 255) and (int(fourth_bit,10) < 0 and int(fourth_bit,10) >= 255):
        print("Неправильный IP-адрес")
    else:
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
        break
    ip_add = input('Введите ip-адрес в формате 10.0.1.1  : ')
    count_dot = ip_add.count('.') # получаем кол-во точек в строке
    ip_list = ip_add.split('.')
    dot1 = ip_add.find('.') # получаем индекс первой точки
    dt1 = (dot1+1)
    first_bit = ip_add[0:dot1] # получаем первое число 
    f_bit = ip_add[0:(dot1)]
    second_bit = ip_add[(dt1):] # отрезаем первый бит(число) с точкой от адреса
    dot2 = second_bit.find('.') # получаем индекс второй точки
    sec_bit = second_bit[0:dot2] # получаем второе число
    dt2 = (dot2+1)
    third_bit = second_bit[(dt2):] # отрезаем первых два бита адреса с точкой от адреса 
    dot3 = third_bit.find('.') # получаем индекс 3 точки
    th_bit = third_bit[0:dot3] # получаем 3 число 
    dt3 = (dot3+1)
    fourth_bit = third_bit[dt3:] # получаем четвертое число
    q = len(ip_list)