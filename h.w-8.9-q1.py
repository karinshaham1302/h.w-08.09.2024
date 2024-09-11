# start

slice_of_pizza: int = int(input('how many slices?'))
print(f'how much each friend received {slice_of_pizza // 4}')

if slice_of_pizza % 4 != 0:
    print(f'how many are left {slice_of_pizza % 4}')

# stop
