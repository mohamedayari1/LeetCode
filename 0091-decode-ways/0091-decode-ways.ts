function numDecodings(s: string): number {
    const cache: { [key: number]: number } = { [s.length]: 1 };

    const helper = (i: number): number => {
        if (cache.hasOwnProperty(i)){
            return cache[i];
        }

        // `==` checks for value equality with type coercion, whereas `===` checks value and type.
        if (s[i] === '0'){  
            return 0;
        }

        let curr = helper(i + 1);


        if (
            i + 1 < s.length &&
            (s[i] === '1' || (s[i] === '2' && '0123456'.includes(s[i + 1])))
        ) {
            curr += helper(i + 2);
        }

        cache[i] = curr;
        return curr;
    };

    return helper(0);
}
