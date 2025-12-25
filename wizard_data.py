"""
Testable functions for the NAF Solution Wizard data handling.

This module extracts the core logic for:
1. Building the JSON payload from session state
2. Restoring session state from uploaded JSON data

These functions are pure (no Streamlit dependencies) and can be tested directly.
"""

from typing import Dict, Any, List
from pathlib import Path
import yaml


def build_wizard_payload(session_state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Build a comprehensive wizard payload from session state.
    
    Args:
        session_state: Streamlit session state dictionary
        
    Returns:
        Complete payload dictionary with all wizard data
    """
    # Get the actual deployment strategy value
    deployment_strategy = session_state.get("_wizard_deployment_strategy", "")
    if deployment_strategy == "Other":
        deployment_strategy = session_state.get("_wizard_deployment_strategy_other", "")
    
    # Get the actual category value
    category = session_state.get("_wizard_category", "")
    if category == "Other":
        category = session_state.get("_wizard_category_other", "")
    
    payload = {
        "initiative": {
            "title": session_state.get("_wizard_automation_title", ""),
            "description": session_state.get("_wizard_automation_description", ""),
            "category": category,
            "problem_statement": session_state.get("_wizard_problem_statement", ""),
            "expected_use": session_state.get("_wizard_expected_use", ""),
            "error_conditions": session_state.get("_wizard_error_conditions", ""),
            "assumptions": session_state.get("_wizard_assumptions", ""),
            "deployment_strategy": deployment_strategy,
            "deployment_strategy_description": session_state.get("_wizard_deployment_strategy_description", ""),
            "out_of_scope": session_state.get("_wizard_out_of_scope", ""),
            "no_move_forward": session_state.get("no_move_forward", ""),
            "no_move_forward_reasons": session_state.get("no_move_forward_reasons", []),
        },
        "my_role": {
            "who": session_state.get("my_role_who", ""),
            "skills": session_state.get("my_role_skills", ""),
            "developer": session_state.get("my_role_dev", ""),
        },
        "stakeholders": {
            "choices": session_state.get("stakeholders_choices", {}),
            "other": (session_state.get("stakeholders_other_text") or "").strip(),
        },
        # Add other sections as needed for complete testing
        "presentation": session_state.get("presentation_data", {}),
        "intent": session_state.get("intent_data", {}),
        "observability": session_state.get("observability_data", {}),
        "orchestration": session_state.get("orchestration_data", {}),
        "collector": session_state.get("collector_data", {}),
        "executor": session_state.get("executor_data", {}),
        "dependencies": session_state.get("dependencies_data", []),
        "timeline": session_state.get("timeline_data", {}),
    }
    
    return payload


def restore_session_state_from_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract session state updates from uploaded JSON data.
    
    Args:
        data: Dictionary containing the uploaded JSON data
        
    Returns:
        Dictionary of session state updates
    """
    updates = {}
    
    # Extract initiative data
    ini = data.get("initiative", {})
    if ini.get("title") is not None:
        updates["_wizard_automation_title"] = str(ini.get("title") or "")
    if ini.get("description") is not None:
        updates["_wizard_automation_description"] = str(ini.get("description") or "")
    if ini.get("problem_statement") is not None:
        updates["_wizard_problem_statement"] = str(ini.get("problem_statement") or "")
    if ini.get("expected_use") is not None:
        updates["_wizard_expected_use"] = str(ini.get("expected_use") or "")
    if ini.get("error_conditions") is not None:
        updates["_wizard_error_conditions"] = str(ini.get("error_conditions") or "")
    if ini.get("assumptions") is not None:
        updates["_wizard_assumptions"] = str(ini.get("assumptions") or "")
    if ini.get("deployment_strategy") is not None:
        deploy_strategy = str(ini.get("deployment_strategy") or "")
        # Check if the deployment strategy is in the predefined list
        deploy_yaml_path = Path(__file__).parent / "deployment_strategies.yml"
        try:
            with open(deploy_yaml_path, "r") as f:
                deploy_data = yaml.safe_load(f)
            deploy_options = list(deploy_data.keys()) if deploy_data else []
        except Exception:
            deploy_options = []
        
        if deploy_strategy in deploy_options:
            # It's a standard strategy
            updates["_wizard_deployment_strategy"] = deploy_strategy
            updates["_wizard_deployment_strategy_other"] = ""
        elif deploy_strategy and deploy_strategy != "— Select a deployment strategy —":
            # It's a custom strategy, put it in "Other"
            updates["_wizard_deployment_strategy"] = "Other"
            updates["_wizard_deployment_strategy_other"] = deploy_strategy
        else:
            # Empty or placeholder
            updates["_wizard_deployment_strategy"] = "— Select a deployment strategy —"
            updates["_wizard_deployment_strategy_other"] = ""
    if ini.get("deployment_strategy_description") is not None:
        updates["_wizard_deployment_strategy_description"] = str(ini.get("deployment_strategy_description") or "")
    if ini.get("out_of_scope") is not None:
        updates["_wizard_out_of_scope"] = str(ini.get("out_of_scope") or "")
    if ini.get("no_move_forward") is not None:
        updates["no_move_forward"] = str(ini.get("no_move_forward") or "")
    if ini.get("no_move_forward_reasons") is not None:
        updates["no_move_forward_reasons"] = ini.get("no_move_forward_reasons", []) or []
        updates["no_move_forward_reasons"] = updates["no_move_forward_reasons"] if isinstance(updates["no_move_forward_reasons"], list) else []
    
    # Restore category
    if ini.get("category") is not None:
        category_value = ini.get("category")
        try:
            yaml_path = Path(__file__).parent / "use_case_categories.yml"
            with open(yaml_path, "r") as f:
                categories_data = yaml.safe_load(f)
            category_options = list(categories_data.keys()) if categories_data else []
        except Exception:
            category_options = []
        
        if category_value in category_options:
            updates["_wizard_category"] = category_value
            updates["_wizard_category_other"] = ""
        else:
            updates["_wizard_category"] = "Other"
            updates["_wizard_category_other"] = category_value
    
    # Restore stakeholders
    stakeholders = data.get("stakeholders", {})
    if stakeholders is not None and isinstance(stakeholders, dict):
        if stakeholders.get("choices") is not None and isinstance(stakeholders.get("choices"), dict):
            # Use choices as-is since we no longer support old category names
            updates["stakeholders_choices"] = stakeholders.get("choices")
        else:
            updates["stakeholders_choices"] = {}
        if stakeholders.get("other") is not None:
            updates["stakeholders_other_text"] = str(stakeholders.get("other") or "")
        else:
            updates["stakeholders_other_text"] = ""
    else:
        # Handle None or non-dict stakeholders
        updates["stakeholders_choices"] = {}
        updates["stakeholders_other_text"] = ""
    
    # Restore my role
    my_role = data.get("my_role", {}) or {}
    if my_role.get("who") is not None:
        updates["my_role_who"] = str(my_role.get("who") or "")
    if my_role.get("skills") is not None:
        updates["my_role_skills"] = str(my_role.get("skills") or "")
    if my_role.get("developer") is not None:
        updates["my_role_dev"] = str(my_role.get("developer") or "")
    
    return updates


def get_title_only_session_state(title: str) -> Dict[str, Any]:
    """
    Create a minimal session state with only the title field set.
    Used for testing the title field round-trip.
    
    Args:
        title: The title to set
        
    Returns:
        Minimal session state dictionary
    """
    return {
        "_wizard_automation_title": title,
        "_wizard_automation_description": "Here is a short description of my my new network automation project",
        "_wizard_category": "— Select a category —",
        "_wizard_category_other": "",
        "_wizard_problem_statement": "",
        "_wizard_expected_use": "This automation will be used whenever this task needs to be executed.",
        "_wizard_error_conditions": "",
        "_wizard_assumptions": "",
        "_wizard_deployment_strategy": "",
        "_wizard_deployment_strategy_description": "",
        "_wizard_out_of_scope": "",
        "no_move_forward": "",
        "no_move_forward_reasons": ["— Select one or more risks —"],
        "stakeholders_choices": {},
        "stakeholders_other_text": "",
        "my_role_who": "I'm a network engineer.",
        "my_role_skills": "I have some scripting skills and basic software development experience.",
        "my_role_dev": "I'll do it myself.",
        "my_role_who_other": "",
        "my_role_skills_other": "",
        "my_role_dev_other": "",
    }
