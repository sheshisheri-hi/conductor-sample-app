"""
paginate() utility for in-memory list pagination.

Provides pagination metadata and sliced items for the requested page.

Example usage:
    items = list(range(1, 101))
    result = paginate(items, page=2, page_size=10)
    print(result)
    # Output:
    # {
    #   'page': 2,
    #   'page_size': 10,
    #   'total_items': 100,
    #   'total_pages': 10,
    #   'items': [11, 12, ..., 20]
    # }
"""

def paginate(items, page=1, page_size=10):
    """
    Paginate an in-memory list.

    Args:
        items (list): The list of items to paginate.
        page (int): The page number (1-based).
        page_size (int): Number of items per page.

    Returns:
        dict: Pagination metadata and items for the page.
            {
                'page': int,
                'page_size': int,
                'total_items': int,
                'total_pages': int,
                'items': list
            }
    """
    if page < 1:
        raise ValueError("page must be >= 1")
    if page_size < 1:
        raise ValueError("page_size must be >= 1")
    total_items = len(items)
    total_pages = (total_items + page_size - 1) // page_size if page_size else 0
    start = (page - 1) * page_size
    end = start + page_size
    paged_items = items[start:end]
    return {
        'page': page,
        'page_size': page_size,
        'total_items': total_items,
        'total_pages': total_pages,
        'items': paged_items
    }
