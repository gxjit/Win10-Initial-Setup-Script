lines = ""

with open("DefaultTweaked.preset", "r") as f:
    for line in f:
        if line.startswith("### "):
            lines += f"\n\n\n{line}"
        elif not line.startswith("#"):
            lines += f"\n\n{line.split('#')[0].strip()}"

with open("Custom.preset", "w") as f:
    f.write("\n#### \nCustom Preset for Win 10 Initial Setup Script\n#### \n")
    f.write(lines)
