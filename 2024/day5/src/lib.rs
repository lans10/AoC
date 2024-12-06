use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn parse_file(filename: &String){
	parse_file_helper(&filename);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_file_helper(filename: &String){
	let mut order_rule = true;
	let mut rules: Vec<(u8,u8)> = vec![];
	let mut mid_sum_1: usize = 0;
	let mut mid_sum_2: usize = 0;
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			if line.trim()==""{
				order_rule = false;
				continue;
			}
			if order_rule{
				let parts: Vec<&str> = line.split("|").collect();
				rules.push((parts[0].parse::<u8>().unwrap(),parts[1].parse::<u8>().unwrap()));				
			} else {
				let curr = process_update(&line, &rules);
				if curr == 0{
					mid_sum_2 += process_incorrect(&line, &rules);
				}else{
					mid_sum_1 += curr;
				}
			}
		}
	}
	println!("Part 1: Mid sums are {}",mid_sum_1);
	println!("Part 2: \"Incorrect\" mid sums are {}",mid_sum_2);
}

fn process_update(line: &String, rules: &Vec<(u8,u8)>) -> usize{
	let mut curr_rules: Vec<(u8,u8)> = vec![];
	let mut update: Vec<u8> = vec![];
	let parts: Vec<&str> = line.split(",").collect();
	for part in parts{
		update.push(part.parse::<u8>().unwrap());
	}
	for (a, b) in rules{
		if update.contains(a) && update.contains(b){
			curr_rules.push((*a,*b));
		}
	}
	for (a, b) in &curr_rules{
		if update.contains(&a) && update.contains(&b){
			if update.iter().position(|&r| r == *a).unwrap() > update.iter().position(|&r| r == *b).unwrap(){
				return 0;
			}
		}
	}
	update[update.len() / 2] as usize
}

fn process_incorrect(line: &String, rules: &Vec<(u8, u8)>) -> usize {
    let mut curr_rules: Vec<(u8, u8)> = vec![];
    let mut ordered: Vec<u8> = vec![];
    let mut update: Vec<u8> = vec![];
    for part in line.split(",") {
        update.push(part.parse::<u8>().unwrap());
    }
    for (a, b) in rules {
        if update.contains(a) && update.contains(b) {
            curr_rules.push((*a, *b));
        }
    }
    while let Some(new_element) = update.pop() {
        ordered.push(new_element);
        let mut idx = ordered.len() - 1;
        while idx > 0 {
            let mut valid = true;
            for (a, b) in &curr_rules {
                if ordered[idx] == *a && ordered.contains(b) {
                    if idx > ordered.iter().position(|&r| r == *b).unwrap() {
                        valid = false;
                    }
                } else if ordered[idx] == *b && ordered.contains(a) {
                    if idx < ordered.iter().position(|&r| r == *a).unwrap() {
                        valid = false;
                    }
                }
            }
            if valid {
                break;
            } else {
                ordered.swap(idx, idx - 1);
                idx -= 1;
            }
        }
    }
    ordered[ordered.len() / 2] as usize
}
