count = 0
for c200 in range(2):
    for c100 in range(3):
        if 200 < c200*200 + c100*100:
            break
        for c50 in range(5):
            if 200 < c200*200 + c100*100 + c50*50:
                break
            for c20 in range(11):
                if 200 < c200*200 + c100*100 + c50*50 + c20*20:
                    break
                for c10 in range(21):
                    if 200 < c200*200 + c100*100 + c50*50 + c20*20 + c10*10:
                        break
                    for c5 in range(41):
                        if 200 < c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5:
                            break
                        for c2 in range(101):
                            if 200 < c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2:
                                break
                            for c1 in range(201):
                                if 200 < c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 + c1:
                                    break
                                if c200*200 + c100*100 + c50*50 + c20*20 + c10*10 + c5*5 + c2*2 + c1 == 200:
                                    count += 1
print(count)