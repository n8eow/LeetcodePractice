        def quicksort(Arr):

            if Arr == [] or len(Arr) == 1:
                return Arr
            Pivot = 0
            for i in range(1, len(Arr)):
                if Arr[i] < Arr[Pivot]:
                    Arr = [Arr[i]] + Arr[:i] + Arr[i+1:]
                    Pivot += 1
            return quicksort(Arr[:Pivot]) + [Arr[Pivot]] + quicksort(Arr[Pivot + 1:])

        arr = quicksort(arr)
