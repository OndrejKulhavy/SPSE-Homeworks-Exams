for i in range(1, 13):
    filename = f"exercise_{i}.py"
    content = f'# {filename}\n\n# Your code goes here\n\nprint("Hello from {filename}")'

    with open(filename, 'w') as file:
        file.write(content)

print("Files created successfully!")
