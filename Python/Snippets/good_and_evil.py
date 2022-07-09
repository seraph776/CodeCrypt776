def goodVsEvil(good, evil):
    good = sum([int(x) * y for x, y in zip(list(good.split(' ')), [1, 2, 3, 3, 4, 10])])
    evil = sum([int(x) * y for x, y in zip(list(evil.split(' ')), [1, 2, 2, 2, 3, 5, 10])])
    result = ['Battle Result: No victor on this battle field', 'Battle Result: Good triumphs over Evil', 'Battle Result: Evil eradicates all trace of Good']
    return result[0] if good == evil else result[1] if good > evil else result[2]

print(good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1')) 
