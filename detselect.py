#deterministic select


#https://www.ics.uci.edu/~eppstein/161/960130.html
#https://www.reddit.com/r/learnprogramming/comments/3ld88o/pythonimplementing_median_of_medians_algorithm/
#https://www.youtube.com/results?search_query=determinstic+sort&page=&utm_source=opensearch
import time
import sys
coutn = 0 #number of comparisons



def deterministic_select(L, k):
    if(L < 10):
        L.sort() #uses quicksort or bubblesort iirc
        return L[k]


    subs = [L[i:i+5] for i in xrange(0, len(L), 5)] # partitions in n/5 groups of length at most 5
    meds = [sorted(sub)[len(sub)/2] for sub in subs] #median of medians for each sublist
    M = sorted(meds)[len(meds)/2]
    # for y in range(0,len(subs)):
    #     meds[y] = deterministic_select(subs[y], 3)
    #M = deterministic_select(meds, (len(L)/10)) #pick the median of the medians

    left = [x for x in L if x < M]
    right = [x for x in L if x > M]
    center = [x for x in L if x == M]
    comp += len(L)
    comp += 3 #for the if statements

    if(k <= len(left)):
            comp -= 2 #didn't compare the other if and else
            return deterministic_select(left,k)
    if(k > len(left)+len(center)):
            comp -= 1 #didnt compare the last else
            return deterministic_select(right, k-len(left)-len(center))
    else:
            return M

def main():
  start = time.clock()
  k = int(sys.argv[2])
  nums = []
  with open(sys.argv[1]) as f:
    for line in f:
      nums.append(int(line))
  x = deterministic_select(nums, k)
  end = time.clock()

  # print(x)
  print("kth element:\t %d" % (x))
  print("Comparisons:\t %d" % (comp))
  print("Time:\t %f" % (end-start))



if __name__ == "__main__":
    main()
