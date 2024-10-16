function climbStairs(n: number): number {
    let cache: {[key: number]: number} = {};
    cache[n] = 1;
    cache[n-1] = 1;
    for (let i=n-2; i>=0; i--) {
        cache[i] = cache[i+1] + cache[i+2];
    }
    return cache[0];

};