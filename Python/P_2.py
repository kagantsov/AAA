def fuzz_buzz(it):
    for i in it:
        if i % 3:
            print('Fuzz')
        else:
            print(i)
def custom_fuzz_buzz(**params):
    sl = params.get('sl', None)
    start = params.get('start', None)
    end = params.get('end', None)
    if sl is not None:
        if start is not None or end is not None:
            raise ValueError
        else:
            fuzz_buzz(sl)
    elif start is not None or end is not None:
        fuzz_buzz(range(start, end))
    else:
        raise ValueError