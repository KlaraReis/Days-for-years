num_one,num_two,num_three=map(int,input("coloque os tres numeros").split(" "))
if(num_one<num_two and num_one<num_three):
    print("{}  O menor".format(num_one))
elif (num_two<num_three):
    print("{} O menor".format(num_two))
else:
    print("{} O menor".format(num_three))
