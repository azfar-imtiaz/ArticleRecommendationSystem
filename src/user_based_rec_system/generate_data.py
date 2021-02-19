import sys
import joblib
import numpy as np
import pandas as pd

sys.path.append("..")

import config


def generate_book_id_mapping():
    user_data = joblib.load(config.USERS_DATA_PKL)
    book_id_mapping = {}
    id_counter = 0
    for _, book_data in user_data.items():
        for book_name in book_data.keys():
            book_name = book_name.lower().strip()
            try:
                book_id_mapping[book_name]
            except KeyError:
                book_id_mapping[book_name] = id_counter
                id_counter += 1

    joblib.dump(book_id_mapping, config.BOOK_ID_MAPPING_PKL)


def generate_dataframe():
    # NOTE: Move this inside a separate function inside utils.py
    try:
        users_data = joblib.load(config.USERS_DATA_PKL)
    except FileNotFoundError:
        from generate_data_generic import generate_user_data
        generate_user_data()
        users_data = joblib.load(config.USERS_DATA_PKL)
    
    # NOTE: Move this inside a separate function inside utils.py
    try:
        book_id_mapping = joblib.load(config.BOOK_ID_MAPPING_PKL)
    except FileNotFoundError:
        generate_book_id_mapping()
        book_id_mapping = joblib.load(config.BOOK_ID_MAPPING_PKL)

    # Get list of users IDs. These will be the rows
    users_list = list(users_data.keys())
    # Get IDs of books. These will be the columns
    book_ids = list(book_id_mapping.values())

    # Generate matrix of shape users x books, fill it with zeros
    data_matrix = np.zeros((len(users_list), len(book_ids)), dtype=int)
    
    # Populate user-book cells with corresponding ratings
    for index, usr_id in enumerate(users_list):
        if index % 500 == 0:
            print("{} user records have been processed!".format(index))
        for book_name, rating in users_data[usr_id].items():
            book_name = book_name.lower().strip()
            book_id = book_id_mapping[book_name]
            data_matrix[index, book_id] = rating

    # Create a dataframe. Set list of users as index, and book IDs list as columns
    df = pd.DataFrame(data_matrix, index=users_list, columns=book_ids)
    return df