for index, value in enumerate(range(1, 5)):
    print(f"index: {index}, value: {value}")
    if index == 3:
        break

for index, value in enumerate(range(1, 5)):
    if index == 3:
        continue
    print(f'Printed==>> {index}')
