def count(tuple1, tuple2):
    global sum
    zipped = zip(tuple1, tuple2)  # 使用zip方法进行连接
    mapped = map(sum, zipped)  # 使用sum进行求和计算，map方法映射
    sum= tuple(mapped)
    return sum

tuple1 = (6, 7, 8);
tuple2 = (9, 10, 11);

sum2=count(tuple1,tuple2)
print(sum2)


def nan(tuple1,tuple2):
    list=()
    for i in range(3):
        b=tuple1[i]+tuple2[i]
        list+=(b,)
    print(list)
    return list

z=nan(tuple1,tuple2)

b=nan(z,tuple2)

