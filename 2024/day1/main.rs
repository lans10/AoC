use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut sum = 0;
    let mut v1 = Vec::new();
    let mut v2 = Vec::new();
    //if let Ok(lines) = read_lines("./debug.txt") {
    if let Ok(lines) = read_lines("./input.txt") {
        for line in lines.flatten() {
            //println!("{}",&line);
            let parts: Vec<&str> = line.split_whitespace().collect();
            let a = parts[0];
            let b = parts[1];
            v1.push(a.parse::<i32>().unwrap());
            v2.push(b.parse::<i32>().unwrap());
        }
    }
    v1.sort();
    v2.sort();
    //println!("{:?}", v1);
    //println!("{:?}", v2);
    for n in 0..v1.len(){
        sum += i32::abs(v1[n]-v2[n]);
    }
    println!("Sum is {}", sum);
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
