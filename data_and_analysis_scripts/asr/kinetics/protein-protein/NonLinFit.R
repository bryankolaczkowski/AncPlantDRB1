args = commandArgs(trailingOnly = TRUE)
fname = args[1]

data = read.table(fname)

rhs = function(V1,t,k){
   ((t*V1)/(k+V1))
}

fit = nls(V2 ~ rhs(V1,t,k), data, start=list(t=1.0, k=0.000001), control=nls.control(maxiter=10000))
summary(fit)

coef(summary(fit))

