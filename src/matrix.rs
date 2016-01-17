extern crate nalgebra;

use self::nalgebra::{DMat, Row};
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
