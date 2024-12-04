use day1::Config;
use day1::read_lines;

fn main(){
    //let filename = "./debug.txt";
    let filename = "./input.txt";
    let config = Config::new(&filename);
    parse_part1(config.v1, config.v2);
}

fn parse_part1(v1:&Vec<i32>, v2:&Vec<i32>){
    let mut sum = 0;
    for n in 0..v1.len(){
        sum += i32::abs(v1[n]-v2[n]);
    }
    println!("Part 1:\nSum is {}", sum);
}
