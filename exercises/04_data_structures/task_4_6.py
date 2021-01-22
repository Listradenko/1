ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
ospf = ospf_route.replace('[',' ')
osp1 = ospf.replace(']','')
osp2 = osp1.replace('via','')
osq = osp2.replace(',','')
osp = osq.rstrip('')
os = osp.split()

conf = f'''
Prefix                  {os[0]}
AD/Metric               {os[1]}   
Next-hop                {os[2]}
Last update             {os[3]}
Outbound Interface      {os[4]}
'''

print(conf)