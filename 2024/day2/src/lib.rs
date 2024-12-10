use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn parse_file(filename: &String){
	let mut safe_count_1 = 0;
	let mut safe_count_2 = 0;
	let mut v1: Vec<i32> = Vec::new();
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			let parts: Vec<&str> = line.split_whitespace().collect();
			for part in parts{
				v1.push(part.parse::<i32>().unwrap());
			}
			let mut check = check_list(&v1);
			if check{
				safe_count_1 += 1;
				}else{
				for i in 0..v1.len(){
					let mut v2 = v1.clone();
					v2.remove(i);
					check = check_list(&v2);
					v2.clear();
					if check{
						safe_count_2 += 1;
						break;
					}
				}
			}
			v1.clear();
		}
	}
	println!("Part 1: Safe reports = {}", safe_count_1);
	println!("Part 2: Safe reports = {}", safe_count_1+safe_count_2);
}

fn check_list(v1: &Vec<i32>) -> bool{
    let inc;
    if v1[0] < v1[1] && v1[1] < v1[2] {
        inc = true;
		} else if v1[0] > v1[1] && v1[1] > v1[2] {
        inc = false;
		} else {
        return false;
	}
    for n in 0..v1.len() - 1 {
        if (1..=3).contains(&i32::abs(v1[n] - v1[n + 1])) {
            if inc {
	if v1[n] >= v1[n + 1] {
	return false;
	}
	} else {
	if v1[n] <= v1[n + 1] {
	return false;
	}
	}
	} else {
	return false;
	}
    }
    return true;
	}	