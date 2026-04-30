Core Concept

A Checkbutton is a box that a user can toggle on or off. Unlike Radiobuttons, which only allow one selection in a group, Checkbuttons allow the user to select multiple options at the same time.
Implementation Summaries

    Select All (select_all.py)
    This creates a master checkbox that controls a group of other checkboxes. When you check the master box, all other boxes are checked automatically. This is useful for "Select All" features in email or file managers.

    Validation (validation.py)
    This connects a checkbox to a button. The button remains disabled and unclickable until the user checks the box. This is standard for "I agree to the terms" forms.

    Grid Layout (grid_layout.py)
    Instead of a simple list, this uses a coordinate system to place checkboxes in rows and columns. This is the best way to organize a large number of options while saving screen space.

    Tooltip Style (tooltip_style.py)
    This provides instant feedback. When a user checks or hovers over a box, a label or message appears to explain what that specific feature does or confirms that the change was made.

    Pre-Selected Defaults (pre_selected.py)
    This shows how to have a checkbox already checked when the application opens. It is used for settings that you want to be "on" by default for the user.

    Tri-State Logic (tri_state.py)
    This implements a third visual state (usually a dash) that indicates a "partial" selection. It is commonly used in file explorers when some, but not all, files in a folder are selected.

    Styled Customization (styled.py)
    This implementation focuses on looks. It shows how to change the color of the checkmark, the background, and the font to make the checkbox match a specific app theme.

    Scrollable List (scrollable_list.py)
    When you have too many checkboxes to fit on one screen, this method puts them inside a frame that can be scrolled up and down.

    Data Logging (data_logging.py)
    This keeps a record of every click. Every time a box is toggled, the app records the action and the exact time it happened. This is used for tracking user activity or debugging.

