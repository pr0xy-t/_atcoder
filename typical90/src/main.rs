
use proconio::input;

// fn Yokan_Party_001(){
//     input! {
//         L:i64,
//         target:i64,
//         // N: i64,
//         // L: i64,
//         // K: i64,
//         // mut A: [i64;N],
//     }
//     let mut M = L;
//     let mut max = L;
//     let mut mid = L/2;
//     let mut min = 0;
//     // let target = 3;
//     loop {
//         println!("{} {} {}",min,mid,max);
        
//         if mid == target{
//             println!("{}",mid);
//             break;
//         }else if target == max || target == min{
//             println!("{}",target);
//             break;
//         }else if mid == min || mid == max{
//             println!("{}",mid);
//             break;
//         }
//         if target < mid {
//             max = mid;
//             mid = (min + max ) /2;
//         }else if target > mid {
//             min = mid;
//             mid = (min + max ) /2;
//         }else{
//             println!("{}",mid);
//             break;
//         }
//     }
// }

fn Cross_Sum_004(){
    input! {
        H:usize,
        W:usize,
        a:[[i32; W];H],
    }
    let mut h:[i32;2000];
    let mut w:[i32;2000] = [0;2000];
    for j in 0..W{
        for i in 0..H{
            w[j] += a[i][j];
        }
    }
    for i in 0..H{
        for j in 0..W{
            let mut sum:i32 = a[i].iter().sum();
            sum += w[j];
            sum -= a[i][j];
            if j == (W-1){
                println!("{}",sum);
            }else{
                print!("{} ",sum);
            }
            
        }
    }
  
}
fn main() {
    Cross_Sum_02();
}
