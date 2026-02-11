#!/usr/bin/env python3
def main():
    original_list = [2, 8, 9, 48, 8, 22, -12, 2]
    print(original_list)
    transformed_set = {x + 2 for x in original_list if x + 2 > 5}
    print(transformed_set)

if __name__ == "__main__":
    main()