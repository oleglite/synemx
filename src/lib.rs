extern crate libc;

mod matrix;

use std::slice;
use libc::{c_void, int32_t, size_t, c_float};
use matrix::Matrix;


#[no_mangle]
pub extern fn matrix_new(h: size_t, w: size_t, data: *const c_float) -> *const libc::c_void {
    let values = unsafe { slice::from_raw_parts(data, (h * w) as usize) };
    let matrix = Box::new(Matrix::new(h as usize, w as usize, &values));
    Box::into_raw(matrix) as *mut libc::c_void
}

#[no_mangle]
pub extern fn matrix_create(h: size_t, w: size_t, initial_value: c_float) -> *const libc::c_void {
    let matrix = Box::new(Matrix::create(h as usize, w as usize, initial_value as f32));
    Box::into_raw(matrix) as *mut libc::c_void
}

#[no_mangle]
pub extern fn matrix_get(m: &Matrix, y: size_t, x: size_t) -> c_float {
    m.get(y as usize, x as usize) as c_float
}

#[no_mangle]
pub extern fn matrix_set(m: &mut Matrix, y: size_t, x: size_t, value: c_float) {
    m.set(y as usize, x as usize, value as f32);
}
