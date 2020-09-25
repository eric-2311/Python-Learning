def num_teams(rating):
    import pdb
    pdb.set_trace()
    teams = 0
    
    x = 0

    while x < len(rating)-2:
        y = 0

        while y < len(rating)-1:
            y += 1
            z = y + 1
            while z < len(rating):
                if rating[x] < rating[y] and rating[y] < rating[z]:
                    teams += 1

                z += 1

    print(teams)



rating = [2,5,3,4,1] # 3 because [2, 3, 4], [5, 4, 1], [4, 3, 2]
num_teams(rating)