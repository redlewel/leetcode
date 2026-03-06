#include <stdio.h>

void shiftInPlace(int* nums, int size, int shiftIndex) {
	for(int i = shiftIndex; i < size - 1; i++) {
        //printWholeArr(nums, size); uncomment for leetcode entry
		nums[i] = nums[i + 1];
	}
}

int removeElement(int* nums, int numsSize, int val) {
    // NOTE: the adjusted numsize is literally k
	int k = 0;
	for(int i = numsSize - 1; i > -1; i--) {
		if(nums[i] == val) {
            if (i == numsSize) {
                 numsSize -= 1;
            }
            else {
                k += 1;
                shiftInPlace(nums, numsSize, i);
                numsSize -= 1;
            }
		}	
	}
	return numsSize;
}

// Everything down here is for manual debugging with gcc

int main() {
    int nums[] = {3,2,2,3};
    int size = removeElement(nums, 4, 3);
    for(int i = 0; i < size; i++) {
        printf("%d ", nums[i]);
    }
    printf("\n");
    return 0;
}

void printWholeArr(int* nums, int size) {
    printf("Current Array: ");
    for(int i = 0; i < size; i++) {
        printf("%d", nums[i]);
    }
    printf("\n");
}


