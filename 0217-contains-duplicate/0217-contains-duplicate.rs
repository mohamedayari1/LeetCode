use std::collections::HashSet; // Import the HashSet from the standard library
impl Solution {
    // Define the function that checks for duplicates in the vector `nums`
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new(); // Create a new empty HashSet to keep track of seen numbers
        
        // Iterate over each number in the `nums` vector
        for &num in &nums {
            // Attempt to insert the number into the HashSet
            // The `insert` method returns `false` if the number was already in the set
            if !seen.insert(num) {
                // If `insert` returns `false`, it means the number `num` is a duplicate
                return true; // Return `true` since a duplicate was found
            }
        }
        
        // If the loop completes without finding any duplicates, return `false`
        return false;
    }
}
