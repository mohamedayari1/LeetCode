function getAnagramsKey(str: string): string {
    return str.split('').sort().join('');
}
function groupAnagrams(strs: string[]): string[][] {
    const anagramsGroups = new Map<string, string[]>();

    for (let str of strs) {
        const key = getAnagramsKey(str);
        if (anagramsGroups.has(key)) {
            anagramsGroups.get(key).push(str);
        } else {
            anagramsGroups.set(key, [str]);
        }
    }
    return Array.from(anagramsGroups.values());
};