use std::io::BufRead;

fn main() {
    let mut score1 = 0;
    let mut score2 = 0;
    for line in std::io::stdin().lock().lines() {
        let line = line.unwrap();
        let trimmed = line.trim();

        let parts: Vec<&str> = trimmed.split(" ").collect();
        let opponent = parts[0];
        let player = parts[1];

        score1 += match (opponent, player) {
            ("A", "X") => 3 + 1,
            ("A", "Y") => 6 + 2,
            ("A", "Z") => 0 + 3,
            ("B", "X") => 0 + 1,
            ("B", "Y") => 3 + 2,
            ("B", "Z") => 6 + 3,
            ("C", "X") => 6 + 1,
            ("C", "Y") => 0 + 2,
            ("C", "Z") => 3 + 3,
            _ => 0,
        };
        score2 += match (opponent, player) {
            ("A", "X") => 0 + 3,
            ("A", "Y") => 3 + 1,
            ("A", "Z") => 6 + 2,
            ("B", "X") => 0 + 1,
            ("B", "Y") => 3 + 2,
            ("B", "Z") => 6 + 3,
            ("C", "X") => 0 + 2,
            ("C", "Y") => 3 + 3,
            ("C", "Z") => 6 + 1,
            _ => 0,
        };
    }
    println!("{}", score1);
    println!("{}", score2);
}
