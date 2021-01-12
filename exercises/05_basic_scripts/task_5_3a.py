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






#inter = 0
vl = 0

md_inter = input('Введите режим работы интерфеса (access/trunk): ')
inter = input('Введите тип и номер интерфейса: ')
mode_interface = {
    "access" : {
        "conf" : f"interface {inter} \nswitchport mode access \nswitchport access vlan {vl}\nswitchport nonegotiate\nspanning-tree portfast\nspanning-tree bpduguard enable\n",
        "text_vla" : "Введите номер VLAN:" 
    },
    
    "trunk" : {
        "conf1" : f"interface {inter} \nswitchport trunk encapsulation dot1q \nswitchport mode trunk \nswitchport trunk allowed vlan {vl}\n",
        "text_vlat" : "Введите разрешенные VLANы"    
    } 
    
}


#keys = list(mode_interface.keys())

#md_inter = input('Введите режим работы интерфеса (access/trunk): ')
#inter = input('Введите тип и номер интерфейса: ')
k = list(mode_interface[md_inter].values()) # список значений словаря
#mode_interface2 = mode_interface.copy()
#k2 = list(mode_interface2[md_inter].keys()) # список значений ключей
vl = input(f'{k[1]} ')

mode_interface2 = {
    "access" : {
        "conf" : f"interface {inter} \nswitchport mode access \nswitchport access vlan {vl}\nswitchport nonegotiate\nspanning-tree portfast\nspanning-tree bpduguard enable\n",
        "text_vla" : "Введите номер VLAN:" 
    },
    
    "trunk" : {
        "conf1" : f"interface {inter} \nswitchport trunk encapsulation dot1q \nswitchport mode trunk \nswitchport trunk allowed vlan {vl}\n",
        "text_vlat" : "Введите разрешенные VLANы"    
    } 
    
}


k2 = list(mode_interface2[md_inter].keys())
print(mode_interface2[md_inter][k2[0]])


#um_vlan = input('Введите номер влан(ов): ')





