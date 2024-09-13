
const THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    n > THRESHOLD
}

fn main() {
print!("{}",THRESHOLD);
println!("{}",is_big(13));
 
}