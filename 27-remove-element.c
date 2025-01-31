

void shiftInPlace(int* nums, int size, int shiftIndex) {
	int shiftStart = size - shiftIndex;
	for(int i = shiftIndex; i < size; i++) {
		nums[i] = nums[i + 1];
	}
}

int removeElement(int* nums, int numsSize, int val) {
	int k = 0;
	for(int i = 0; i < numsSize; i++) {
		if(nums[i] == val) {
			k += 1;
			shiftInPlace(nums, size, i);
		}	
	}
	return k
}
