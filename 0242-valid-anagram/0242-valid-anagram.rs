use std::collections::HashMap;
impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len(){
            return false;
        }
        let mut count = HashMap::new();

        for (s_char, t_char) in s.chars().zip(t.chars()){
            *count.entry(s_char).or_insert(0) += 1;
            *count.entry(t_char).or_insert(0) -= 1;
        } 

        return count.values().all(|&v| v == 0);
    }
}