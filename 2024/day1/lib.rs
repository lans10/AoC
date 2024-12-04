use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

struct Config{
    v1: Vec<i32>, v2: Vec<i32>
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

// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
