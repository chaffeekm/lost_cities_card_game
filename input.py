import tkinter as tk

def custom_exact_input(title, prompt, x, y, root):
    # Create dialog window
    dialog = tk.Toplevel(root)
    dialog.title(title)
    dialog.geometry(f"+{x}+{y}")

    # Keep dialog on top and focused
    dialog.lift()
    dialog.attributes("-topmost", True)
    dialog.focus_force()

    # Store result
    result = {"value": None}

    # UI Elements
    tk.Label(dialog, text=prompt, padx=10, pady=10).pack()

    entry = tk.Entry(dialog, width=30)
    entry.pack(padx=10, pady=5)
    entry.focus()

    def submit():
        result["value"] = entry.get()
        dialog.destroy()

    def on_enter(event):
        submit()

    tk.Button(dialog, text="OK", command=submit).pack(pady=10)

    # Bind Enter key
    entry.bind("<Return>", on_enter)

    # Wait until window is closed
    dialog.grab_set()
    root.wait_window(dialog)

    return result["value"]
