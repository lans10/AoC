use day1::Config;
use day1::parse_part1;
use day1::parse_part2;

fn main(){
	println!("Day 1, Advent of Code 2024");
    //let filename = "./debug.txt";
    let filename = "./input.txt";
    let config = Config::new(&filename.to_string());
    parse_part1(&config.v1, &config.v2);
	parse_part2(&config.v1, &config.v2_sum);
}
