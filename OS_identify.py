#encoding:utf-8
from scapy.all import *
class OS_identify():
    def __init__(self,ip,port):
        self.check_sum_sock = 4
        self.windows = 0
        self.linux = 0
        self.linux3 = 0
        self.win_vista_sock = 0
        self.ip = ip
        self.port = port
    def check(self):
        try:
            syn_packet = IP(dst=self.ip)/TCP(dport=self.port, flags="S")
            response_packet = sr1(syn_packet, timeout=3, verbose=0)
        except Exception as e:
            return False
        if response_packet is not None:
            IP_ = response_packet[IP]
            tcp_flags = response_packet[TCP].flags
            # print(tcp_flags) 
            try:
                match IP_.ttl:
                    case 128:
                        self.windows +=1
                    case 64:
                        self.linux += 1
                        self.linux3 += 1
                        self.win_vista_sock += 1
            except Exception as e:
                pass
            try:
                match IP_.flags:
                    case "DF":
                        self.windows +=1
                        self.linux += 1
                    case _ :
                        self.linux3 += 1
                        self.win_vista_sock += 1
            except Exception as e:
                pass
            try:
                match response_packet[TCP].options[0][1]:
                    case 1380:
                        self.windows +=1
                        self.win_vista_sock += 1
                    case 1460:
                        self.linux += 1
                    case 1414:
                        self.linux3 += 1
            except Exception as e:
                pass
            try:
                match response_packet[TCP].window:
                    case 8192:   
                        self.windows +=1
                        self.win_vista_sock += 1
                    case 5792:
                        self.linux += 1
                    case 32736:
                        self.linux3 += 1
            except Exception as e:
                pass
            # if tcp_flags == 18:
            #     self.linux += 1
            #     self.linux3 += 1
            # elif tcp_flags == 20:
            #     self.windows +=1
            #     self.win_vista_sock += 1
        if (self.windows == 0 )&( self.linux == 0)&(self.linux3 == 0)&(self.win_vista_sock == 0):
            return False
        else:
            return True
    def get_reault(self):  
             
        print("windows vista: {:.2%}".format(self.win_vista_sock/self.check_sum_sock))     
        print("windows 7    : {:.2%}".format(self.windows/self.check_sum_sock))
        print("linux2.6     : {:.2%}".format(self.linux/self.check_sum_sock))   
        print("linux3.0     : {:.2%}".format(self.linux3/self.check_sum_sock))   
        print("mac          : {:.2%}".format(self.mac_sock/self.check_sum_sock))   
        print("openbsd      : {:.2%}".format(self.openbsd_sock/self.check_sum_sock))   
        print("windows vista: {:.2%}".format(self.win_vista_sock/self.check_sum_sock))  
    def return_percent(self):  
        result = {"windows vista":self.win_vista_sock/self.check_sum_sock,
        "windows":self.windows/self.check_sum_sock,
        "linux":self.linux/self.check_sum_sock,
        "linux3.0":self.linux3/self.check_sum_sock,}
        return result
    
    def return_res_max(self):  
        result = {"windows vista":self.win_vista_sock/self.check_sum_sock,
        "windows":self.windows/self.check_sum_sock,
        "linux":self.linux/self.check_sum_sock,
        "linux3.0":self.linux3/self.check_sum_sock,}
        keys = list(result.keys())
        value = []
        for key in keys:
            value.append(result[key])
        max_value = max(value)
        index = value.index(max_value)  
        return keys[index]
        # return()
    def main(self):
        if self.check():
            # self.get_reault()
            most_os = self.return_res_max()
            print(most_os)
            if most_os:
                return most_os
            else:
                return "unknow"
        else:
            # print("[*]未成功进行数据交互，请查看网络配置")
            return "unknow"
                
if __name__ == "__main__":
    ip = sys.argv[1]
    port = sys.argv[2]
    test = OS_identify(ip,int(port))
    test.main()