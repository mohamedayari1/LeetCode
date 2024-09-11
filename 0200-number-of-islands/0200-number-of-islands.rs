use std::collections::{HashSet, VecDeque};
impl Solution {
    pub fn num_islands(grid: Vec<Vec<char>>) -> i32 {
        let mut visited = HashSet::new();
        let mut num_of_islands = 0;

        let rows = grid.len();
        let cols = grid[0].len();


        fn bfs(r: usize, c: usize, grid: &Vec<Vec<char>>, visited: &mut HashSet<(usize, usize)>, rows: usize, cols: usize) {
            let mut queue = VecDeque::new();
            queue.push_back((r, c));
            visited.insert((r, c));
            let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];

            while let Some((row, col)) = queue.pop_front() {
                for &(dr, dc) in &directions {
                    let nr = row as isize + dr;
                    let nc = col as isize + dc;

                    if nr >= 0 && nr < rows as isize &&
                        nc >= 0 && nc < cols as isize &&
                        grid[nr as usize][nc as usize] == '1' &&
                        !visited.contains(&(nr as usize, nc as usize)){

                            queue.push_back((nr as usize, nc as usize));
                            visited.insert((nr as usize, nc as usize));
                    }
                }   
            }
        }
            for r in 0..rows{
                for c in 0..cols{
                    if grid[r][c] == '1' && !visited.contains(&(r, c)) { 
                        bfs(r, c, &grid, &mut visited, rows, cols);
                        num_of_islands += 1;
                    }
                }
            }



        num_of_islands
    }
}



