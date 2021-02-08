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


def generate_book_data():
    all_books_data = {}
    for filename in glob.glob(os.path.join(config.DATA_PATH, config.BOOK_FILES_PATTERN)):
        print("Currently processing books from file {}...".format(filename))
        book_data = utils.load_book_data(filename)
        all_books_data.update(book_data)

    return all_books_data


def generate_dataframe():
    print("Loading users data from pickle file...")
    users_data = joblib.load(config.USERS_DATA_PKL)
    print("Loading books data from pickle file...")
    books_data = joblib.load(config.BOOKS_DATA_PKL)

    book_titles = list(books_data.keys())
    del books_data

    num_users = len(users_data.keys())
    num_books = len(book_titles)

    users_books_matrix = np.zeros(num_users, num_books)


if __name__ == '__main__':
    print("Loading data for users...")
    users_data = generate_user_data()
    print("Saving users data to disk...")
    joblib.dump(users_data, config.USERS_DATA_PKL)

    print("Loading data for books...")
    books_data = generate_book_data()
    print("Saving books data to disk...")
    joblib.dump(books_data, config.BOOKS_DATA_PKL)