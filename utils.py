#!/usr/bin/python3 -tt
# Project: naf_naf_solution_wizard
# Filename: utils.py
# claudiadeluna
# PyCharm

__author__ = "Claudia de Luna (claudia@indigowire.net)"
__version__ = ": 1.0 $"
__date__ = "11/25/25"
__copyright__ = "Copyright (c) 2025 Claudia"
__license__ = "Python"


# from __future__ import annotations

from typing import List, Optional
import streamlit as st


def thick_hr(color: str = "red", thickness: int = 3, margin: str = "1rem 0"):
    """
    Render a visually thicker horizontal line in Streamlit using raw HTML.

    Parameters
    - color: CSS color for the rule (named color or hex).
    - thickness: Pixel height of the line.
    - margin: CSS margin to apply (e.g., "1rem 0").

    Behavior
    - Uses st.markdown with unsafe_allow_html to inject an <hr> replacement.
    """
    st.markdown(
        f"""
        <hr style="
            border: none;
            height: {thickness}px;
            background-color: {color};
            margin: {margin};
        ">
        """,
        unsafe_allow_html=True,
    )


def hr_colors():
    """
    Returns a dictionary of colors for horizontal lines.

    utils.thick_hr(color="#6785a0", thickness=3)
    """
    hr_color_dict = {
        "naf_yellow": "#fffe03",
        "eia_blue": "#92c0e4",
        "eia_dkblue": "#122e43",
    }
    return hr_color_dict



def render_global_sidebar() -> None:
    """Render global sidebar branding used across all pages.

    Includes the EIA logo, external links, and bottom NAF branding bar.
    """

    hr_color_dict = hr_colors()

    with st.sidebar:
        # Top branding: logo and EIA links
        col_logo, col_links = st.columns([1, 2])
        with col_logo:
            st.image("images/EIA Logo FINAL small_Round.png", width="stretch")
        with col_links:
            st.markdown("[🏠 EIA Home](https://eianow.com)")
            st.markdown(
                "[[in] EIA on LinkedIn](https://www.linkedin.com/company/eianow/)"
            )

        thick_hr(
            color=hr_color_dict.get("eia_blue", "#92c0e4"),
            thickness=6,
            margin="0.5rem 0",
        )

        # Bottom NAF branding bar with NAF icon

        _naf_logo_col, _naf_link_col = st.columns([1, 2])
        with _naf_logo_col:
            st.image("images/naf_icon.png", width="stretch")
        with _naf_link_col:
            st.markdown("[🏠 NAF Home](https://networkautomation.forum/)")
            # linkedin.com/company/network-automation-forum/
            st.markdown(
                "[[in] NAF on LinkedIn](https://www.linkedin.com/company/network-automation-forum/)"
            )
        thick_hr(
            color=hr_color_dict.get("naf_yellow", "#fffe03"),
            thickness=6,
            margin="0.75rem 0 0.25rem 0",
        )




def main():
    """
    Module self-check entry point (optional).

    Purpose
    - Provides a basic callable for ad-hoc verification or future CLI hooks.

    Current behavior
    - No-op (pass). Keep in place to allow running this module directly without errors.
    """
    pass


# Standard call to the main() function.
if __name__ == "__main__":
    main()
