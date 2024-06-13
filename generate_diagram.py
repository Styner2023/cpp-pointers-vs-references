"""
This module generates a diagram comparing pointers and references in C++.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def create_diagram():
    """
    Creates a diagram illustrating the differences between pointers and references in C++.
    """
    _, ax = plt.subplots(figsize=(10, 8))

    # Pointers
    ax.add_patch(patches.Rectangle((0.1, 0.7), 0.2, 0.1,
                 edgecolor='black', facecolor='lightblue'))
    ax.text(0.15, 0.75, 'int* ptr', fontsize=12,
            verticalalignment='center', horizontalalignment='center')
    ax.text(0.15, 0.72, '(Pointer)', fontsize=12,
            verticalalignment='center', horizontalalignment='center')
    ax.annotate('', xy=(0.2, 0.7), xytext=(0.2, 0.6),
                arrowprops={'arrowstyle': '->'})
    ax.add_patch(patches.Rectangle((0.1, 0.5), 0.2, 0.1,
                 edgecolor='black', facecolor='lightgreen'))
    ax.text(0.2, 0.55, 'value', fontsize=12,
            verticalalignment='center', horizontalalignment='center')

    # References
    ax.add_patch(patches.Rectangle((0.6, 0.7), 0.2, 0.1,
                 edgecolor='black', facecolor='lightblue'))
    ax.text(0.7, 0.75, 'int& ref', fontsize=12,
            verticalalignment='center', horizontalalignment='center')
    ax.text(0.7, 0.72, '(Reference)', fontsize=12,
            verticalalignment='center', horizontalalignment='center')
    ax.annotate('', xy=(0.7, 0.7), xytext=(0.7, 0.6),
                arrowprops={'arrowstyle': '-'})
    ax.add_patch(patches.Rectangle((0.6, 0.5), 0.2, 0.1,
                 edgecolor='black', facecolor='lightgreen'))
    ax.text(0.7, 0.55, 'value', fontsize=12,
            verticalalignment='center', horizontalalignment='center')

    # Comparison Table
    table_data = [
        ["Feature", "Pointer", "Reference"],
        ["Declaration", "`int* ptr = &variable;`", "`int& ref = variable;`"],
        ["Initialization", "Can be uninitialized", "Must be initialized"],
        ["Reassignment", "Can point to different variables", "Cannot be reassigned"],
        ["Nullability", "Can be `nullptr`", "Cannot be null"],
        ["Dereferencing", "Requires `*` to access value",
            "Automatically dereferenced"],
        ["Memory Address", "Holds the address of a variable", "Acts as an alias"]
    ]

    col_labels = table_data[0]
    table_vals = table_data[1:]

    table = plt.table(cellText=table_vals, colLabels=col_labels,
                      cellLoc='center', loc='bottom', bbox=[0, -1, 1, 0.5])
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig("diagram.png")


create_diagram()
