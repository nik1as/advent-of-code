use std::io::{self, BufRead};

fn main() {
    let mut total1 = 0;
    let mut total2 = 0;
    for line in io::stdin().lock().lines() {
        let mut mass = line.unwrap().trim().parse::<usize>().unwrap();
        total1 += mass / 3 - 2;

        while let Some(fuel) = (mass / 3).checked_sub(2) {
            total2 += fuel;
            mass = fuel;
        }
    }

    println!("Part 1: {:?}", total1);
    println!("Part 2: {:?}", total2);
}
