time1 = input ( 'Enter number od seconds :')
rem = int ( time1 ) % 3600
hrs = round(int ( time1 ) / 3600,0)
min = round(rem / 60,0)
sec = min % 60
print ( f"seconds to coverted time is : {hrs} H : {min} M : {sec} S")