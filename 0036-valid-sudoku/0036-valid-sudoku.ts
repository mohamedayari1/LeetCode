function isValidSudoku(board: string[][]): boolean {
    const validator = (value: string, seen: Set<string>): boolean => {
        if (value == "." ) {
            return true;
        }
        if (seen.has(value)) {
            return false;
        }
        seen.add(value);
        return true;
    };

    const boxMap: { [key:string]: Set<string> } = {};
    for (let i=0;i<3;i++){
        for (let j=0;j<3;j++) {
            boxMap[`${i},${j}`] = new Set<string>();
        }
    }

    for (let i=0;i < 9; i++) {
        const rowSet: Set<string> = new Set<string>();
        const colSet: Set<string> = new Set<string>();
        for (let j=0;j<9;j++) {

            if (!validator(board[i][j], colSet)){
                return false;
            }
            if (!validator(board[j][i], rowSet)){
                return false;
            }
            const currBoxKey = `${Math.floor(i / 3)},${Math.floor(j / 3)}`;
            if (!validator(board[i][j], boxMap[currBoxKey])){
                return false;
            }
        }
    }
    return true;




};