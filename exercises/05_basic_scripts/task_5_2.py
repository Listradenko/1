ip_add = input('Введите ip-ceти в формате (10.1.1.0/24) : ')

# действия с ip_адресом
ip = ip_add[0:ip_add.find('/')]
ip_list = ip.split('.')
int_ip = [int(ip_list[0],10), int(ip_list[1],10), int(ip_list[2],10), int(ip_list[3],10)]

# действия с маской
mask = ip_add[ip_add.find('/'):] # первая строка для вывода
x = int(mask.replace('/',''),10)
y = (32 - x) # число для уножения на "0"
bit = ("1"*x)+("0"*y) 
oktet1 = bit[0:8] # 1 октет маски слева
oktet2 = bit[8:16] # 2 октет маски
oktet3 = bit[16:24] # 3 oктет
oktet4 = bit[24:32] # 4 октет

list_okt10 = [int(oktet1,2), int(oktet2,2), int(oktet3,2), int(oktet4,2)] # create list mask in decimal

#list_okt2 = [bin(list_okt10[0]), bin(list_okt10[1]), bin(list_okt10[2]) ,bin(list_okt10[3])] # create list mask in binary



print(ip)
print(f"""
Network:
{int_ip[0]:<8} {int_ip[1]:<8} {int_ip[2]:<8} {int_ip[3]:<8}
{int_ip[0]:08b} {int_ip[1]:08b} {int_ip[3]:08b} {int_ip[3]:08b}

Mask:
{mask}
{list_okt10[0]:<8} {list_okt10[1]:<8} {list_okt10[2]:<8} {list_okt10[3]:<8}
{list_okt10[0]:08b} {list_okt10[1]:08b} {list_okt10[2]:08b} {list_okt10[3]:08b}

""")

#print(mask)
#print(bit)





