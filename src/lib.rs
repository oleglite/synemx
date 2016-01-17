extern crate libc;

mod matrix;

use matrix::Matrix;


#[no_mangle]
pub extern fn make_matrix(h: u32, w: u32, initial_value: f32) -> *const libc::c_void {
    let matrix = Box::new(Matrix::new(h as usize, w as usize, initial_value));
    Box::into_raw(matrix) as *mut libc::c_void
}

#[no_mangle]
pub extern fn get(m: &Matrix, y: usize, x: usize) -> f32 {
    m.get(y, x)
}

#[no_mangle]
pub extern fn set(m: &mut Matrix, y: usize, x: usize, value: f32) {
    m.set(y, x, value);
}
