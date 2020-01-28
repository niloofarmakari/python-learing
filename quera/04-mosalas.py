def aya_okeye(mylist):
    for item in mylist:
        if item == 0:
            return False

    if sum(mylist) != 180:
        return False

    return True


li = list(map(int, input().split()))

# do_something if follan_chiz else do_something_else
print('Yes' if aya_okeye(li) else 'No')
