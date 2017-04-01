[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>>```python  
>> import nsfg  
>>import numpy as np  
>>preg = nsfg.ReadFemPreg()  
>>live = preg[preg.outcome == 1]  
>>firsts = live[live.birthord == 1]  
>>others = live[live.birthord != 1]  
>>def CohenEffectSize(group1, group2):  
>>    """Computes Cohen's effect size for two groups.  
>>    
>>    group1: Series or DataFrame  
>>    group2: Series or DataFrame  
>>    
>>    returns: float if the arguments are Series;  
>>             Series if the arguments are DataFrames  
>>    """
>>    diff = group1.mean() - group2.mean()  
>>
>>    var1 = group1.var()  
>>    var2 = group2.var()  
>>    n1, n2 = len(group1), len(group2)  
>>
>>    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)  
>>    d = diff / np.sqrt(pooled_var)  
>>    return d  
>>print("First baby - mean weight:", firsts.totalwgt_lb.mean())  
>>#First baby - mean weight: 7.201094430437772
>>print("Other baby - mean weight:", others.totalwgt_lb.mean())  
>>#Other baby - mean weight: 7.325855614973262  
>>print("Cohen Difference - mean weight:", CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb))  
>>#Cohen Difference - mean weight: -0.0886729270726  
>>print("First baby - mean pregnancy length:", firsts.prglngth.mean())  
>>#First baby - mean pregnancy length: 38.60095173351461  
>>print("Other baby - mean pregnancy length:", others.prglngth.mean())  
>>#Other baby - mean pregnancy length: 38.52291446673706  
>>print("Cohen Difference - mean pregnancy length:", CohenEffectSize(firsts.prglngth, others.prglngth))  
>>#Cohen Difference - mean pregnancy length: 0.0288790446544  
