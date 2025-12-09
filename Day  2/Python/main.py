part1_sum = 0
part2_sum = 0


with open("input.txt") as f:
    line = f.read().strip()


ranges = line.split(",")


for r in ranges:
    start, end = r.split("-")
    start = int(start)
    end = int(end)

    for num in range(start, end + 1):
        s = str(num)
        l = len(s)

        found_exact_two = False
        found_two_or_more = False

        for bs in range(1, l // 2 + 1):
            if l % bs != 0:
                continue
            block = s[:bs]
            repeats = l // bs
            if block * repeats == s and repeats >= 2:
                found_two_or_more = True
                if repeats == 2:
                    found_exact_two = True
                break
        if found_exact_two:
            part1_sum += num
        if found_two_or_more:
            part2_sum += num

print(f"Part 1 Answer: {part1_sum}")
print(f"Part 2 Answer: {part2_sum}")
