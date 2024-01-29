
setwd("~/git/school/research/bianchim_rf_ltd/argentina2")

#setwd("/Users/mitchellvaughn7576088545/Dropbox/PycharmProjects/syp2/data")
#setwd("~/git/school/research/bianchim_rf_ltd/data")
data = read.csv("datay_clean.csv")


y = data$gdp_cycle
#y = y[1:109]
N = length(y)

## declaring model

setwd("~/git/school/research/bianchim_rf_ltd/argentina2")
model <- stan_model("try_argentina.stan")

options(mc.cores=4)
fit <- sampling(model, list(N=N, y=y), iter=50000, chains=8,
                control = list(adapt_delta=0.60) )

fit <- sampling(model, list(N=N, y=y), iter=6000, chains=8)

params <- extract(fit)

params_df = data.frame(
  rho_y = params$rho_y,
  rho_sigma = params$rho_sigma,
  sigma_bar = params$sigma_bar,
  sigma_nu = params$sigma_nu
)
write.csv(params_df, "draws_argentina.csv")


pairs(fit, pars = c( "rho_y", "sigma_bar", "rho_sigma", "sigma_nu"), las = 1)

## other plotting
hist(params$rho_y)
hist(params$rho_sigma)
hist(exp(params$sigma_bar))
hist(params$sigma_nu)


