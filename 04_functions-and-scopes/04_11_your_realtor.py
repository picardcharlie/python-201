# Write a function that prints out nicely formatted information about a
# real estate listing. The information can vary for every listing, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def listing(address, *args):
    """
    Takes in information for a reality listing and formats it.

    Accepts the address as address.
    Then a string of discriptions of the home.

    Returns a string as the listing.
    """

    listing = f"Home for sale at {address} by PGH Reality \nThe home includes "

    for feature in args:
        listing += feature + " "

    listing += "\nStop by PGH on 35th to talk to a realitor!"

    return listing
listlist = ["2 bedrooms", "3 bathrooms", "14 car garage"]
print(listing("123 Main", *listlist))
