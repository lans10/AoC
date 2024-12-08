use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn parse_file(filename: &str) {
    let mut sum_part_1: usize = 0;
    let mut sum_part_2: usize = 0;
    
    if let Ok(lines) = read_lines(filename) {
        for line in lines.flatten() {
            let parts: Vec<&str> = line.split(":").collect();
            let target = parts[0].trim().parse::<usize>().unwrap();
            let nums: Vec<usize> = parts[1].trim().split_whitespace().map(|num| num.parse::<usize>().unwrap()).collect();
            sum_part_1 += process_line(&target, &nums, 1);
            sum_part_2 += process_line(&target, &nums, 2);
        }    
    }
    println!("Part 1: Possible equations are {}", sum_part_1);
    println!("Part 2: Possible equations are {}", sum_part_2);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn process_line(target: &usize, nums: &Vec<usize>, part: u8) -> usize {
    if *target == nums[0] && nums.len() == 1 {
        return *target;
    }
    let mut operators = vec!['+', '*'];
    if part == 2 {
        operators.insert(0, '|');
    }
    let total_op_combos = operators.len().pow((nums.len() - 1) as u32);
    for combo_index in 0..total_op_combos {
        let mut op_combination = Vec::new();
        let mut op_index = combo_index;
        for _ in 0..(nums.len() - 1) {
            op_combination.push(operators[op_index % operators.len()]);
            op_index /= operators.len();	
        }
        let mut res: usize = nums[0];
        let mut valid = true;
        for (i, op) in op_combination.iter().enumerate() {
            match *op {
                '+' => res += nums[i + 1],
                '*' => res *= nums[i + 1],
                '|' => res = concat(res, nums[i + 1]),
                _ => valid = false,
            }
            if res > *target {
                valid = false;
                break;
            }
        }
        if valid && res == *target {
            return *target;
        }
    }
    0
}

fn concat(a: usize, b: usize) -> usize {
    format!("{}{}", a, b).parse::<usize>().unwrap()
}
