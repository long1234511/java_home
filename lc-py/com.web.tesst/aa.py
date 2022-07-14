if __name__ == '__main__':
  aa = [15, 13, 22, 14, 61, 12, 32, 11]
  for i in range(len(aa)):
    min_a = i
    for j in range(i+1,len(aa)):
        if aa[i] > aa[j]:
            index_a = aa[i]
            aa[i] = aa[j]
            aa[j] = index_a
  print(aa)