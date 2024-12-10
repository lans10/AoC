use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

pub fn parse_file(filename: &str) {
    if let Ok(lines) = read_lines(filename) {
        for line in lines.flatten() {
			let initial: Vec<Option<usize>> = create_initial_1(&line);
            part_1(&initial);

			let initial_2: Vec<(usize,usize)> = create_initial_2(&line);
			part_2(&initial_2);
        }
    }
}

fn create_initial_1(disk_map: &str) -> Vec<Option<usize>> {
    let mut map: Vec<Option<usize>> = Vec::new();
    let mut file_id = 0;
    for (i, block_count) in disk_map.chars().enumerate() {
        if let Some(count) = block_count.to_digit(10) {
            if i % 2 == 0 {
				map.extend(std::iter::repeat(Some(file_id)).take(count as usize));
				file_id += 1;
            }
            else {
                map.extend(std::iter::repeat(None).take(count as usize));
            }
        }
    }
    while map.last() == Some(&None) {
        map.pop();
    }
    map
}

fn part_1(map: &Vec<Option<usize>>){
    let part_1_map = frag_part_1(map.clone());
    let sum = checksum_1(part_1_map);
    println!("Part 1: Checksum is {}", sum);
}

fn frag_part_1(map: Vec<Option<usize>>) -> Vec<Option<usize>> {
	let mut blocks = map.clone();
    let mut i = 0;
    while i < blocks.len() {
        if blocks[i].is_none() {
            if let Some(block) = blocks.pop() {
                blocks[i] = block;
            }
        }
        while blocks.last() == Some(&None) {
            blocks.pop();
        }
        i += 1;
    }
    blocks
}

fn checksum_1(fs: Vec<Option<usize>>) -> usize {
	let mut sum: usize = 0;
	let mut i: usize = 0;
	for b in fs{
		if b.is_some(){
			sum += i*b.unwrap();
			i+=1;
		}
	}
	sum
}

fn part_2(map: &Vec<(usize, usize)>){
    let part_2_map:Vec<(usize, usize)> = frag_part_2(map.clone());
    let sum = checksum_2(part_2_map);
    println!("Part 2: Checksum is {}", sum);
}

fn create_initial_2(disk_map: &str) -> Vec<(usize,usize)> {
    let mut map: Vec<(usize,usize)> = Vec::new();
    let mut file_id: usize = 0;
    for (i, block_count) in disk_map.chars().enumerate() {
        if let Some(count) = block_count.to_digit(10) {
            if i % 2 == 0 {
				map.push((file_id,count as usize));
                file_id += 1;
            } else {
				map.push((usize::MAX,count as usize));
            }
        }
    }
    map
}

fn frag_part_2(mut blocks: Vec<(usize, usize)>) -> Vec<(usize, usize)> {
    let mut i = blocks.len();
    while i > 0 {
        i -= 1;
        let (id, size) = blocks[i];
        if id != usize::MAX {
            let free_index = find_earliest_free(size, &blocks);
            if free_index != usize::MAX && free_index < i {
                let available_space = blocks[free_index].1;
                if available_space == size {
					blocks.swap(free_index, i);
                } else if available_space > size {
                    blocks[free_index].1 -= size;
                    blocks[i] = (usize::MAX, size);
                    blocks.insert(free_index, (id, size));
                    i += 1;
                }
            }
        }
    }
    blocks
}

fn find_earliest_free(n: usize, map: &Vec<(usize,usize)>) -> usize {
	let mut i: usize = 0;
	while i < map.len(){
		if map[i].1 >= n && map[i].0 == usize::MAX{
			return i;
		}
		i+=1;
	}
	return usize::MAX;
}

fn checksum_2(fs: Vec<(usize, usize)>) -> usize {
    let mut sum: usize = 0;
    let mut v_i: usize = 0;
    
    for (file_id, block_count) in fs {
        if file_id != usize::MAX {
            for _ in 0..block_count {
                sum += file_id * v_i;
                v_i += 1;
            }
        } else {
            v_i += block_count;
        }
    }
    sum
}
