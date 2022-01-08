digits = int(input("To what digit do you want pi rounded to up to a million"))
digits += 2
# I added two to make up for the decimal point and the 3
f = open("/home/artemis/vscodefiles/python/pi/pi.txt", "r")
pi = f.readline()
print(pi[0 : digits])
print(len("3.14159265"))