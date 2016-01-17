extern crate nalgebra;

use self::nalgebra::{DMat, Row};
use std::fmt;


pub struct Matrix {
    h: usize,  // number of signals, number of rows
    w: usize, // number of impulses in signal, number of columns
    matrix: DMat<f32>       // matrix where rows is signals
}


impl Matrix {
    /// Create message where all values is zeros
    pub fn new(h: usize, w: usize, initial_value: f32) -> Matrix {
        Matrix {
            h: h,
            w: w,
            matrix: DMat::from_elem(h, w, initial_value),
        }
    }

    // pub fn from_data(signals_number: usize, impulses_number: usize, data: &[f32]) -> Matrix {
    //     assert_eq!(signals_number * impulses_number, data.len());

    //     Matrix {
    //         signals_number: signals_number,
    //         impulses_number: impulses_number,
    //         matrix: DMat::from_row_vec(signals_number, impulses_number, data),
    //     }
    // }

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
