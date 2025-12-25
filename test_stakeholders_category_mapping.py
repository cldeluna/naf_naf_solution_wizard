"""
Test stakeholder category mapping for backward compatibility.

This test verifies that old category names in JSON are correctly mapped
to current category names when uploading.
"""

import json
from wizard_data import (
    restore_session_state_from_data,
    get_title_only_session_state
)


def test_stakeholders_category_mapping():
    """Test that old category names are mapped to current ones."""
    
    print("\n=== Testing Stakeholders Category Mapping ===")
    
    # Create test JSON with old category names
    test_json = {
        "initiative": {
            "title": "Test Project",
            "description": "Test description"
        },
        "stakeholders": {
            "choices": {
                "Technical Stakeholders": "Individual Network Engineer",
                "Business Stakeholders": "IT Director",  # Old name - should be mapped
                "User Stakeholders": "Customers",  # Old name - should be mapped
                "User and Customer Stakeholders": "Internal users (ITSM / Service Desk)",
                "Governance and Risk Stakeholders": "None",
                "Business and Leadership Stakeholders": "None",
                "External/Vendor/Partner Stakeholders": "None"
            },
            "other": ""
        }
    }
    
    # Restore session state from JSON
    restored_updates = restore_session_state_from_data(test_json)
    
    # Verify category mapping worked
    choices = restored_updates["stakeholders_choices"]
    
    # Should have mapped old names to new ones
    assert "Business and Leadership Stakeholders" in choices, \
        "Mapped 'Business and Leadership Stakeholders' not found"
    assert choices["Business and Leadership Stakeholders"] == "IT Director", \
        f"Expected 'IT Director' but got '{choices['Business and Leadership Stakeholders']}'"
    
    assert "User and Customer Stakeholders" in choices, \
        "Mapped 'User and Customer Stakeholders' not found"
    assert choices["User and Customer Stakeholders"] == "Customers", \
        f"Expected 'Customers' but got '{choices['User and Customer Stakeholders']}'"
    
    # Should preserve unmapped categories
    assert choices["Technical Stakeholders"] == "Individual Network Engineer"
    assert choices["Governance and Risk Stakeholders"] == "None"
    
    # Should NOT have the old category names
    assert "Business Stakeholders" not in choices, \
        "Old 'Business Stakeholders' should not exist after mapping"
    assert "User Stakeholders" not in choices, \
        "Old 'User Stakeholders' should not exist after mapping"
    
    print("✅ Old category names correctly mapped to new ones")
    print("  - 'Business Stakeholders' → 'Business and Leadership Stakeholders'")
    print("  - 'User Stakeholders' → 'User and Customer Stakeholders'")
    
    print("\n✅ Category mapping test passed!")


def test_stakeholders_mapping_with_actual_values():
    """Test mapping with the actual values from the user's JSON."""
    
    print("\n=== Testing with User's Actual JSON Values ===")
    
    # Use the exact JSON structure from the user
    user_json = {
        "initiative": {
            "title": "User Project"
        },
        "stakeholders": {
            "choices": {
                "Technical Stakeholders": "Individual Network Engineer",
                "Business Stakeholders": "IT Director",
                "User Stakeholders": "Customers",
                "User and Customer Stakeholders": "None",
                "Governance and Risk Stakeholders": "None",
                "Business and Leadership Stakeholders": "None",
                "External/Vendor/Partner Stakeholders": "None"
            }
        }
    }
    
    # Restore session state
    restored_updates = restore_session_state_from_data(user_json)
    
    # Verify the problematic categories are now correctly mapped
    choices = restored_updates["stakeholders_choices"]
    
    # These should now be correctly mapped and display in the UI
    assert choices["Business and Leadership Stakeholders"] == "IT Director", \
        "IT Director should be mapped to Business and Leadership Stakeholders"
    assert choices["User and Customer Stakeholders"] == "Customers", \
        "Customers should be mapped to User and Customer Stakeholders"
    
    print("✅ User's JSON values correctly mapped")
    print(f"  - IT Director now in 'Business and Leadership Stakeholders'")
    print(f"  - Customers now in 'User and Customer Stakeholders'")
    
    # Simulate widget initialization to verify they would display
    for category, value in choices.items():
        if value not in ["None", ""]:
            print(f"  - Widget '{category}' would display: {value}")
    
    print("\n✅ User JSON mapping test passed!")


def test_stakeholders_mapping_edge_cases():
    """Test edge cases for category mapping."""
    
    print("\n=== Testing Category Mapping Edge Cases ===")
    
    # Test with unknown category (should remain unchanged)
    test_json_1 = {
        "initiative": {"title": "Test"},
        "stakeholders": {
            "choices": {
                "Unknown Category": "Some value",
                "Technical Stakeholders": "Network team"
            }
        }
    }
    
    restored_1 = restore_session_state_from_data(test_json_1)
    choices_1 = restored_1["stakeholders_choices"]
    
    # Unknown category should remain as-is
    assert "Unknown Category" in choices_1, \
        "Unknown category should be preserved"
    assert choices_1["Unknown Category"] == "Some value", \
        "Unknown category value should be preserved"
    
    print("✅ Unknown categories preserved correctly")
    
    # Test with empty choices
    test_json_2 = {
        "initiative": {"title": "Test"},
        "stakeholders": {
            "choices": {}
        }
    }
    
    restored_2 = restore_session_state_from_data(test_json_2)
    assert restored_2["stakeholders_choices"] == {}, \
        "Empty choices should remain empty"
    
    print("✅ Empty choices handled correctly")
    
    # Test with all old categories
    test_json_3 = {
        "initiative": {"title": "Test"},
        "stakeholders": {
            "choices": {
                "Business Stakeholders": "CEO",
                "User Stakeholders": "End Users"
            }
        }
    }
    
    restored_3 = restore_session_state_from_data(test_json_3)
    choices_3 = restored_3["stakeholders_choices"]
    
    assert len(choices_3) == 2, \
        f"Expected 2 categories but got {len(choices_3)}"
    assert "Business and Leadership Stakeholders" in choices_3
    assert "User and Customer Stakeholders" in choices_3
    assert choices_3["Business and Leadership Stakeholders"] == "CEO"
    assert choices_3["User and Customer Stakeholders"] == "End Users"
    
    print("✅ All old categories mapped correctly")
    
    print("\n✅ Edge cases test passed!")


if __name__ == "__main__":
    print("=" * 60)
    print("Testing Stakeholders Category Mapping")
    print("=" * 60)
    
    test_stakeholders_category_mapping()
    test_stakeholders_mapping_with_actual_values()
    test_stakeholders_mapping_edge_cases()
    
    print("\n" + "=" * 60)
    print("🎉 All category mapping tests passed successfully!")
    print("=" * 60)
