function getFrequency(nums: number[]): Map<number, number> {
    const freqMap = new Map<number, number>();

    for (let num of nums) {
        freqMap.set(num, 1 + (freqMap.get(num) || 0));
    }
    return freqMap;
}

function topKFrequent(nums: number[], k: number): number[] {
    if (nums.length  === 0|| k<=0) return [];

    const freqMap: Map<number, number> = getFrequency(nums);

    const freqBuckets: number[][] = Array.from({length: nums.length+1}, () => [])

    for (let [num, freq] of freqMap.entries()) {
        freqBuckets[freq].push(num);
    }

    const result: number[] = [];
    
    for (let i=nums.length; i>=0 && result.length < k; i--) {
        while (freqBuckets[i].length > 0) {
            result.push(freqBuckets[i].pop());
            if (result.length === k) break;
        }
    }
    return result;
};