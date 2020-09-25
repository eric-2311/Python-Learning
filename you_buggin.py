def num_teams(rating):
    import pdb
    # pdb.set_trace()
    teams = 0
    l = []
    x = 0

    while x <= len(rating)-2:
        y = x + 1
        while y <= len(rating)-1:
            z = y + 1
            while z < len(rating):
                if rating[x] < rating[y] and rating[y] < rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])
                elif rating[x] > rating[y] and rating[y] > rating[z]:
                    teams += 1
                    l.append([rating[x], rating[y], rating[z]])

                z += 1
            y += 1
        x += 1

    
    print(l)
    print(teams)



rating = [2,5,3,4,1] # 3 because [2, 3, 4], [5, 4, 1], [4, 3, 2]
num_teams(rating)