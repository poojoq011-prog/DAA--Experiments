import math

items = [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
capacity = 1.0


def first_fit(items, capacity):
    bins = []

    for item in items:
        placed = False
        for b in bins:
            if sum(b) + item <= capacity:
                b.append(item)
                placed = True
                break
        if not placed:
            bins.append([item])

    return bins


def first_fit_decreasing(items, capacity):
    return first_fit(sorted(items, reverse=True), capacity)


def best_fit_decreasing(items, capacity):
    items = sorted(items, reverse=True)
    bins = []

    for item in items:
        best_bin = -1
        min_space = capacity + 1

        for i in range(len(bins)):
            space = capacity - sum(bins[i])
            if item <= space and (space - item) < min_space:
                min_space = space - item
                best_bin = i

        if best_bin == -1:
            bins.append([item])
        else:
            bins[best_bin].append(item)

    return bins


ff = first_fit(items, capacity)
ffd = first_fit_decreasing(items, capacity)
bfd = best_fit_decreasing(items, capacity)

lower_bound = math.ceil(sum(items) / capacity)

print("Items:", items)
print("Bin Capacity:", capacity)

print("\nFirst Fit (FF)")
for i, b in enumerate(ff, 1):
    print(f"Bin {i}: {b} -> {sum(b):.1f}")
print("Bins Used:", len(ff))

print("\nFirst Fit Decreasing (FFD)")
for i, b in enumerate(ffd, 1):
    print(f"Bin {i}: {b} -> {sum(b):.1f}")
print("Bins Used:", len(ffd))

print("\nBest Fit Decreasing (BFD)")
for i, b in enumerate(bfd, 1):
    print(f"Bin {i}: {b} -> {sum(b):.1f}")
print("Bins Used:", len(bfd))

print("\nTheoretical Lower Bound:", lower_bound)

OUTPUT:
Items: [0.5, 0.7, 0.3, 0.9, 0.2, 0.6, 0.8, 0.4, 0.1, 0.5]
Bin Capacity: 1.0

First Fit (FF)
Bin 1: [0.5, 0.3, 0.2] -> 1.0
Bin 2: [0.7, 0.1] -> 0.8
Bin 3: [0.9] -> 0.9
Bin 4: [0.6, 0.4] -> 1.0
Bin 5: [0.8] -> 0.8
Bin 6: [0.5] -> 0.5
Bins Used: 6

First Fit Decreasing (FFD)
Bin 1: [0.9, 0.1] -> 1.0
Bin 2: [0.8, 0.2] -> 1.0
Bin 3: [0.7, 0.3] -> 1.0
Bin 4: [0.6, 0.4] -> 1.0
Bin 5: [0.5, 0.5] -> 1.0
Bins Used: 5

Best Fit Decreasing (BFD)
Bin 1: [0.9, 0.1] -> 1.0
Bin 2: [0.8, 0.2] -> 1.0
Bin 3: [0.7, 0.3] -> 1.0
Bin 4: [0.6, 0.4] -> 1.0
Bin 5: [0.5, 0.5] -> 1.0
Bins Used: 5

Theoretical Lower Bound: 5
