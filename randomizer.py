import random

CLASSES =  {                                                                                                                                                                                                                                
    6: [ 'Ayman', 'Shaeq', 'Patrick', 'Yvonne', 'Wilson', 'Brian', 'Farhan', 'Janet', 'Harry', 'Kevin', 'Nicholas', 'Jason', 'Yikai', 'Emma', 'Kenneth', 'Nala', 'Karol', 'Elias', 'Ely', 'Reo', 'Dhriaj', 'Amy', 'Arvind', 'Nobel', 'Angel\
a', 'Edward', 'Jonathan', 'Celine', 'Daniel', 'Lindsey', 'Ziyan', 'Elina'],                                                                                                                                                                 
    8: ['Julian', 'Sebastian', 'Jordan', 'Alan', 'Yuki', 'Chloe', 'Noah', 'Edvic', 'Jia Qi', 'Shan', 'Rodda', 'Anya', 'Edmond', 'Asher', 'Kathy', 'Sharon', 'Vncent', 'Lawrence', 'Sachal', 'Gabriel', 'Jason', 'Daniel', 'Felix', 'Jacob',\
 'Bayle', 'Fortune', 'Gio', 'Kelly', 'William', 'Jordan', 'Haley', 'Henry'],                                                                                                                                                                
    9: ['James', 'Vanna', 'Zicheng', 'Quinn', 'Anthony C', 'Joel', 'Steph', 'Xinhui', 'Richard', 'Misha', 'Maddie', 'Winston', 'Shariar', 'Nancy', 'Jerry', 'Michael', 'Stiven', 'Will',  'Olivia', 'Constantine', 'Jessica', 'Kate', 'Sham\
aul', 'Max', 'Sarah', 'Anthony L', 'Brandon', 'Nicole', 'Brian', 'Issac', 'Seiji', 'Lorenz']                                                                                                                                                
} 

def randomizer(n):
    return random.choice(CLASSES[n])

print randomizer(6)
print randomizer(8)
print randomizer(9)
