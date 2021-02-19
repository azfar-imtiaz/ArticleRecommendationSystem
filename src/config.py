from os.path import join

HOME_DIR_PATH = "/home/azfar/PythonProjects/ArticleRecommendationSystem"

DATA_PATH = join(HOME_DIR_PATH, "data/archive/")
BOOK_FILES_PATTERN = "book*"
USER_FILES_PATTERN = "user_rating*"

USERS_DATA_PKL = join(HOME_DIR_PATH, "data/users_data.pkl")
BOOKS_DATA_PKL = join(HOME_DIR_PATH, "data/books_data.pkl")
BOOKS_NAME_ID_MAP_PKL = join(HOME_DIR_PATH, "data/books_id_map.pkl")

# This is for user-based recommendation only

BOOK_ID_MAPPING_PKL = join(HOME_DIR_PATH, "src/user_based_rec_system/data/book_id_mapping.pkl")