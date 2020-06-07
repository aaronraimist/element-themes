#!/usr/bin/python
# This takes all the themes and puts it in one file
import json
import os


OUTPUT = "./output.json"
BLACKLIST = [
	".git",
	"images"
]


if __name__ == '__main__':
	result = []
	json_paths = []


	# 1. Let's recursively look for all the JSON files

	# root_dirs = ["Discord", "Geeko Dark", etc...]
	root = os.listdir("./")
	for root_dir in root:
		is_dir = os.path.isdir(f"./{root_dir}")
		if root_dir in BLACKLIST or not is_dir:
			continue

		
		# if root_dir is "Discord" then deep_dirs is
		# deep_dirs = ["Discord-Dark"]
		# ./Discord
		#  └── Discord-Dark
		#      ├── Discord-Dark-Theme.json
		#      └── Discord-Dark-Theme.png

		deep_dirs = os.listdir(f"./{root_dir}")
		for deep in deep_dirs:
			current_path = f"./{root_dir}/{deep}"

			is_dir = os.path.isdir(current_path)
			if is_dir:
				files = os.listdir(current_path)

				for file in files:
					current_path = f"./{root_dir}/{deep}/{file}"
					if file.lower().endswith(".json"):
						json_paths.append(current_path)
						print(f"Added {file}")
						
			elif deep.lower().endswith(".json"):
				json_paths.append(current_path)
				print(f"Added {file}")

	# 2. Now let's parse all the JSON files
	for json_path in json_paths:
		with open(json_path, 'r') as file:
			parsed = json.load(file)
			result.append(parsed)


	# 3. Finally output the themes as a JSON array
	with open(OUTPUT, 'w') as output:
		output.write(
			json.dumps(result, indent=2)
		)
		output.close()
		print(f"Output: {OUTPUT}")
