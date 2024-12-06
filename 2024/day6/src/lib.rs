use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::time::Instant;

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
	let mut map: Vec<Vec<char>> = vec![];
	if let Ok(lines) = read_lines(filename) {
		for line in lines.flatten() {
			let row: Vec<char> = line.trim().chars().collect();
			map.push((*row).to_vec());
		}
	}
	let map_copy = map.clone();
	'outer: for i in 0..map.len(){
		for j in 0..map[0].len(){
			if map[i][j] != '.' &&  map[i][j] != '#'{
				let guard_i = i;
				let guard_j = j;
				let guard_pos = map[i][j];
				let sum_1 = sum_walk(&guard_i, &guard_j, &guard_pos, &mut map);
				println!("Part 1: Guard steps = {}", sum_1);
				let sum_2 = obstacle_adder(guard_i, guard_j, guard_pos, &mut map, &map_copy);
				println!("Part 2: Obstacles = {}", sum_2);
				break 'outer;
			}
		}
	}
}

fn sum_walk(guard_i: &usize, guard_j: &usize, guard_pos: &char, map: &mut Vec<Vec<char>>) -> usize {
    let start_time = Instant::now();
	let mut steps: usize = 1;
    let mut curr_i: isize = *guard_i as isize;
    let mut curr_j: isize = *guard_j as isize;
    let mut curr_pos: char = *guard_pos;
    let mut di: isize;
    let mut dj: isize;
    map[curr_i as usize][curr_j as usize] = 'X';
    loop {
        if start_time.elapsed().as_millis() > 1 {
            return 0;
        }
        (di, dj) = get_dir(&curr_pos);
        let next_i = curr_i + di;
        let next_j = curr_j + dj;
        if !valid(&next_i, &next_j, &map) {
            return steps;
        }
        match map[next_i as usize][next_j as usize] {
            '.' => {
                map[next_i as usize][next_j as usize] = 'X';
                steps += 1;
                curr_i = next_i;
                curr_j = next_j;
            }
            '#' => {
                curr_pos = change_dir(curr_pos);
            }
            'X' => {
                curr_i = next_i;
                curr_j = next_j;
            }
            _ => {
                return steps;
            }
        }
    }
}

fn valid(x: &isize, y: &isize, map: &Vec<Vec<char>>) -> bool {
    *x >= 0 && *y >= 0 && *x < map.len() as isize && *y < map[0].len() as isize
}

fn get_dir(curr_pos: &char) -> (isize, isize){
	let directions = vec![
        (-1, 0, '^'),
        (1, 0, 'v'),
        (0, -1, '<'),
        (0, 1, '>'),
    ];
	for (a, b, c) in directions{
		if c == *curr_pos{
			return (a, b);
		}
	}
	(0, 0)
}

fn change_dir(curr_pos: char) -> char {
    match curr_pos {
        '^' => '>',
        '>' => 'v',
        'v' => '<',
        '<' => '^',
		_ => curr_pos,
    }
}

fn _print_map(map: &Vec<Vec<char>>){
	for i in map{
		println!("{:?}", i);
	}
	println!();
}

fn obstacle_adder(guard_i: usize, guard_j: usize, guard_pos: char, map: &Vec<Vec<char>>, map_copy: &Vec<Vec<char>>) -> usize {
    let mut candidates = 0;
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] == 'X' && (i!=guard_i || j!=guard_j) {
                let mut new_map = map_copy.clone();
                new_map[i][j] = '#';
				let sum = sum_walk(&guard_i, &guard_j, &guard_pos, &mut new_map);
				if sum == 0 {
                    candidates += 1;
                }
            }
        }
    }
    candidates
}