code = """
data {
 int N; 
 real y[N];
  
}
parameters {
  real<lower=0, upper=1> rho_y;
  real<lower=0, upper=1> rho_sigma;
  real sigma_bar;
  real<lower=0> sigma_nu;
  
  real sigma[N];
}
model {
  rho_y ~ beta(.5, .2);
  rho_sigma ~ beta(.5, .2);
  sigma_bar ~ normal(-4, 1);
  sigma_nu ~ gamma(1, 2);
  sigma[1] ~ normal( sigma_bar, sigma_nu / sqrt( 1 - (rho_sigma * rho_sigma)));
  for (t in 2:N) 
    y[t] ~ normal(rho_y * y[t-1] , exp(sigma[t]));
  for (t in 2:N) 
    sigma[t] ~ normal((1 - rho_sigma) * sigma_bar + rho_sigma * sigma[t-1] , sigma_nu);
}
"""