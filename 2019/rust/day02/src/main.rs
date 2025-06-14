use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read input");

    let program: Vec<usize> = input
        .trim()
        .split(',')
        .filter_map(|s| s.trim().parse::<usize>().ok())
        .collect();

    // Part 1
    let mut part1_program = program.clone();
    part1_program[1] = 12;
    part1_program[2] = 2;
    let result = run_program(part1_program);
    println!("{:?}", result);

    // Part 2
    for noun in 0..100 {
        for verb in 0..100 {
            let mut part2_program = program.clone();
            part2_program[1] = noun;
            part2_program[2] = verb;
            if run_program(part2_program) == 19690720 {
                print!("{:?}", 100 * noun + verb);
                return;
            }
        }
    }
}

fn run_program(mut program: Vec<usize>) -> usize {
    let mut pc: usize = 0;

    while pc < program.len() {
        match program[pc] {
            1 => {
                let (a, b, c) = (program[pc + 1], program[pc + 2], program[pc + 3]);
                program[c] = program[a] + program[b];
                pc += 4;
            }
            2 => {
                let (a, b, c) = (program[pc + 1], program[pc + 2], program[pc + 3]);
                program[c] = program[a] * program[b];
                pc += 4;
            }
            99 => break,
            opcode => {
                eprintln!("Unknown opcode {} at position {}", opcode, pc);
                break;
            }
        }
    } 
    program[0]
}
