nbr_freqs = int(input(''))
freqs_input = input('')

freqs_text = freqs_input.split()

freqs = []
for item in freqs_text:
    freqs.append(int(item))

smallest_multiple = None
for item in freqs:
    if item % 3 == 0:
        if not smallest_multiple:
            smallest_multiple = item
        else:
            if item < smallest_multiple:
                smallest_multiple = item

print(smallest_multiple)
