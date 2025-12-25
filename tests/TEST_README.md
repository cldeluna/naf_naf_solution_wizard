# Test Documentation

This document describes the test structure and test files for the NAF Solution Wizard application.

## Test Directory Structure

```
naf_naf_solution_wizard/
├── tests/                          # Main test directory
│   ├── README.md                   # Original test documentation
│   ├── conftest.py                 # pytest configuration
│   ├── test_wizard_utils.py        # Tests for wizard utility functions
│   ├── test_data_generator.py      # Data generation tests
│   ├── upload_validator.py         # Upload validation utilities
│   ├── exports/                    # Test export outputs
│   ├── generated/                  # Generated test data
│   └── results/                    # Test results
│
├── test_title_roundtrip.py         # Top-level: Title field round-trip tests
├── test_deployment_strategy_other.py  # Top-level: Deployment Strategy "Other" tests
├── test_specific_fields.py         # Top-level: Specific field validation tests
├── test_stakeholders_none.py       # Top-level: Stakeholders "None" selection tests
├── test_stakeholders_widget_init.py # Top-level: Stakeholders widget initialization tests
├── test_stakeholders_full_flow.py  # Top-level: Stakeholders complete flow tests
├── test_stakeholders_category_mapping.py # Top-level: Stakeholders category mapping (deprecated)
├── test_upload_validation.py       # Top-level: Simple upload validation test
└── test_lorem.py                   # Top-level: Lorem ipsum test
```

## Test File Organization

### Tests Directory (`tests/`)
The `tests/` directory contains pytest-based tests that:
- Use pytest framework with fixtures and assertions
- Test utility functions and helper modules
- Have complex setup/teardown requirements
- Generate test data and validate exports

**Key files in `tests/` relevant to today's work:**
- `conftest.py` - pytest configuration and shared fixtures
- `test_wizard_utils.py` - Tests for wizard-specific utility functions
- `test_data_generator.py` - Test data generation and validation
- `upload_validator.py` - Validation utilities for uploaded data

### Top-Level Test Files
Test files at the repository root are standalone, pure Python tests that:
- Don't require pytest framework
- Can be run directly with `python test_file.py`
- Focus on specific business logic scenarios
- Test JSON serialization/deserialization
- Validate field-specific behavior

**Top-level test files:**

#### 1. `test_title_roundtrip.py`
**Purpose:** Tests the core JSON save/load functionality for the title field.

**Key Tests:**
- `test_title_field_roundtrip()` - Verifies only the title field changes when modified
- `test_json_serialization_roundtrip()` - Tests JSON serialization integrity
- `test_multiple_field_changes()` - Validates multiple field updates

**Dependencies:**
- `wizard_data.py` - Uses `build_wizard_payload()` and `restore_session_state_from_data()`

#### 2. `test_deployment_strategy_other.py`
**Purpose:** Tests the "Other" option functionality for deployment strategy field.

**Key Tests:**
- `test_deployment_strategy_other_roundtrip()` - Custom strategy preservation
- `test_standard_deployment_strategy()` - Standard strategy handling
- `test_unknown_deployment_strategy()` - Unknown strategy moved to "Other"

**Dependencies:**
- `wizard_data.py` - Tests payload building and session state restoration
- `deployment_strategies.yml` - Validates against predefined strategies

#### 3. `test_specific_fields.py`
**Purpose:** Tests specific field scenarios as requested by users.

**Key Tests:**
- `test_category_device_onboarding()` - Category "Device Onboarding" save/load
- `test_deployment_strategy_other_my_own()` - Custom strategy "My own Strategy"
- `test_json_roundtrip_combined()` - Both fields together

**Dependencies:**
- `wizard_data.py` - Core data transformation functions
- `use_case_categories.yml` - Validates category names

#### 4. `test_stakeholders_none.py`
**Purpose:** Tests stakeholders field handling with "None" selections.

**Key Tests:**
- `test_stakeholders_with_none_selections()` - Verifies "None" selections are preserved
- `test_stakeholders_empty_and_none()` - Tests empty and None stakeholder data
- `test_stakeholders_all_none()` - Validates all stakeholders set to "None"

**Dependencies:**
- `wizard_data.py` - Tests restore_session_state_from_data() for stakeholders

#### 5. `test_stakeholders_widget_init.py`
**Purpose:** Tests that stakeholders widgets are properly initialized from uploaded JSON.

**Key Tests:**
- `test_stakeholders_widget_initialization()` - Verifies widget keys get uploaded values
- `test_stakeholders_widget_with_empty_data()` - Tests empty data handling

**Dependencies:**
- `wizard_data.py` - Tests session state restoration for widget initialization

#### 6. `test_stakeholders_full_flow.py`
**Purpose:** Tests complete stakeholders flow including selectbox index calculation.

**Key Tests:**
- `test_stakeholders_selectbox_index_calculation()` - Verifies correct index calculation
- `test_stakeholders_full_roundtrip()` - Tests complete save/load cycle
- `test_stakeholders_edge_cases()` - Tests edge cases and error handling

**Dependencies:**
- `wizard_data.py` - Tests payload building and restoration

#### 7. `test_stakeholders_category_mapping.py`
**Purpose:** Tests stakeholder category mapping for backward compatibility.

**Note:** This test is deprecated as category mapping has been removed. JSON files must use exact category names.

**Key Tests:**
- `test_stakeholders_category_mapping()` - Tests old category name mapping
- `test_stakeholders_mapping_with_actual_values()` - Tests with user's JSON
- `test_stakeholders_mapping_edge_cases()` - Tests edge cases

#### 8. `test_upload_validation.py`
**Purpose:** Simple upload validation test (minimal implementation).

#### 9. `test_lorem.py`
**Purpose:** Lorem ipsum text generation test.

## Core Test Dependencies

### `wizard_data.py`
The central module for data transformation that most tests depend on:
- `build_wizard_payload(session_state)` - Converts session state to JSON payload
- `restore_session_state_from_data(data)` - Converts JSON back to session state updates
- `get_title_only_session_state(title)` - Creates minimal test session state

### Configuration Files
- `deployment_strategies.yml` - Predefined deployment strategies
- `use_case_categories.yml` - Predefined categories for validation

## Running Tests

### Running Top-Level Tests
```bash
# Run individual test files
python test_title_roundtrip.py
python test_deployment_strategy_other.py
python test_specific_fields.py
python test_stakeholders_none.py
python test_stakeholders_widget_init.py
python test_stakeholders_full_flow.py
python test_stakeholders_category_mapping.py  # Deprecated

# All top-level tests are self-contained and can be run directly
```

### Running pytest Tests
```bash
# Run all tests in tests/ directory
pytest tests/

# Run specific test file
pytest tests/test_wizard_utils.py

# Run with verbose output
pytest tests/ -v
```

## Test Relationships

```
wizard_data.py (Core Module)
├── test_title_roundtrip.py ──┐
├── test_deployment_strategy_other.py ──┐
├── test_specific_fields.py ──┐
├── test_stakeholders_none.py ──┐
├── test_stakeholders_widget_init.py ──┐
├── test_stakeholders_full_flow.py ──┐
├── test_stakeholders_category_mapping.py ──┐ (deprecated)
    └── All test JSON save/load functionality

pages/20_NAF_Solution_Wizard.py (Main UI)
├── test_stakeholders_widget_init.py
├── test_stakeholders_full_flow.py
    └── Tests widget initialization and index calculation

utils.py
├── tests/test_wizard_utils.py
    └── Test utility functions
```

## Test Coverage Areas

1. **Data Transformation**
   - JSON serialization/deserialization
   - Session state management
   - Field validation and transformation

2. **Field-Specific Behavior**
   - Category field (standard vs "Other")
   - Deployment strategy field (standard vs "Other")
   - Title field round-trip preservation

3. **Upload/Download**
   - JSON upload validation
   - Field population from uploaded data
   - Export format validation

4. **Business Logic**
   - Field value preservation
   - Custom strategy handling
   - Round-trip data integrity

## Best Practices

1. **Top-level tests** should:
   - Be self-contained and runnable with `python test_file.py`
   - Focus on business logic, not UI
   - Use pure functions from `wizard_data.py`

2. **pytest tests** should:
   - Use fixtures for setup/teardown
   - Follow pytest naming conventions
   - Test utility functions and integration points

3. **All tests should**:
   - Include clear assertions with helpful error messages
   - Test both success and failure cases
   - Document the purpose of each test function

## Future Test Additions

When adding new tests:
- For field-specific logic: Add to top-level test files
- For utility functions: Add to `tests/` directory with pytest
- For JSON serialization/validation: Add to top-level test files
- For complex scenarios: Consider creating a new top-level test file
