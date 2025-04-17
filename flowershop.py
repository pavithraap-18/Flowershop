def min_cost_to_buy_all_flowers(P):

    # Step 1: Sort the flower types so we can process them in order
    P.sort()

    # Initialize variables
    n = len(P)       # Total number of flowers
    count = 0        # Counter for how many flowers Oasis needs to pay for
    i = 0            # Index to track current position in the list

    # Step 2: Traverse the list of sorted flower types
    while i < n:
        # Oasis chooses to buy the current flower type
        buy_type = P[i]
        count += 1   # This purchase costs 1 unit

        # Step 3: Skip all flower types that are covered in the range [buy_type, buy_type + 4]
        # Since those are obtained for free with this purchase
        while i < n and P[i] <= buy_type + 4:
            i += 1

    # Step 4: Return the total amount paid
    return count

# Example usage:
if __name__ == "__main__":
    # Sample flower types
    P = [4, 1, 7, 2, 3]
    # Output the minimum cost
    print("Minimum cost to buy all flowers:", min_cost_to_buy_all_flowers(P))
