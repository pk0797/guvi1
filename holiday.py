def f(x):
    return {
        "monday"   :  "no",
        "tuesday"  :  "no",
        "wednesday":  "no",
        "thursday" :  "no",
        "friday"   :  "no",
        "saturday" :  "yes",
        "sunday"   :  "yes"
        
    }.get(x,"not a valid day") 
p=raw_input()
k=f(p.lower())
print(k)
