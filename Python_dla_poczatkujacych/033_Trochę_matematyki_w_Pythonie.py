f_smaller = 3.141592653589793
f_bigger = 3.87756392764

print(f_smaller, f_bigger)
print("\n")

print(int(f_smaller), int(f_bigger))
print("\n")

print(abs(f_smaller), abs(-f_smaller))
print("\n")

print(round(f_smaller, 2), round(f_bigger, 2), round(f_bigger, 3))
print("\n")

print(min(f_smaller, f_bigger), max(f_smaller, f_bigger))
print("\n")

list = [1, 2, 3, 4, 5, 4, 4, 5, 4]

print(sum(list), len(list))
print("\n")

print(sum(list)/len(list))
print("\n")

print(round(2.675, 2))

print('-------------------------------------------------')

# Trochę matematyki w Pythonie - LAB

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal', 'United Kingdom', 'Serbia', 'Germany', 'Albania',
             'France', 'Czech Republic', 'Denmark', 'Australia', 'Finland', 'Bulgaria',
             'Moldova', 'Sweden', 'Hungary', 'Israel', 'Netherlands', 'Ireland',
             'Cyprus', 'Italy']

sumOfPoints = 4988

print("min: ", min(percent), "max: ", max(percent))

for a in range(len(countries)):
    print(percent[a], int(percent[a]), round(percent[a], 2), int(round(percent[a]*sumOfPoints/100,0)), countries[a])

print('-------------------------------------------------')
