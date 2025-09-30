import os
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
from . import covert_handler as ch

def ImportXML(file_path:os.PathLike):
    # Single Root Support
    tree = ET.parse(file_path)
    
    return tree.getroot()

def ExportXML(element_tags:list, attribute_map:list, file_path:os.PathLike) -> None:
    roots = ch.tagWrapper(element_tags, attribute_map)

    if os.path.exists(file_path):
        os.remove(file_path)
     
    with open(file_path, "a") as f:
        for root in roots:
            ET.indent(root, space="    ")
            f.write(f"{ET.tostring(root, encoding="unicode")}\n")

def ExportGim(file_path:os.PathLike, gim_data:bytearray) -> None:
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "wb") as f:
        f.write(gim_data)

def openFileDialog() -> os.PathLike:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select NeoX Asset",
        filetypes=[("NeoX Asset", "*.gim *.mtg *.mtl"), ("All Files", "*.*")])

    return file_path

def saveFileDialog(file_extension:str) -> os.PathLike:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(
        title="Export Converted File",
        filetypes=[("NeoX Asset", f"*.{file_extension}"), ("All Files", "*.*")])

    return file_path