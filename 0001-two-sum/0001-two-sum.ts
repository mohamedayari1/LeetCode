function twoSum(nums: number[], target: number): number[] {
  const tracker: { [key: number]: number } = {}

  for (let i=0; i < nums.length; i++) {
    const num = nums[i]
    
    if (tracker.hasOwnProperty(num)) {
        return [i, tracker[num]]
    }
    tracker[target - num] = i
  }  
  return null;
};