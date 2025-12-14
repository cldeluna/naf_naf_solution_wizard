#!/usr/bin/python3 -tt
# Project: naf_naf_solution_wizard
# Filename: naf_naf_solution_wizard.py
# claudiadeluna
# PyCharm

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/25/25"
__copyright__ = "Copyright (c) 2025 Claudia"
__license__ = "Python"


import utils
import streamlit as st


def main() -> None:
    """Landing page for the NAF‑NAF Wizard.

    This page orients users to the workflow and explains how the Use Case and
    Solution Wizard pages fit together when running as a multipage app.
    """

    st.set_page_config(
        page_title="NAF NAF Wizard App",
        page_icon="images/EIA_Favicon.png",
        layout="wide",
    )

    # Shared sidebar branding
    utils.render_global_sidebar()

    st.title("Network Automation Forum (NAF) Network Automation Framework (NAF) Wizard App")
    st.markdown(
        """
        This application helps you apply the Network Automation Forum's
        **Network Automation Framework (NAF)** to your own automation projects.

        The workflow is designed in two main steps:
        """
    )

    st.markdown("### 1. Start with the Use Case page to help you think through use cases")
    st.markdown(
        """
        Use the **Use Case** page to think through and **document the automation use cases** you are targeting:

        - What problem are you trying to solve?
        - Who are the primary users and stakeholders?
        - What is in scope and out of scope?
        - What assumptions, risks, or dependencies should be called out?
        - What are the steps required to execute the use case?

        Treat this as a structured notepad for one or more *stories* of the automation.
        The more clearly you define the use cases, the easier it is to build a
        meaningful solution design.
        """
    )

    st.markdown("### 2. Then use the Solution Wizard page")
    st.markdown(
        """
        After you have one or more use cases defined, move to the
        **Solution Wizard** page:

        - Walk through each NAF component: Presentation, Intent, Observability,
          Orchestration, Collector, and Executor.
        - Capture how your automation will interact with people and systems.
        - Describe how state is represented, observed, and changed.
        - Identify external dependencies and sketch a staffing/timeline plan.

        The wizard can generate a **high‑level solution document** (JSON +
        Markdown + timeline artifacts) that you can share with:

        - Team members who will help design or build the automation.
        - Stakeholders who need to understand what the automation will do.
        - Management who need a concise overview of scope, impact, and effort.
        """
    )

    st.markdown("### Navigation, State, and Downloading/Uploading Your Work")
    st.markdown(
        """
        - Use the **sidebar page selector** to switch between the Use Case and
          Solution Wizard pages.
        - The application keeps shared information so values entered on one page
          remain available on the others during the same session.
        - You can iterate: refine your use case, update the solution design,
          and re‑generate artifacts as your understanding evolves.
        - The application allows you to save your work (uses cases and solution design) 
          as a JSON file that you can load later.
        - If you saved a previous session, you can load it using the **Load
          Session** button at the top of the Solution Wizard page (this includes saved 
          use cases and solution designs).

        """
    )


if __name__ == "__main__":
    main()
    st.markdown("---")
    st.caption(
        "Disclaimer: Results depend entirely on your inputs. Validate data and use professional judgment."
    )

    with st.expander("⚠️ Read full disclaimer", expanded=False):
        st.markdown(
            """
            The calculations, outputs, and recommendations presented by this application are for informational purposes only. 
            Results are entirely dependent on the inputs provided by the user and any assumptions entered. 
            It is the user's responsibility to validate all inputs, review the outputs for accuracy and suitability, and apply appropriate professional judgment before making decisions based on these results.
            
            By using this application, you acknowledge and agree that:
            - You are solely responsible for the data you enter and for any conclusions or decisions you draw from the results.
            - The authors and contributors make no warranties, express or implied, regarding accuracy, completeness, or fitness for a particular purpose.
            - The authors and contributors shall not be liable for any losses or damages arising from use of or reliance on the results.
            """
        )
