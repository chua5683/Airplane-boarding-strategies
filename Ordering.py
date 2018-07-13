
# coding: utf-8

# ## Generrating the ordering for diferrent strategies

import random
import numpy as np
random.seed(2018)

def ordering(nrows, ncols, groups, methods, percentFamily = 0.3):
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

    return: a list of the ordering
    '''
    ordering = []

    if methods == "BTF":
        for i in range(nrows-1, -1, -1):
            for j in range(ncols//2):
                ordering.append([i, ncols - j - 1])
                ordering.append([i, j])

    elif methods == 'BLOCK':
        blocRows = nrows // groups
        for i in range(0, groups, 2):
            lower = nrows - blocRows*(i + 1)
            upper = nrows - blocRows*i
            blocks = [[j, k] for j in range(lower, upper) for k in range(ncols)]
            random.shuffle(blocks)
            ordering = ordering + blocks
        for i in range(1, groups, 2):
            lower = nrows - blocRows*(i + 1)
            upper = nrows - blocRows*i
            blocks = [[j, k] for j in range(lower, upper) for k in range(ncols)]
            random.shuffle(blocks)
            ordering = ordering + blocks

    elif methods == 'WILMA':
        # 3 groups: windows, midlle, asile
        for j in range(groups):
            blocks = [[k, j] for k in range(nrows)] + [[k, ncols - j - 1] for k in range(nrows)]
            random.shuffle(blocks) 
            ordering = ordering + blocks

    elif methods == 'RASS':
        ordering = [[i, j] for i in range(nrows) for j in range(ncols)]
        random.shuffle(ordering)


    elif methods == 'STFOPT':
        for i in range(ncols//2):
            even1 = [[j, ncols - i - 1] for j in range(nrows-1, -1, -2)]
            even2 = [[j, i] for j in range(nrows-1, -1, -2)]

            odd1 = [[j, ncols - i - 1] for j in range(nrows-2, -1, -2)]
            odd2 = [[j, i] for j in range(nrows-2, -1, -2)]
            ordering = ordering + even1 + even2 + odd1 + odd2

    elif methods == 'STFMOD':
        for i in range(groups//2):
            # four groups: right even -> left even -> right odd -> left odd
            blocks1 = [[j, k] for j in range(nrows-1-i, -1, -groups//2) for k in range(ncols-1, (ncols-1)//2, -1)]
            random.shuffle(blocks1)
            blocks2 = [[j, k] for j in range(nrows-1-i, -1, -groups//2) for k in range((ncols-1)//2, -1, -1)]
            random.shuffle(blocks2)
            ordering = ordering + blocks1 + blocks2
            
    elif methods == 'RFOALL':
        total = ncols*nrows
        col_prob = [0.175, 0.025, 0.3, 0.3,0.025, 0.175]
        
        while len(ordering) < total:
            j = np.random.choice(ncols, 1, p=col_prob, replace=True)
            if j[0] == 0 or j[0] == 5:
                # ind = np.random.choice(nrows,1)
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            elif j[0] ==1 or j[0] ==4:
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            elif j[0] ==2 or j[0] ==3:
                ind = int(np.random.gamma(1,nrows/6))
                person = [ind, j[0]]
            
            if person in ordering or person[0] >= nrows:
                continue
            else:
                ordering.append(person)
    
    elif methods == 'REVPYR':
        ncols = 6                    # only works for 6 columns and 4 or 5 groups
        
        if groups == 4:
            cut1 = nrows // 4        # group 1 starts here
            
            group1 = [[j,k] for j in range(cut1,nrows) for k in [0,5]]
            random.shuffle(group1)
#             print(group1)
            
            b = 2*cut1               # group 2 middle ends here
            group2A = [[j,k] for j in range(0,cut1) for k in [0,5]]
            group2B = [[j,k] for j in range(b,nrows) for k in [1,4]]
            group2 = group2A + group2B
            random.shuffle(group2)

            c = 3*cut1               # group 3 aisle ends here (also size group 4)
            group3A = [[j,k] for j in range(0,b) for k in [1,4]]
            group3B = [[j,k] for j in range(c,nrows) for k in [2,3]]
            group3 = group3A + group3B
            random.shuffle(group3)

            group4 = [[j,k] for j in range(0,c) for k in [2,3]]
            random.shuffle(group4)

            ordering = ordering + group1 + group2 + group3 + group4
            
        elif groups == 5:
            cut1 = 2*nrows // 5 

            group1 = [[j,k] for j in range(cut1,nrows) for k in [0,5]]
            random.shuffle(group1)
            print(group1)
            
            cut2 = 2*cut1 // 5                      
            b = 2*cut1 - cut2                   # group 2 middle comes up to here 
            group2A = [[j,k] for j in range(cut2,cut1) for k in [0,5]]
            group2B = [[j,k] for j in range(b,nrows) for k in [1,4]]
            group2 = group2A + group2B
            random.shuffle(group2)
            
            c = 3*cut1 - nrows                  # group 3 middle comes up to here
            group3A = [[j,k] for j in range(0,cut2) for k in [0,5]]
            group3B = [[j,k] for j in range(c,b) for k in [1,4]]
            group3 = group3A + group3B
            random.shuffle(group3)

            d = 4*cut1 - nrows                  # size group 5
            group4A = [[j,k] for j in range(0,c) for k in [1,4]]
            group4B = [[j,k] for j in range(d,nrows) for k in [2,3]]
            group4 = group4A + group4B
            random.shuffle(group4)
                         
            group5 = [[j,k] for j in range(0,d) for k in [2,3]]
            random.shuffle(group5)
            ordering = ordering + group1 + group2 + group3 + group4 + group5
            
        else:
            print('Number of groups should be 4 or 5.')
            
    elif methods == 'Amigos':
        print('Waiting for the surprise!')
                
                
#     print('Length of the ordering:', len(ordering))
    
    if len(ordering) != nrows*ncols:
        print(len(ordering))
        print('The total number of passengers is not correct!')
    
    return ordering


