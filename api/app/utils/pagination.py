def paginate(collection, page, size):
    if page < 0 or size < 0:
        return {"message": "Error, page and size values have to be no negative integers."}
    begin = (page - 1) * size
    end = begin + size - 1
    collection_size = len(collection)
    if collection_size < begin:
        return {
            "items": [],
            "total": collection_size,
            "page": page,
            "size": size
        }
    if collection_size < end:
        return {
            "items": [collection[i] for i in range(begin, collection_size)],
            "total": collection_size,
            "page": page,
            "size": size
        }

    return {
        "items": [collection[i] for i in range(begin, end)],
        "total": collection_size,
        "page": page,
        "size": size
    }
