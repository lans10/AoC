use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;

pub struct Config{
    pub v1: Vec<i32>, pub v2: Vec<i32>, pub v2_sum: HashMap<i32,i32>
}

impl Config{
    pub fn new(filename: &String) -> Config{
        let mut v1 = Vec::new();
        let mut v2 = Vec::new();
		let mut v2_sum = HashMap::new();
        if let Ok(lines) = read_lines(filename) {
            for line in lines.flatten() {
                let parts: Vec<&str> = line.split_whitespace().collect();
                v1.push(parts[0].parse::<i32>().unwrap());
                v2.push(parts[1].parse::<i32>().unwrap());
            }
        }
        v1.sort();
        v2.sort();
		for &num in &v2 {
			*v2_sum.entry(num).or_insert(0) += 1;
		}
        Config{v1,v2,v2_sum}
    }
}

pub fn parse_part1(v1:&Vec<i32>, v2:&Vec<i32>){
    let mut sum = 0;
    for n in 0..v1.len(){
        sum += i32::abs(v1[n]-v2[n]);
    }
    println!("Part 1: Sum is {}", sum);
}

pub fn parse_part2(v1:&Vec<i32>, v2_sum:&HashMap<i32,i32>){
    let mut sum = 0;
	for &n in v1 {
		if let Some(&count) = v2_sum.get(&n) {
			sum += n * count;
		}
    }
    println!("Part 2: Sum is {}", sum);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
