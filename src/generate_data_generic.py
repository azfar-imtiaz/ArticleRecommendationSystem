import os
import glob
import joblib
import numpy as np

import config
import utils


def generate_user_data():
    all_users_data = {}
    for filename in glob.glob(os.path.join(config.DATA_PATH, config.USER_FILES_PATTERN)):
        print("Currently processing users from file {}...".format(filename))
        user_data = utils.load_user_data(filename)
        all_users_data.update(user_data)

    return all_users_data


def generate_list_of_read_books():
    assert os.path.exists(config.USERS_DATA_PKL)
    assert os.path.exists(config.BOOKS_NAME_ID_MAP_PKL)
    books_read = set()
    users_data = joblib.load(config.USERS_DATA_PKL)
    book_id_mapping = joblib.load(config.BOOKS_NAME_ID_MAP_PKL)
    for usr_id, usr_data in users_data.items():
        usr_books = usr_data.keys()
        for bk_nm in usr_books:
            try:
                usr_book_id = book_id_mapping[bk_nm]
                books_read.add(usr_book_id)
            except KeyError:
                print("The book '{}' does not exist in the books dataset!".format(bk_nm))
        books_read.update(usr_books)
    
    return books_read


def generate_book_data():
    all_books_data = {}
    book_names_to_id_mapping = {}
    for filename in glob.glob(os.path.join(config.DATA_PATH, config.BOOK_FILES_PATTERN)):
        print("Currently processing books from file {}...".format(filename))
        book_data, book_name_id_map = utils.load_book_data(filename)
        all_books_data.update(book_data)
        book_names_to_id_mapping.update(book_name_id_map)

    return all_books_data, book_names_to_id_mapping


if __name__ == '__main__':
    print("Loading data for users...")
    users_data = generate_user_data()
    print("Saving users data to disk...")
    joblib.dump(users_data, config.USERS_DATA_PKL)

    print("Loading data for books...")
    books_data, books_name_to_id_mapping = generate_book_data()
    print("Saving books data to disk...")
    joblib.dump(books_data, config.BOOKS_DATA_PKL)
    joblib.dump(books_name_to_id_mapping, config.BOOKS_NAME_ID_MAP_PKL)