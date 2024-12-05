use day3::parse_file;

fn main() {
    println!("Day 3, Advent of Code 2024");
    //let filename = "./debug1.txt".to_string();
	//let filename = "./debug2.txt".to_string();
    let filename = "./input.txt".to_string();
	parse_file(&filename);
}