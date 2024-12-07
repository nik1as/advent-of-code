passports = ""
while True:
    try:
        passports += input() + "\n"
    except EOFError:
        break

passports = passports.split("\n\n")

fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
valid = 0
for passport in passports:
    for field in fields:
        if field + ":" not in passport:
            break
    else:
        valid += 1

print(valid)
