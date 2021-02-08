import csv
from langdetect import detect
from collections import defaultdict

import constants


def load_user_data(filename):
    user_data = defaultdict(lambda: {})
    with open(filename, 'r') as rfile:
        reader = csv.DictReader(rfile)
        # TODO: Here we can implement a functionality that everytime we start loading records for a new user,
        # check the total amount of books the previous user has rated. If they are less than a certain
        # threshold, remove the data of this user from the dict.
        for elem in reader:
            user_id = int(elem['ID'])
            book_name = elem['Name']
            user_rating = elem['Rating']
            
            if user_rating in constants.RATINGS_TO_IGNORE:
                continue
            # Convert the text rating to its equivalent rating score
            user_rating = constants.RATING_TXT_TO_NUM_MAPPING[user_rating]
            
            if book_name.strip() == '':
                continue

            user_data[user_id][book_name] = user_rating

    return dict(user_data)


def load_book_data(filename):
    books_data = {}
    with open(filename, 'r') as rfile:
        reader = csv.DictReader(rfile)
        for index, elem in enumerate(reader):
            book_id = int(elem['Id'])
            book_name = elem['Name']
            book_rating = elem['Rating']
            book_language = elem['Language']
            # NOTE: This takes too long when loading data for all books
            # book_language = detect(book_name)
            try:
                book_num_pages = elem['pagesNumber']
            except KeyError:
                book_num_pages = elem['PagesNumber']

            # TODO: We can perhaps use the CountsOfReview column to filter out books with too less reviews?

            books_data[book_name] = {
                'id': book_id,
                'rating': book_rating,
                'language': book_language,
                'num_pages': book_num_pages
            }

    return books_data