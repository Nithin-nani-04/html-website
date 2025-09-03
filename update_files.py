#!/usr/bin/env python3
"""
Script to update all HTML files with CSS styling and improved structure
"""

import os
import re

# List of files to update (excluding index.html and media.html which are already updated)
files_to_update = [
    'head.html',
    'text.html', 
    'lists.html',
    'semantic.html',
    'tables.html',
    'forms.html',
    'extras.html'
]

# CSS and favicon links to add
css_links = '''    <link rel="stylesheet" href="styles.css">
    <link rel="icon" type="image/x-icon" href="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdCb3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHJlY3Qgd2lkdGg9IjMyIiBoZWlnaHQ9IjMyIiByeD0iNCIgZmlsbD0iIzQyODVGNCIvPgo8dGV4dCB4PSIxNiIgeT0iMjIiIGZvbnQtZmFtaWx5PSJBcmlhbCwgc2Fucy1zZXJpZiIgZm9udC1zaXplPSIxOCIgZm9udC13ZWlnaHQ9ImJvbGQiIGZpbGw9IndoaXRlIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj5IPC90ZXh0Pgo8L3N2Zz4K">'''

def update_html_file(filename):
    """Update a single HTML file with CSS and structure improvements"""
    
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping...")
        return
    
    print(f"Updating {filename}...")
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add CSS and favicon links before </head>
    if '<link rel="stylesheet"' not in content:
        content = content.replace('</head>', f'{css_links}\n</head>')
    
    # Update header to use class
    content = re.sub(r'<header>', '<header class="main-header">', content)
    
    # Update nav to use class and add icons link
    content = re.sub(r'<nav>', '<nav class="main-nav">', content)
    
    # Add icons link to navigation if not present
    if 'icons.html' not in content:
        # Find the forms.html link and add icons after it
        content = re.sub(
            r'(<li><a href="forms\.html">📝 Forms & Inputs</a></li>)',
            r'\1\n            <li><a href="icons.html">🎨 Icons & Favicons</a></li>',
            content
        )
    
    # Update main structure
    content = re.sub(r'<main>', '<div class="main-content">\n        <main class="content-area">', content)
    
    # Update sections to use classes
    content = re.sub(r'<section>', '<section class="content-section">', content)
    content = re.sub(r'<article>', '<article class="element-card">', content)
    
    # Update aside to use class
    content = re.sub(r'<aside>', '<aside class="sidebar">', content)
    
    # Update footer to use class
    content = re.sub(r'<footer>', '<footer class="main-footer">', content)
    
    # Add closing div for main-content before aside
    if '<aside class="sidebar">' in content and '</main>' in content:
        content = re.sub(
            r'(</main>)\s*(<aside class="sidebar">)',
            r'\1\n\n      \2',
            content
        )
        content = re.sub(
            r'(</aside>)\s*(<footer class="main-footer">)',
            r'\1\n    </div>\n\n    \2',
            content
        )
    
    # Add syntax, output, notes blocks structure
    # This is a basic pattern - might need manual adjustment for complex cases
    content = re.sub(
        r'<h4>Syntax:</h4>\s*<pre><code>',
        '<div class="syntax-block">\n                <h4>Syntax:</h4>\n                <pre><code>',
        content
    )
    
    content = re.sub(
        r'</code></pre>\s*<h4>Output:</h4>',
        '</code></pre>\n                </div>\n                <div class="output-block">\n                <h4>Output:</h4>',
        content
    )
    
    content = re.sub(
        r'<h4>Notes:</h4>',
        '</div>\n                <div class="notes-block">\n                <h4>Notes:</h4>',
        content
    )
    
    # Close the last notes block before next article or end of article
    content = re.sub(
        r'(</p>)\s*(</article>)',
        r'\1\n                </div>\n            \2',
        content
    )
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated {filename}")

def main():
    """Main function to update all files"""
    print("Starting HTML files update...")
    
    for filename in files_to_update:
        update_html_file(filename)
    
    print("All files updated successfully!")
    print("\nNote: Some manual adjustments might be needed for complex layouts.")
    print("Please review the files and make any necessary corrections.")

if __name__ == "__main__":
    main()