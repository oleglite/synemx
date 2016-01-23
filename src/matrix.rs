extern crate nalgebra;

use self::nalgebra::{DMat, DVec, Row};
use std::fmt;


pub struct Matrix {
    h: usize, 
    w: usize,
    matrix: DMat<f32>
}


impl Matrix {
    pub fn new(h: usize, w: usize, data: &[f32]) -> Matrix {
        assert_eq!(h * w, data.len());

        Matrix {
            h: h,
            w: w,
            matrix: DMat::from_row_vec(h, w, data),
        }
    }

    pub fn create(h: usize, w: usize, initial_value: f32) -> Matrix {
        Matrix {
            h: h,
            w: w,
            matrix: DMat::from_elem(h, w, initial_value),
        }
    }

    pub fn get(&self, y: usize, x: usize) -> f32 {
        self.matrix[(y, x)]
    }

    pub fn set(&mut self, y: usize, x: usize, value: f32) {
        self.matrix[(y, x)] = value;
    }

    pub fn average_similarity(&self, other: &Matrix ) -> f32 {
        assert_eq!(self.h, other.h);
        assert_eq!(self.w, other.w);

        let mut sim: f32 = 0.0;
        for y in 0 .. self.h {
            sim += similarity(self.matrix.row(y), other.matrix.row(y));
        }
        sim / (self.h as f32)
    }
}


impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        writeln!(f, "[");
        for i in 0..self.h {
            writeln!(f, "   {:?},", self.matrix.row(i).as_ref());
        }
        write!(f, "]")
    }
}


fn similarity(v1: DVec<f32>, v2: DVec<f32>) -> f32 {
    let mut min_acc: f32 = 0.0;
    let mut max_acc: f32 = 0.0;
    let mut limit: f32 = 0.0;

    for i in 0..v1.len() {
        let x1: f32 = v1[i];
        let x2: f32 = v2[i];

        if x1 > x2 {
            min_acc += x2;
            max_acc += x1;
            if x1 > limit {
                limit = x1;
            }
        } else {
            min_acc += x1;
            max_acc += x2;
            if x2 > limit {
                limit = x2;
            }
        }
    }
    if max_acc > 0.0 {
        (limit * min_acc / max_acc)
    } else {
        0.0
    }
}
