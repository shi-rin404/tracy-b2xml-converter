from utils import parse_handler as ph
from utils import covert_handler as ch
from utils import io_handler as io
from utils.utils import formatFilePath

def main():
    open_file_path = io.openFileDialog()
    file_extension = open_file_path.rsplit(".", 1)[1]
    save_file_path = io.saveFileDialog(file_extension)
    file_type = ph.typeFile(open_file_path)

    if file_type == 'Binary':
        io.ExportXML(*ph.parseCustomBinFormat(open_file_path), formatFilePath(save_file_path, file_extension))
    elif file_type == 'XML':
        io.ExportGim(formatFilePath(save_file_path, file_extension), ch.xml_to_custom_bin(ch.xml_to_bfs_list(io.ImportXML(open_file_path))))

if __name__ == "__main__":
    main()