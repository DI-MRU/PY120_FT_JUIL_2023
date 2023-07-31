class Pagination:
    def __init__(self, items=None, pageSize=10):
        # Initialize the Pagination class with a list of items and the page size (number of items per page).
        # If no items are provided, the default is an empty list.
        self.items = items or []
        self.page_size = int(pageSize)
        # Calculate the total number of pages required to display all items with the given page size.
        # Ensure there is at least one page, even if there are no items.
        self.total_pages = max(1, (len(self.items) + self.page_size - 1) // self.page_size)
        # Set the current page to 1 by default. There cannot be a page 0.
        self.current_page = 1

    def getVisibleItems(self):
        # Return a list of items visible on the current page based on the page size and current page number.
        start_idx = (self.current_page - 1) * self.page_size
        end_idx = start_idx + self.page_size
        return self.items[start_idx:end_idx]

    def prevPage(self):
        # Move to the previous page if possible (current page should not go below 1).
        self.current_page = max(1, self.current_page - 1)
        return self

    def nextPage(self):
        # Move to the next page if possible (current page should not go above the total number of pages).
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def firstPage(self):
        # Move to the first page (page 1).
        self.current_page = 1
        return self

    def lastPage(self):
        # Move to the last page (the page with the highest number).
        self.current_page = self.total_pages
        return self

    def goToPage(self, pageNum):
        # Move to the specified page number, ensuring it is within the valid range (1 to total_pages).
        # If the page number provided is outside the valid range, go to the closest available page.
        # If a negative or zero page number is provided, set the current page to 1.
        self.current_page = max(1, min(self.total_pages, int(pageNum)))
        return self

# Example usage:
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # Output: ["a", "b", "c", "d"]

p.nextPage()
print(p.getVisibleItems())  # Output: ["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())  # Output: ["y", "z"]

p.goToPage(10)  # If the page is outside the total pages, it goes to the closest page available
print(p.getVisibleItems())  # Output: ["y", "z"] (because there are only 5 total pages)
