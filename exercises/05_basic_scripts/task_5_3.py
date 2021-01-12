access_template = [
    "switchport mode access", 
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}"
]

#x = str(access_template)
#y = str(trunk_template)

md_inter = input('Введите режим работы интерфеса (access/trunk): ')
inter = input('Введите тип и номер интерфейса: ')
vl = input('Введите номер влан(ов): ')
mode_interface = {
    "access" :  f"interface {inter} \nswitchport mode access \nswitchport access vlan {vl}\nswitchport nonegotiate\nspanning-tree portfast\nspanning-tree bpduguard enable\n",
    "trunk"  :  f"interface {inter} \nswitchport trunk encapsulation dot1q \nswitchport mode trunk \nswitchport trunk allowed vlan {vl}\n"
}

#md_inter = input('Введите режим работы интерфеса (access/trunk): ')
#inter = input('Введите тип и номер интерфейса: ')




#md_inter = input('Введите режим работы интерфеса (access/trunk): ')
#inter = input('Введите тип и номер интерфейса: ')

print(mode_interface[md_inter])
#type_num_int = input('Введите тип и номер интерфейса: ')

#um_vlan = input('Введите номер влан(ов): ')






