from os import walk
# iterate all .md files recursively:
mds = [f for _, _, fs in walk(".") for f in fs if f.endswith(".md") and f != "ALL.md"]

open("ALL.md", "w").write("\n".join([f"![[{f}]]" for f in mds]))