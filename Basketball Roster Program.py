#!/usr/bin/env python
# coding: utf-8

# In[61]:


print('\t\tWelcome to the BasketBall Roster Program')

point_guard = input('Who is your point guard: ').title()
shooting_guard = input('Who is your shooting guard: ').title()
small_forward = input('Who is your small forward: ').title()
power_forward = input('Who is your power forward: ').title()
center = input('Who is your center: ').title()



# In[62]:


my_list = [point_guard,shooting_guard,small_forward,power_forward,center]

print(f'\t\tYour starting {len(my_list)} for the upcoming basketball season')
print(f'\t\t\tPoint guard:\t{my_list[0]}')
print(f'\t\t\tShooting guard:\t{my_list[1]}')
print(f'\t\t\tSmall Forward:\t{my_list[2]}')
print(f'\t\t\tPower Forward:\t{my_list[3]}')
print(f'\t\t\tCenter:\t\t{my_list[4]}\n')

print(f'Oh No! {my_list[2]} is injured')
my_list.remove(my_list[2])
print(f'Your roster only has {len(my_list)} players')
new_small_forward = input(f'Who will take {small_forward} spot: \n')

my_list.insert(2,new_small_forward)
print(f'\t\tYour starting {len(my_list)} for the upcoming basketball season')
print(f'\t\t\tPoint guard:\t{my_list[0]}')
print(f'\t\t\tShooting guard:\t{my_list[1]}')
print(f'\t\t\tSmall Forward:\t{my_list[2]}')
print(f'\t\t\tPower Forward:\t{my_list[3]}')
print(f'\t\t\tCenter:\t\t{my_list[4]}\n')

print(f'Good Luck {my_list[2]} you will do great \nYour roster now has {len(my_list)} players')


