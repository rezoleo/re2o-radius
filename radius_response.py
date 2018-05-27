# encoding=utf8

class RadiusResponse:
    @staticmethod
    def send(is_mac_authorized):
        if is_mac_authorized:
            vlan = 128
        else:
            vlan = 42
        print('Tunnel-type=VLAN,')
        print('Tunnel-Medium-Type= IEEE-802,')
        print('Tunnel-Private-Group-ID="{vlan}"'.format(vlan=vlan))
