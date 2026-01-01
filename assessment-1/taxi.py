d = int(input())
oc, of, od = map(int,input().split())
cs, cb, cm, cd = map(int,input().split())

if d <= of:
    online_cost = oc
else:
    online_cost = oc+(d-of)*od
time_taken = d//cs

#  2+⌊13/4⌋×1+13×2=31
classic_cost = cb+(time_taken*cm)+(d*cd)

if online_cost <= classic_cost:
    print("Online Taxi")
else:
    print("Classic Taxi")