import os
import json
import argparse

def list_files(directory):
    files_list = []
    # Walk through directory recursively
    for root, dirs, files in os.walk(directory, topdown=True):
        files.sort(reverse=True)

        temp_file = ""

        for file in files:
            if "flag" in file:
                temp_file = file
            else:
                files_list.append({"logo":"graphics/factions/custom/"+temp_file, "crest":"graphics/factions/custom/"+file})
    return files_list

def write_json(target_path, file):
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    files_data = list_files("./graphics/factions/custom/")

    with open(os.path.join(target_path, file), 'w') as json_file:
        json.dump(
        {
	        "id":"player",
            "flags":files_data
        }
        , json_file, indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory")
    parser.add_argument(
        "-o", "--output",
        default="player.faction",
    )
    args = parser.parse_args()
    
    write_json("./data/world/factions/", args.output)

if __name__ == "__main__":
    main()

# py parser.py ./