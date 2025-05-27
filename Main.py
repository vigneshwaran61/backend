import Extraction as ext
import Hider as hd
import hash as ha

# ha.generate_file_hash(ha.file_path)
# hash_val= ha.file_hash
# print(hash_val)
# hd.hide_data(ha.file_path,ha.file_hash,"out.png")
imgname="out.png"
extdata=ext.extract_hidden_data(imgname)
print(extdata)
