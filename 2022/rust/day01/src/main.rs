use std::io::BufRead;

fn main() {
    let mut calories: Vec<usize> = Vec::new();
    let mut curr_sum: usize = 0;
    for line in std::io::stdin().lock().lines() {
        let line = line.unwrap();
        let trimmed = line.trim();

        if trimmed.is_empty() {
            calories.push(curr_sum);
            curr_sum = 0;
        } else if let Ok(value) = trimmed.parse::<usize>() {
            curr_sum += value;
        }
    }
    if curr_sum > 0 {
        calories.push(curr_sum);
    }

    calories.sort_unstable_by(|a, b| b.cmp(a));

    println!("{:?}", calories.first().unwrap());
    println!("{:?}", calories.iter().take(3).sum::<usize>())
}
