def time_delivery(d):
    res = []
    for i in d:
        if d[i].count(1) > 3:
            res.append(i)
    return sorted(res)

print(time_delivery({'Грузовичок':[1,1,1,1], "Машинка":[0,1,1,1], "Доставочка":[1,0,0], "Производства":[1,1,1,1,0], "Андромеда":[1,1,0,1,0,1]}))