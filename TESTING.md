# Testing Strategy

The Quick-Calc application uses both unit testing and integration testing to verify correctness.

## What was tested

The core mathematical functions were tested individually using unit tests. This ensures that each function behaves correctly in isolation.

Integration tests verify the interaction between the user input layer and the calculator logic.

## What was not tested

User interface design and performance testing were not included because the focus of this assignment is functional correctness.

## Testing Pyramid

The test suite follows the testing pyramid principle. Most tests are unit tests (8 tests), while a smaller number are integration tests (2 tests). This ensures fast execution and easier debugging.

## Black-box vs White-box Testing

Unit tests mainly use white-box testing because the internal logic of functions is known and directly tested.

Integration tests follow black-box testing because they verify behavior through the interface without inspecting internal implementation.

## Functional vs Non-Functional Testing

This project focuses on functional testing, ensuring the calculator performs the correct operations. Non-functional testing such as performance or security testing was not implemented.

## Regression Testing

The test suite can be reused whenever the code changes. Running the tests after updates ensures that previously working functionality is not broken.

## Test Results

| Test Name | Type | Result |
|-----------|------|-------|
| test_add | Unit | Pass |
| test_subtract | Unit | Pass |
| test_multiply | Unit | Pass |
| test_divide | Unit | Pass |
| test_divide_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_full_operation | Integration | Pass |
| test_clear_function | Integration | Pass |
