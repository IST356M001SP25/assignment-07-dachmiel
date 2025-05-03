if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from menuitem import MenuItem
else:
    from code.menuitem import MenuItem


def clean_price(price:str) -> float:
    # remove $ from price
    price = price.replace("$", "")

    # removes , from price
    price = price.replace(",", "")

    # convert price to a float
    price = float(price)

    return price

def clean_scraped_text(scraped_text: str) -> list[str]:
    # split scraped data into new lines
    text = scraped_text.split('\n')

    cleaned_items = []

    # loop through each item that was scraped and filters out the designated lines
    for item in text:
        if item in ['GS', 'V', 'S', 'P']:
            continue
        if item.startswith('NEW'):
            continue
        if len(item.strip()) == 0:
            continue

        # adds lines that don't contain the designated items to the list
        cleaned_items.append(item)
    
    return cleaned_items

def extract_menu_item(title:str, scraped_text: str) -> MenuItem:
    cleaned_text = clean_scraped_text(scraped_text)

    # create item with a default value for MenuItem
    item = MenuItem(category= title, name = "", price = 0.0, description= "")

    # adds the first element of cleaned text as the name of the item
    item.name = cleaned_text[0]

    # adds the second element of cleaned text as the price of the item
    item.price = clean_price(cleaned_text[1])

    # check to see if item has a description
    if len(cleaned_text) > 2:
        item.description = cleaned_text[2]
    else:
        item.description = "No Description Available."

    return item



if __name__=='__main__':
    pass
