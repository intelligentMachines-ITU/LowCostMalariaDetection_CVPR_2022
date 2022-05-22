import sys
import os
import json
import xml.etree.ElementTree as ET



START_BOUNDING_BOX_ID = 1
# names = ['gametocyte','schizont','trophozoite','ring']

PRE_DEFINE_CATEGORIES = {"gametocyte": 1, 'schizont': 2,'trophozoite': 3,'ring': 4}
COUNT = {"gametocyte": 0, 'schizont': 0,'trophozoite': 0,'ring': 0}


def get(root, name):
    vars = root.findall(name)
    return vars


def get_and_check(root, name, length):
    vars = root.findall(name)

    if len(vars) == 0:
        raise NotImplementedError('Can not find %s in %s.'%(name, root.tag))
    if length > 0 and len(vars) != length:
        # print(root.findall('filename')[0].text + " has size issue")
        vars = [vars[0]]

        # raise NotImplementedError('The size of %s is supposed to be %d, but is %d.'%(name, length, len(vars)))
    if length == 1:
        vars = vars[0]
    return vars


def get_filename_as_int(filename):
    try:
        filename = os.path.splitext(filename)[0]
        return int(filename)
    except:
        raise NotImplementedError('Filename %s is supposed to be an integer.'%(filename))
def convert(xml_list, xml_dir, json_file, res):
    m = 0

    list_fp = open(xml_list, 'r')
    json_dict = {"images":[], "type": "instances", "annotations": [],
                 "categories": []}
    categories = PRE_DEFINE_CATEGORIES
    bnd_id = START_BOUNDING_BOX_ID
    image_id = 000000
    ERRORS = []
    for line in list_fp:
        line = line.strip()
        # line = line.replace("_1000x", "_400x") 
        line += '_'+res+'.xml'
        xml_f = os.path.join(xml_dir, line)
        try:

            tree = ET.parse(xml_f)
        except:
            print(line, " couldn't read")
            continue
        root = tree.getroot()
        path = get(root, 'path')

        filename = get_and_check(root, 'filename', 1).text
        filename = filename.replace(" ", "")
        # segfilename = get_and_check(root, 'segfilename', 1).text
#             print filename
#             print segfilename
        # else:
        #     raise NotImplementedError('%d paths found in %s'%(len(path), line))

           
        image_id += 1
        size = get_and_check(root, 'size', 1)
        width = int(get_and_check(size, 'width', 1).text)
        height = int(get_and_check(size, 'height', 1).text)
        image = {'file_name': filename, 'height': height, 'width': width,
                 'id':image_id, 'seg_file_name': filename}
        # json_dict['images'].append(image)

        obj_count = 0
        if(len(get(root, 'object')) <1):
            print(line)
        for obj in get(root, 'object'):
            category = get_and_check(obj, 'name', 1).text.lower()
            # if category == 'schizont':
            #     print(line, len(get(root, 'object')))
                # break
            COUNT[category] += 1
            # continue
            if category not in categories:
                print(category)
                raise
                new_id = len(categories)
                categories[category] = new_id
            category_id = categories[category]
            bndbox = get_and_check(obj, 'bndbox', 1)
            xmin = int(get_and_check(bndbox, 'xmin', 1).text)
            ymin = int(get_and_check(bndbox, 'ymin', 1).text)
            xmax = int(get_and_check(bndbox, 'xmax', 1).text)
            ymax = int(get_and_check(bndbox, 'ymax', 1).text)
            if (xmax <= xmin) or (ymax <= ymin):
                if line not in ERRORS:
                    ERRORS.append(line)
                    # print("Error %s %s"%(line, len(get(root, 'object'))))
                continue

            assert(xmax > xmin)
            assert(ymax > ymin)
            o_width = abs(xmax - xmin)
            o_height = abs(ymax - ymin)
            ann = {'area': o_width*o_height, 'iscrowd': 0, 'image_id':
                   image_id, 'bbox':[xmin, ymin, o_width, o_height],
                   'category_id': category_id, 'id': bnd_id, 'ignore': 0,
                   'segmentation': [1,477,2,478,3,479,4,479,5,480,6,479,7,478,7,477,8,476,9,475]}
            json_dict['annotations'].append(ann)
            bnd_id = bnd_id + 1
            obj_count+= 1
        if obj_count > 0:
            json_dict['images'].append(image)
        else:
            image_id -= 1
    print(COUNT)
    # print(ERRORS)
    # raise    
    # cat = [{"supercategory": "none", "id": 1, "name": "CLASS"}]
    cat = [{"supercategory": "none", "id": 1, "name": "gametocyte"},
                {"supercategory": "none", "id": 2, "name": "schizont"},
                {"supercategory": "none", "id": 3, "name": "trophozoite"},
                {"supercategory": "none", "id": 4, "name": "ring"},
    ]
    # names = ['gametocyte','schizont','trophozoite','ring']

    for cid in range(len(cat)):
#         cat = {'supercategory': 'none', 'id': cid, 'name': cate}
        json_dict['categories'].append(cat[cid])
   
#     for cate, cid in categories.items():
#         cat = {'supercategory': 'none', 'id': cid, 'name': cate}
#         json_dict['categories'].append(cat)
    json_fp = open(json_file, 'w')
    json_str = json.dumps(json_dict)
    json_fp.write(json_str)
    json_fp.close()
    list_fp.close()



if __name__ == '__main__':
    import glob
    path_model_prediction = 'Annotations/LCM/train/1000x/'  # Enter the path of the annotations folder
    textpath = path_model_prediction
    xmls_files = path_model_prediction
    draw_xmls_files = os.listdir(xmls_files)
    # draw_xmls_files = [os.path.basename(x) for x in glob.glob(xmls_files + '/*.xml')]

    images_name = 'Annotations/LCM/train/train.txt'
    m = 0
   
    textpath = path_model_prediction

    path_to_save = 'Annotations/LCM/train/train_1000x.json'

    # print(path_model_prediction.split('/'))
    convert(images_name, xmls_files, path_to_save, path_model_prediction.split('/')[3])
