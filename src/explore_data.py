import os
import csv
import glob
from collections import defaultdict


def explore_books_data(filename):
    field_names = ['Id', 'Name', 'RatingDist1', 'pagesNumber', 'RatingDist4', 'RatingDistTotal', 'PublishMonth', 'PublishDay', 'Publisher', 'CountsOfReview', 'PublishYear', 'Language', 'Authors', 'Rating', 'RatingDist2', 'RatingDist5', 'ISBN', 'RatingDist3']
    with open(filename, 'r') as rfile:
        reader = csv.DictReader(rfile, fieldnames=field_names)
        for index, elem in enumerate(reader):
            if index > 10:
                break
            print(elem['Id'])
            print(elem['Name'])
            print(elem['Rating'])
            print(elem['Language'])
            # this can be used to filter out some books
            print(elem['pagesNumber'])


def explore_users_data(filename):
    field_names = ['ID', 'Name', 'Rating']
    ratings = set()
    with open(filename, 'r') as rfile:
        reader = csv.DictReader(rfile, fieldnames=field_names)
        for index, elem in enumerate(reader):
            if index <= 10:
                print("{}, {}".format(elem['Name'], elem['Rating']))
            ratings.add(elem['Rating'])
            
    print("Unique ratings are: ", ratings)


def explore_all_users(filenames):
    field_names = ['ID', 'Name', 'Rating']
    users = defaultdict(lambda: defaultdict())
    for filename in filenames:
        with open(filename, 'r') as rfile:
            reader = csv.DictReader(rfile, fieldnames=field_names)
            for index, elem in enumerate(reader):
                if index == 0:
                    continue
                user_rating = elem['Rating']
                if user_rating == "This user doesn't have any rating" or user_rating == 'Rating':
                    continue
                book_name = elem['Name']
                if book_name.strip() == '':
                    continue
                user_id = int(elem['ID'])
                users[user_id][book_name] = user_rating
    return users


if __name__ == '__main__':
    books_data_filename = "../data/archive/book1-100k.csv"
    explore_books_data(books_data_filename)

    users_data_filename = "../data/archive/user_rating_1000_to_2000.csv"
    explore_users_data(users_data_filename)

    path_to_files = "../data/archive/"
    user_files_pattern = "user_rating_*"
    user_data_files = glob.glob(os.path.join(path_to_files, user_files_pattern))
    user_data = explore_all_users(user_data_files)