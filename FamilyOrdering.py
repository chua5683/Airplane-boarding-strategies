
# coding: utf-8

# In[ ]:


import random
from Ordering import ordering
import numpy as np

random.seed(2018)

def familyEffects(nrows, ncols, groups, methods, percentFamily = [0.2, 0.4]):
    
    origOrder = ordering(nrows, ncols, groups, methods)

    # (1) determine the effect of families of size 3
    sampling = [[i, j] for i in range(nrows) for j in [0, 5]]
    famSize_3 = random.sample(sampling, int(2*nrows*percentFamily[0]))
#     print('Families of size 3:', famSize_3)
    
    leftRows = set([i for i in range(nrows)])
    rightRows = set([i for i in range(nrows)])
    
    for family in famSize_3:
        if family[1] == 0:
            member1 = [family[0], 1]
            member2 = [family[0], 2]
            leftRows = leftRows - set([family[0]])

        elif family[1] == 5:
            member1 = [family[0], 4]
            member2 = [family[0], 3]
            rightRows = rightRows - set([family[0]])

        origOrder.remove(member1)
        origOrder.remove(member2)
        # determine the position of the first person in each family group
        ind = origOrder.index(family)
        origOrder.insert(ind+1, member1)
        origOrder.insert(ind+2, member2)

    # (2) determine the effect of families of size 2
    famSize_2 = []
    allRows = [i for i in range(nrows)]
#     print(leftRows)
#     print(rightRows)
    leftRowInd = random.sample(leftRows, int(nrows*percentFamily[1]))
    rightRowInd = random.sample(rightRows, int(nrows*percentFamily[1]))
    for x in leftRowInd:
        y = random.sample([0, 1], 1)[0]
        famSize_2.append([x, y])
    for x in rightRowInd:
        y = random.sample([4, 5], 1)[0]
        famSize_2.append([x, y])
    
#     print('Families of size 2:', famSize_2)
    for family in famSize_2:
        if family[1] == 0 or family[1] == 1:
            member = [family[0], family[1] + 1]

        elif family[1] == 4 or family[1] == 5:
            member = [family[0], family[1] - 1]

        origOrder.remove(member)
        # determine the position of the first person in each family group
        ind = origOrder.index(family)
        origOrder.insert(ind+1, member)
        
        
    if len(origOrder) != nrows*ncols:
        print('The total number of passengers is not correct!')
        
    return origOrder


# In[ ]:


def familyOrdering(nrows, ncols, groups, methods, percentFamily = [0.2, 0.4]):
    ''' 
    inputs:
        nrows, ncols:  integer, number of rows and columns of the airplane
        groups: integer, number of groups
        methods: string, different strategies
                 'BTF': Back-to-Front with ordering
                 'BLOCK': Back-to-Front with Blocks
                 'WILMA': Window-Middle-Asile
                 'RASS': Random-with-AssignSeats
                 'RFOALL': Random-Free-for-All
                 'STFOPT': Steffan-optimal
                 'STFMOD': Steffan-Modified-Optimal
                 'Amigos': Amigos-Steffan method
                 'REVPYR': Reverse Pyramid
                 
        percentFamily: percentage of differcent family sizes, 
                       for example [0.2, 0.4] means:
                           0.2 -- 20% of rows will have a family of size 3
                           0.4 -- 40% of rows will have a family of size 2

    return: a list of the ordering
    '''
    
    if methods == "BTF":
        familyOrdering = familyEffects(nrows, ncols, groups, 'BTF', percentFamily) 

    elif methods == 'BLOCK':
        familyOrdering = familyEffects(nrows, ncols, groups, 'BLOCK', percentFamily)

    elif methods == 'WILMA':
        # 3 groups: windows, midlle, asile
        groups = 3
        familyOrdering = familyEffects(nrows, ncols, groups, 'WILMA', percentFamily)

    elif methods == 'RASS':
        familyOrdering = familyEffects(nrows, ncols, groups, 'RASS', percentFamily)

    elif methods == 'STFOPT':
        familyOrdering = familyEffects(nrows, ncols, groups, 'STFOPT', percentFamily)

    elif methods == 'STFMOD':
        groups = 4
        familyOrdering = familyEffects(nrows, ncols, groups, 'STFMOD', percentFamily)
    
    elif methods == 'REVPYR':
        # groups = 4 or 5
        familyOrdering = familyEffects(nrows, ncols, groups, 'REVPYR', percentFamily)
    
    elif methods == 'RFOALL':
        familyOrdering = familyEffects(nrows, ncols, groups, 'RFOALL', percentFamily)
    
    elif methods == 'Amigos':
        print('Waiting for the surprise!')

    return familyOrdering


# In[ ]:


# familyOrdering(12, 6, 4, 'RFOALL')

