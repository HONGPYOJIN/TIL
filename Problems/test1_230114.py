def RSP ():
    while True:
        # print('plz input the data (Rock : 1, Scissors : 2, Paper : 3')
        # print(' : ')
        dataA, dataB = map(int , input().split())
        # modA = dataA%3
        # modB = dataB%3
        if dataA*dataB==0:
            break
        # elif dataA > 3 or dataA < 0 or dataB > 3 or dataB < 0:
        #     print('input is wrong')
        else :
            if (dataA)%3 == (dataB+1)%3 :
                print('B')
            elif (dataA)%3 == (dataB+2)%3:
                print('A')
            else :
                print('Draw...')
        
    
RSP()