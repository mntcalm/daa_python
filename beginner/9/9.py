def cleanr(sps, sps_cl):
   for j in range (0, len(sps_cl)):
       sps.remove(sps_cl[j])
   return sps

list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 4]

print(cleanr(list1, list2))
