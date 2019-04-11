import io
from tqdm import tqdm
import time
import os
from PIL import Image
from pytesseract import image_to_string
import natsort as ns

directory = "/home/rony/contract_sol/PDF/"
image_dir = "/home/rony/contract_sol/images"

for filename in tqdm(os.listdir(directory)):
        content = ""
        if filename.endswith(".pdf"): 
                infile = "".join(filename.split(' '))

                #renaming files to remove spaces in filename
                os.rename(os.path.join(directory,filename), os.path.join(directory, infile))
                

                infolder = infile.split('.')[0]
                create_dir = 'mkdir -p {}'.format(os.path.join(image_dir,infolder))
                os.system(create_dir)

                outfile = os.path.join(os.path.join(image_dir,infolder),str(infile).split('.')[0]+".jpeg")

                command = 'convert -density 300 {} -quality 90 +profile "icc" {}'.format(os.path.join(directory,infile), outfile)
                os.system(command)

        with open("t.text",'w') as f:
                for image in ns.natsorted(os.listdir(os.path.join(image_dir,infolder))):
                        final_dir = os.path.join(image_dir,infolder)
                        content = image_to_string(Image.open(os.path.join(final_dir,image)), lang='eng')
                        # print(type(image_to_string(Image.open(os.path.join(final_dir,image)), lang='eng')))
                        f.write(content)
        f.close()
        break  