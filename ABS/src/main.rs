use std::io::*;
use std::str::FromStr;

use proconio::input;

fn read<T: FromStr>() -> T {
    let stdin = stdin();
    let stdin = stdin.lock();
    let token: String = stdin
        .bytes()
        .map(|c| c.expect("failed to read char") as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect();
    token.parse().ok().expect("failed to parse token")
}

fn practice_1(){
    let a: i32 = read();
    let b: i32 = read();
    let c: i32 = read();
    let s: String = read();
    println!("{} {}", a+b+c,s);
}

fn practice_2(){
    let a: i32 = read();
    let b: i32 = read();
    if a % 2 == 0 || b % 2 == 0 {
        println!("Even");
    }else{
        println!("Odd");
    }
}
fn practice_3(){
    // let s: i32 = read();
    // let (s1,s2,s3) = (s/100,s%100/10,s % 10);
    // println!("{}", s1 + s2 + s3);
    
    input! {
        s: String,
    };

    let mut count = 0;
    for c in s.chars() {
        if c == '1' {
            count += 1;
        }
    }
    println!("{}", count);
}

fn practice_4(){
    input! {
        N: i32,
    }
    let mut max = 10000000;
    for _ in 0..N{
        input! {
            mut t: i64,
        }
        let mut cnt = 0;
        while t % 2 == 0 {
            t = t / 2;
            cnt += 1;
        }
        max = if max > cnt {
            cnt
        }else{
            max
        };
        
    }
    println!("{}",max);
}

fn practice_5(){
    input! {
        A: i32,
        B: i32,
        C: i32,
        X: i32,
    }
    let mut cnt = 0 ;
    for a in 0..A+1 {
        for b in 0..B+1{
            for c in 0 .. C+1{
                if X == 500 * a + 100 * b + 50 * c {
                    cnt += 1;
                }
            }
        }
    }
    println!("{}", cnt);
}

fn practice_6(){
    input! {
        N: i32,
        A: i32,
        B: i32,
    }

    let mut result = 0;
    for i in 1..N+1{
        let mut sum = 0;
        let mut t = i;
        while t > 0 {
            sum += t % 10;
            t /= 10;
        }

        if sum >= A && sum <= B {
            result += i;
        }
        
    }
    println!("{}", result);
}

fn practice_7(){
    input! {
        n: usize,
        mut a: [i32;n],
    }
    let mut alice_cards = Vec::<i32>::new();
    let mut bob_cards = Vec::<u32>::new();
    a.sort();
    a.reverse();
    
    let mut alice_score = 0;
    let mut bob_score = 0;

    for i in a.iter().enumerate(){
        if i.0 % 2 == 0 {
            alice_score += i.1;
        }else{
            bob_score += i.1;
        }
    }
    println!("{}", alice_score - bob_score);
    
}

fn practice_8(){

}
fn main() {
    practice_8();
}