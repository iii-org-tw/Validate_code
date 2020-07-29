library(devtools)
install_github("iii-org-tw/Hmisc")
require(Hmisc)
d = file("../data/HIGGS.csv", "r")
for (i in c(1:100000)){
  line = strsplit(readLines(d, n=1,), ',')
  vector = c()
  for (v in line){
    vector = append(vector, as.double(v),)
  }
  if (quantile(vector, probs=0.5) != wtd.quantile(vector, probs=0.5,weights=c(rep(1,29)) )){
    print("error")
    print (quantile(vector,))
    print ( wtd.quantile(vector, weights=c(rep(1,29)) ))
  }
}

print ("pass")