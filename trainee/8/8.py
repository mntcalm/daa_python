lines = []
cntr=0
with open("file.txt", "r") as f:
  for line in f:
    line = line.strip()
    if "catch me" in line:
      lines.append(line)
      cntr=cntr+1
print(lines)
print("количество попавшихся строк=", cntr)
