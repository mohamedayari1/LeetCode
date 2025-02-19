function twoSum(nums: number[], target: number): number[] {
    
    const map = new Map<number, number>();

    for (let i=0; i<nums.length; i++) {
        if (map.has(nums[i])) {
            return [i, map.get(nums[i])];
        }
        map.set(target - nums[i], i);
    }


};