def logistic_function (FicoScore, LoanAmount, IR_TF, ind_vars):
    interest_rate = b + a1(FICOScore) + a2(LoanAmount)
    logit = sm.Logit(df['IR_TF'], df[ind_vars])
    result = logit.fit()
    coeff = result.params
    print coeff
