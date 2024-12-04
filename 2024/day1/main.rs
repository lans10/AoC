//TODO
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main(){
    //let filename = "./debug.txt";
    let filename = "./input.txt";
    let config = Config::new(&filename);
    parse_part1(config.v1, config.v2);
}

impl Config{
    fn new(filename: &String) -> Config{
        let mut v1 = Vec::new();
        let mut v2 = Vec::new();
        if let Ok(lines) = read_lines(filename) {
            for line in lines.flatten() {
                let parts: Vec<&str> = line.split_whitespace().collect();
                v1.push(parts[0].parse::<i32>().unwrap());
                v2.push(parts[1].parse::<i32>().unwrap());
            }
        }
        v1.sort();
        v2.sort();
        Config{v1,v2}
    }
}

fn parse_part1(v1:&Vec<i32>, v2:&Vec<i32>){
    let mut sum = 0;
    for n in 0..v1.len(){
        sum += i32::abs(v1[n]-v2[n]);
    }
    println!("Part 1:\nSum is {}", sum);
}

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
