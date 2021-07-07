def find_index(array, occ, fav):
    index_array = {}
    i = 1
    j = 1
    for a in array:
        if a == fav:
            index_array[j] = i
            j = j + 1
        i = i + 1

    for o in occ:
        if index_array.has_key(o):
            print(index_array[o])
        else:
            print(-1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array = [1,8,3,4,8,9,3,8,5,2,1]
    occ = [1,3,2,9,5]
    fav = 3
    find_index(array, occ, fav)
