import sympy as sm

def get_beta_param(mean, std):
    alpha, beta = sm.symbols('alpha, beta')
    eq1 = sm.Eq(alpha/(alpha+beta), mean) # mean
    eq2 = sm.Eq(alpha*beta / ((alpha+beta)**2 * (alpha + beta + 1)), std**2) # variance
    result = sm.solve([eq1, eq2], (alpha, beta))
    return result