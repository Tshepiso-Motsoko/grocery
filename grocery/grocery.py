from collections import defaultdict

def main():
    grocery_list = defaultdict(int)

    try:
        while True:
            try:
                # Prompt the user for an item
                item = input()

                # Convert the item to uppercase for case insensitivity
                item = item.upper()

                if item:
                    # Add the item to the grocery list
                    grocery_list[item] += 1

            except EOFError:
                break

    except KeyboardInterrupt:
        pass

    # Sort the grocery list items alphabetically
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])

    # Print the grocery list with the count and item in uppercase
    for item, count in sorted_items:
        print(f"{count} {item}")

if __name__ == "__main__":
    main()
