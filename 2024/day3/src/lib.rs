use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex_lite::Regex;

pub fn parse_file(filename: &String){
	parse_file_part_1(&filename);
	parse_file_part_2(&filename);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_file_part_1(filename: &String){
	let mut sum = 0;
	let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)").unwrap();
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			let regexp = re.captures_iter(&line);
			for t in regexp{
				let a = &t[1].parse::<i32>().unwrap();
				let b = &t[2].parse::<i32>().unwrap();
				sum += a*b;
			}
		}
	}
	println!("Part 1: Sum of muls is {}", sum);
}

fn parse_file_part_2(filename: &String){
	let mut sum = 0;
	let mut do_it = true;
	let re = Regex::new(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)").unwrap();
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			let regexp = re.captures_iter(&line);
			for t in regexp{
				if t.get(0).unwrap().as_str().starts_with("mul"){
					if do_it{
						let a = &t[1].parse::<i32>().unwrap();
						let b = &t[2].parse::<i32>().unwrap();
						sum += a*b;
					}
				} else if t.get(0).unwrap().as_str().starts_with("don\'t"){
					do_it = false;
				} else {
					do_it = true;
				}
			}
		}
	}
	println!("Part 2: Sum of muls is {}", sum);
}
