import os
import shutil
import time


# # Remove these if exists
# if os.path.exists("site"):
#     shutil.rmtree("site")

# if os.path.exists("temp"):
#     shutil.rmtree("temp")


# Step #1: Build the mkdocs site
os.system("mkdocs build")


# Step #2: Add `temp`` folder
os.mkdir("temp")


# Step #3: Clone the MicroPython editor into `temp`
os.system("git clone https://github.com/TinyCircuits/TinyCircuits-MicroPython-Editor.git temp/editor")


# Step #4: Install everything to build the editor
os.system("(cd temp/editor/app && npm i)")


# Step #5: Build the editor
os.system("(cd temp/editor/app && npm run build)")


# Step #6: Copy the built editor assets into `site/code`
shutil.copytree("temp/editor/pb_public", "site/code")


# Step #7: Move `site/code/assets` to `site/assets`
shutil.copytree("site/code/assets", "site/assets", dirs_exist_ok=True)
shutil.rmtree("site/code/assets")


# Step #8: Rename .wasm file
files = os.listdir("site/assets")
for file in files:
    if "micropython" in file and ".wasm" in file:
        shutil.move("site/assets/" + file, "site/assets/micropython.wasm")


# Step #8: Copy `site/code/code` to `site/code`
shutil.copytree("site/code/code", "site/code", dirs_exist_ok=True)
shutil.rmtree("site/code/code")


# Step 9: Copy `temp/editor/app/src` to `site/src` for worker script (only the .js files)
def ignore_files(dir, files):
    return [f for f in files if not f.endswith('.js')]

shutil.copytree("temp/editor/app/src", "site/src", ignore=ignore_files)


# Step #8: Move anything that is not a directory, .html, or .svg from site/code to site (files need to be at root level)
entries = os.listdir("site/code")
for entry in entries:
    if (".svg" not in entry) and (".html" not in entry) and os.path.isfile("site/code/" + entry):
        shutil.move("site/code/" + entry, "site/" + entry)


# Step #9: Clone the engine
os.system("git clone https://github.com/TinyCircuits/TinyCircuits-Tiny-Game-Engine.git temp/engine")


# Step #10: Build the engine docs
os.system("(cd temp/engine/doc && python generate.py)")


# Step #11: Copy the docs to the site assets
shutil.copytree("temp/engine/doc/build", "site/doc/build")
shutil.copyfile("temp/engine/doc/landing.html", "site/doc/landing.html")


# Step #12: Copy assets for simulator to website `assets/simulator` folder
shutil.copytree("temp/engine/filesystem/system", "site/assets/simulator/system")
shutil.copyfile("temp/engine/filesystem/main.py", "site/assets/simulator/main.py")