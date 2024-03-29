import os
import ast
from dotenv import load_dotenv


class env_data:
    def __init__(self):
        env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'env.configs')
        load_dotenv(env_path)
        self.configs = os.environ

    def get_config(self):
        return self.configs
    #get segment type
    def get_segment_type(self):
        return self.configs["SEGMENT_TYPE"]
    
    #get image path
    def get_image_path(self):
        return self.configs["IMAGE_PATH"]
    #get output path
    def get_output_path(self):
        return self.configs["OUTPUT_PATH"]
    #get output extension
    def get_output_extension(self):
        return self.configs["OUTPUT_EXTENSION_TYPE"]
    def get_min_polygon_area(self):
        return int(self.configs["MIN_POLYGON_AREA"])




    def get_model(self):
        return self.configs["MODEL"]
    def get_model_type(self):
        return self.configs["MODEL_TYPE"]
    def get_checkpoint(self):
        return self.configs["MODEL_CHECKPOINT"]
    def get_batch(self):
        return ast.literal_eval(self.configs["BATCH"])


    def get_text_prompt(self):
        return self.configs["TEXT_PROMPT"]
    # get box_threshold
    def get_box_threshold(self):
        return float(self.configs["BOX_THRESHOLD"])
    # get text_threshold
    def get_text_threshold(self):
        return float(self.configs["TEXT_THRESHOLD"])
    


    def get_imageresize(self):
        return int(self.configs["IMAGE_RESIZE"])
    #get quality
    def get_quality(self):
        return int(self.configs["QUALITY"])
    #get brightscale
    def get_brightscale(self):
        try:
            return float(self.configs["BRIGHT"])
        except:
            return ast.literal_eval(self.configs["BRIGHT"])

    #get blur_image
    def get_blur_image(self):
        return ast.literal_eval(self.configs["BLUR_IMAGE"])
    #get hsv_image
    def get_hsv_image(self):
        return ast.literal_eval(self.configs["HSV_IMAGE"])
    #get gray_image
    def get_gray_image(self):
        return ast.literal_eval(self.configs["GRAY_IMAGE"])
    




    def get_samkwargs(self):
        if ast.literal_eval(self.configs["SAM_KWARGS"]) == True :
            kwargs = {
                'points_per_side' : int(self.configs["POINTS_PER_SIDE"]),
                'points_per_batch': int(self.configs["POINTS_PER_BATCH"]),
                'pred_iou_thresh': float(self.configs["PRED_IOU_THRESH"]),
                'stability_score_thresh': float(self.configs["STABILITY_SCORE_THRESH"]),
                'stability_score_offset': float(self.configs["STABILITY_SCORE_OFFSET"]),
                'box_nms_thresh': float(self.configs["BOX_NMS_THRESH"]),
                'crop_n_layers': int(self.configs["CROP_N_LAYERS"]),
                'crop_nms_thresh': float(self.configs["CROP_NMS_THRESH"]),
                'crop_overlap_ratio': float(self.configs["CROP_OVERLAP_RATIO"]),
                'crop_n_points_downscale_factor': int(self.configs["CROP_N_POINTS_DOWNSCALE_FACTOR"]),
                'min_mask_region_area': int(self.configs["MIN_MASK_REGION_AREA"]),
                'output_mode': self.configs["OUTPUT_MODE"]
                        }
            return kwargs
        else:
            return None
        


# def data():
#     env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'env.configs')
#     load_dotenv(env_path)
#     configs = os.environ
#     return configs

# def get_model():
#     configs = env_data()
#     return configs["MODEL"]

# def get_model_type():
#     configs = env_data()
#     return configs["MODEL_TYPE"]

# def get_checkpoint():
#     configs = env_data()
#     return configs["MODEL_CHECKPOINT"]

# def get_batch():
#     configs = env_data()
#     return ast.literal_eval(configs["BATCH"])

# def get_imageresize():
#     configs = env_data()
#     return int(configs["IMAGE_RESIZE"])

# def get_output_extension():
#     configs = env_data()
#     return configs["OUTPUT_EXTENSION_TYPE"]



# def get_min_polygon_area():
#     configs = env_data()
#     return int(configs["MIN_POLYGON_AREA"])

# def get_samkwargs():
#     configs = env_data()
#     if ast.literal_eval(configs["SAM_KWARGS"]) == True :
#         kwargs = {
#             'points_per_side' : int(configs["POINTS_PER_SIDE"]),
#             'points_per_batch': int(os.getenv("POINTS_PER_BATCH")),
#             'pred_iou_thresh': float(os.getenv("PRED_IOU_THRESH")),
#             'stability_score_thresh': float(os.getenv("STABILITY_SCORE_THRESH")),
#             'stability_score_offset': float(os.getenv("STABILITY_SCORE_OFFSET")),
#             'box_nms_thresh': float(os.getenv("BOX_NMS_THRESH")),
#             'crop_n_layers': int(os.getenv("CROP_N_LAYERS")),
#             'crop_nms_thresh': float(os.getenv("CROP_NMS_THRESH")),
#             'crop_overlap_ratio': float(os.getenv("CROP_OVERLAP_RATIO")),
#             'crop_n_points_downscale_factor': int(os.getenv("CROP_N_POINTS_DOWNSCALE_FACTOR")),
#             'min_mask_region_area': int(os.getenv("MIN_MASK_REGION_AREA")),
#             'output_mode': os.getenv("OUTPUT_MODE")
#                     }
#         return kwargs
#     else:
#         return None
# if __name__ == "__main__":
#     print(get_checkpoint())