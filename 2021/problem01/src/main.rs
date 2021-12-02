use std::fs;

fn parse_input() -> Vec<i32> {
    let contents = fs::read_to_string("input").expect("couldn't read input");
    let mut results = Vec::new();
    for line in contents.lines() {
        let num: i32 = line.parse().unwrap();
        results.push(num);
    }

    results
}

fn part_one() {
    let input = parse_input();

    let mut increasing = 0;
    let mut prev: i32 = input[0];
    for num in input[1..].iter() {
        if *num > prev {
            increasing = increasing + 1;
        }
        prev = *num;
    }

    println!("part_one: {}", increasing);
}

fn part_two() {
    let input = parse_input();

    let mut increasing = 0;
    let mut i = 1;
    let mut window1 = input[0] + input[1] + input[2];
    while i < input.len() - 2 {
        let window2 = input[i] + input[i + 1] + input[i + 2];
        if window2 > window1 {
            increasing = increasing + 1;
        }
        window1 = window2;
        i = i + 1;
    }

    println!("part_two: {}", increasing);
}

fn main() {
    part_one();
    part_two();
}
