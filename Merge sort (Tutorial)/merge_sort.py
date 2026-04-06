def mergeSort(nums):
    # Once our array is sorted
    if len(nums) <= 1:
        return nums

    mid = (len(nums)) // 2
    left_half = nums[:mid]
    right_half = nums[mid:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    # We merge after all sides return something
    return merge(sorted_left, sorted_right)

def merge(sorted_left, sorted_right):
        sorted_list = []
        l, r = 0, 0
        
        while l < len(sorted_left) and r < len(sorted_right):
            if sorted_left[l] < sorted_right[r]:
                sorted_list.append(sorted_left[l]) 
                l += 1

            else:
                sorted_list.append(sorted_right[r])
                r += 1

        sorted_list.extend(sorted_left[l:])
        sorted_list.extend(sorted_right[r:])

        return sorted_list


print(mergeSort([1, 3, 2, 10, -3, 8]))
    