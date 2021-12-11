import statistics
#Data Analysis - Basic Statistical Descriptions assignment
#Below present the tuple of the ages in increasing order.
#Below is the list of age values 
ages = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40,
45, 46, 52, 70]
#variable dealing with quartiles
q = statistics.quantiles(ages, n=4)                      
#print for the display of the data
print(ages)
print("")
#Print statement as an introduction
print("Hello these are the statistical descriptions of the tuple above.")
print("")
#statements for each descriptions
print("The mean:",format(statistics.mean(ages), '.2f'))
print("the median:", statistics.median(ages))
print("The mod:", statistics.mode(ages) ," and the data is a bimodal")
print("The midgrange:", (min(ages) + max(ages)) / 2)
print("THe variance:", format(statistics.variance(ages),".2f"), "and the standard deviation is:", format(statistics.stdev(ages),".2f"))
print("The first and third quartiles:", q)
print("The five-number summary:", min(ages), q , max(ages))

      
