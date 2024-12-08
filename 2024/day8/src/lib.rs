use std::collections::{HashMap, HashSet};
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn valid(x: isize, y: isize, map: &Vec<Vec<char>>) -> bool {
    x >= 0 && y >= 0 && (x as usize) < map.len() && (y as usize) < map[0].len()
}

pub fn parse_file(filename: &str) {
    let map = parse_file_helper(filename);
    find_antinodes(&map);
}

fn parse_file_helper(filename: &str) -> Vec<Vec<char>> {
    let mut map: Vec<Vec<char>> = vec![];
    if let Ok(lines) = read_lines(filename) {
        for line in lines.flatten() {
            let row: Vec<char> = line.trim().chars().collect();
            map.push(row);
        }
    }
    map
}

fn calc_distances(i: isize, j: isize, i1: isize, j1: isize, i2: isize, j2: isize) -> (isize, isize, (isize, isize), (isize, isize)) {
    let delta1 = (i - i1, j - j1);
    let delta2 = (i - i2, j - j2);
    ((i-i1).abs()+(j-j1).abs(), (i-i2).abs()+(j-j2).abs(), delta1, delta2)
}

fn eval_part_1(i: isize, j: isize, map: &Vec<Vec<char>>, d1: isize, d2: isize, di1: isize, di2: isize, dj1: isize, dj2: isize) -> bool {
    (d1 == 2 * d2 || d1 * 2 == d2) && valid(i, j, map) && di1 * dj2 == dj1 * di2
}

fn eval_part_2(i: isize, j: isize, map: &Vec<Vec<char>>, di1: isize, di2: isize, dj1: isize, dj2: isize) -> bool {
    valid(i, j, map) && di1 * dj2 == dj1 * di2
}

fn find_antinodes(map: &Vec<Vec<char>>) {
    let mut antenna_positions: HashMap<char, Vec<(isize, isize)>> = HashMap::new();
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            if map[i][j] != '.' {
                antenna_positions.entry(map[i][j]).or_insert(vec![]).push((i as isize, j as isize));
            }
        }
    }
    let mut part_1_antinodes = HashSet::new();
    let mut part_2_antinodes = HashSet::new();
    for i in 0..map.len() {
        for j in 0..map[0].len() {
            let current_pos = (i as isize, j as isize);
            for (_, positions) in &antenna_positions {
                for (i1, j1) in positions {
                    for (i2, j2) in positions {
                        if (i1, j1) != (i2, j2) {
                            let (d1, d2, delta1, delta2) = calc_distances(i as isize, j as isize, *i1, *j1, *i2, *j2);
                            if eval_part_1(i as isize, j as isize, map, d1, d2, delta1.0, delta2.0, delta1.1, delta2.1) {
                                part_1_antinodes.insert(current_pos);
                            }
                            if eval_part_2(i as isize, j as isize, map, delta1.0, delta2.0, delta1.1, delta2.1) {
                                part_2_antinodes.insert(current_pos);
                            }
                        }
                    }
                }
            }
        }
    }
    println!("Part 1: Count is {}", part_1_antinodes.len());
    println!("Part 2: Count is {}", part_2_antinodes.len());
}
