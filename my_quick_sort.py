concat_list = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
print("input list  : ", concat_list)

# Begin from all items in the input list as one group to divide
tod_lists = [concat_list]

# When the input list is divided into each item as a group (the number of groups
# in output list is sequal to the number of items in input list), process stops.
while len(tod_lists) < len(concat_list):
    pivot_locs = []
    sort_lists = []

    pivot_start = 0
    for tod_list in tod_lists:
        # Assign the item in the middle location of each group to pivot value.
        pivot_loc = pivot_start + int((len(tod_list)-1)/2)
        pivot_val = concat_list[pivot_loc]

        left_list = []
        right_list = []
        # Divide each item in the sublist so that the item in left side item is
        # less than pivot value and the item in right side is greater value.
        for loc in range(pivot_start, pivot_start + len(tod_list)):
            # Skip when loop to pivot position
            if loc == pivot_loc:
                continue

            val = concat_list[loc]
            if val < pivot_val:
                left_list.append(val)
            else:
                right_list.append(val)

        sort_lists += [left_list] + [[pivot_val]] + [right_list]

        # Jump to next group starting position
        pivot_start += len(tod_list)

    # Save current sorting group list
    tod_lists = sort_lists

    # Remove any empty group in the sorting list
    while tod_lists.count([]):
        tod_lists.remove([])

    print("processing  : ", tod_lists)

    concat_list = []
    for tod_list in tod_lists:
        concat_list += tod_list

print("sorted list : ", concat_list)
