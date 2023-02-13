addresses = ["www.google.com", "www.youtube.com", "www.facebook.com"]
fixed_addresses = ["http://" + address if address.startswith("www.") and address.endswith(".com")
                   else "http://" + address + ".com" if address.startswith("www.")
                   else address for address in addresses]
print("Исправленные адреса: ", fixed_addresses)