#Homework - Package Loading Program


count_of_packages = 1
packages_sent = 0
total_weight_sent = 0
min_items = 0
max_items = 10
max_item_weight = 10
min_item_weight = 1
max_package_weight = 20
current_package_weight = 0
unused_capacity_per_package = []
used_capacity_per_package = []


while True:
    try:
        item_count = int(input(f"How many items do you want to send? The maximum possible amount is {max_items} items: "))
        break
    except ValueError:
        print("Please, enter a number.")

if item_count < min_items:
    print("O items left. Terminating the program.")

elif item_count > max_items:
    print(f"Maximum number of items ({max_items}) exceeded. Terminating the program.")

while min_items < item_count <= max_items:
        while True:
            try:
                item_weight = int(input(f"Which is the weight of the current item (in kg)? The weight must be between {min_item_weight}kg and {max_item_weight}kg: "))
                break
            except ValueError:
                print("Please, enter a number.")

        if item_weight <= 0:
            print("Terminating the program.")
            break

        elif min_item_weight < item_weight > max_item_weight:
            print(f"Incorrect weight of the item. The weight must be between {min_item_weight}kg and {max_item_weight}kg.")
            continue

        elif current_package_weight + item_weight < max_package_weight:
            print(f"PACKAGE NUMBER {count_of_packages}")
            current_package_weight += item_weight
            item_count -= 1
            print(f"Current package weight: {current_package_weight}kg \n"
                  f"Items left to include: {item_count}")

        elif current_package_weight + item_weight == max_package_weight:
            print(f"PACKAGE NUMBER {count_of_packages}")
            current_package_weight += item_weight
            packages_sent += 1
            unused_capacity_per_package.append(max_package_weight - current_package_weight)
            used_capacity_per_package.append(current_package_weight)
            count_of_packages += 1
            item_count -= 1
            print(f"Current package weight: {current_package_weight}kg \n"
                  f"The PACKAGE NUMBER {count_of_packages - 1} was sent since it reached the maximum kg amount ({max_package_weight}kg) \n"
                  f"Packages sent until now: {packages_sent} \n"
                  f"Items left to include: {item_count}")
            current_package_weight = 0
            continue

        elif current_package_weight + item_weight > max_package_weight:
            unused_capacity_per_package.append(max_package_weight - current_package_weight)
            used_capacity_per_package.append(current_package_weight)
            current_package_weight = item_weight
            count_of_packages += 1
            print(f"The last item was included in PACKAGE NUMBER {count_of_packages} and the PACKAGE NUMBER {count_of_packages - 1} was sent.")
            print(f"PACKAGE NUMBER {count_of_packages}")
            packages_sent += 1
            item_count -= 1
            print(f"Current package weight: {current_package_weight}kg \n"
                  f"Packages sent until now: {packages_sent} \n"
                  f"Items left to include: {item_count}")

        if item_count == 0:
            packages_sent += 1
            unused_capacity_per_package.append(max_package_weight - current_package_weight)
            used_capacity_per_package.append(current_package_weight)
            print(f"The items ended and the PACKAGE NUMBER {count_of_packages} was sent")
            break

package_max_unused_capacity = unused_capacity_per_package.index(max(unused_capacity_per_package)) + 1

print()

print("The total number of packages sent is {} \n"
      "The total weight of packages sent is {}kg \n"
      "The total unused capacity has been {}kg"
      .format(packages_sent, sum(used_capacity_per_package), sum(unused_capacity_per_package)))

if max(unused_capacity_per_package) != 0:
    print("The package that had the most unused capacity was the PACKAGE NUMBER {} with {}kg of unused capacity"
      .format( package_max_unused_capacity, max(unused_capacity_per_package)))
else: print("")