use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

pub fn parse_file(filename: &String){
	let mut xmas_box: Vec<Vec<char>> = vec![];
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			let row: Vec<char> = line.trim().chars().collect();
			xmas_box.push((*row).to_vec());
		}
	}
	parse_file_part_1(&xmas_box);
	parse_file_part_2(&xmas_box);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn parse_file_part_1(xmas_box: &Vec<Vec<char>>){
	let directions = vec![
        (-1, 0, "n"),
        (1, 0, "s"),
        (0, -1, "w"),
        (0, 1, "e"),
		(-1, 1, "ne"),
		(1, 1, "se"),
		(-1, -1, "nw"),
		(1, -1, "sw"),
    ];
	let mut sum = 0;
	for i in 0..xmas_box.len(){
		for j in 0..xmas_box[0].len(){
			if xmas_box[i][j] == 'X'{
				sum += find_xmas(i, j, &directions, &xmas_box);
			}
		}
	}
	println!("Part 1: XMAS count is {}", sum);
}

fn parse_file_part_2(xmas_box: &Vec<Vec<char>>){
	let mut sum = 0;
	for i in 1..xmas_box.len()-1{
		for j in 1..xmas_box[0].len()-1{
			if xmas_box[i][j] == 'A'{
				if 
				((xmas_box[i-1][j-1] == 'M' && xmas_box[i+1][j+1] == 'S') || (xmas_box[i-1][j-1] == 'S' && xmas_box[i+1][j+1] == 'M')) &&
				((xmas_box[i+1][j-1] == 'M' && xmas_box[i-1][j+1] == 'S') || (xmas_box[i+1][j-1] == 'S' && xmas_box[i-1][j+1] == 'M')){
					sum += 1;
				}
			}
		}
	}
	println!("Part 2: XMAS count is {}", sum);
}

fn valid(x: isize, y:isize, xmas_box: &Vec<Vec<char>>) -> bool{
	return x >= 0  && y >= 0 && x < xmas_box.len() as isize && y < xmas_box[0].len() as isize;
}

fn find_xmas(i: usize, j: usize, directions: &Vec<(isize, isize, &str)>, xmas_box: &Vec<Vec<char>>) -> usize {
    let mut count = 0;
    for &(di, dj, _) in directions {
        let mut x = i as isize;
        let mut y = j as isize;
        x += di;
        y += dj;
        if !valid(x, y, &xmas_box) || xmas_box[x as usize][y as usize] != 'M' {
            continue;
        }
        x += di;
        y += dj;
        if !valid(x, y, &xmas_box) || xmas_box[x as usize][y as usize] != 'A' {
            continue;
        }
        x += di;
        y += dj;
        if !valid(x, y, &xmas_box) || xmas_box[x as usize][y as usize] != 'S' {
            continue;
        }
        count += 1;
    }
    count
}