use pyo3::prelude::*;

#[pyfunction]
fn get_value_of_pi(n: u32) -> f32 {
    let mut total_of_sum: f32 = 0.0;
    let mut denominator: f32 = 1.0;

    for i in 0..n {
        let condition = i % 2;
        if condition == 0 {
            total_of_sum += 4.0 / denominator
        } else {
            total_of_sum -= 4.0 / denominator
        }
        denominator += 2.0
    }

    return total_of_sum;
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
#[pyo3(name = "valids_rs")]
fn rust_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(get_value_of_pi, m)?)?;

    Ok(())
}
