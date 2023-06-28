import OS_identify,sys
f = open("ip_os.csv","w",encoding='utf8')
f.write("IP,操作系统\n")
for i in range (0,2):
    for n in range(1,255):
        try:
            list = []
            ip = "198.120."+str(i)+"."+str(n)
            # ip = "198.120."+str(i)+"."+'1'
            test = OS_identify.OS_identify(ip,sys.argv[1])
            os = test.main()
            list.append(ip)
            list.append(os)
            print(list)
            f.write(ip+","+os+"\n")
            # break
        except Exception as e:
            print (e)
            pass
f.close()