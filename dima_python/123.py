def can_be_dividev_without_remainder_4 (a):
        ostatok=a%4
        if ostatok==0:
            return True
        else:
            return False
print (can_be_dividev_without_remainder_4(8))