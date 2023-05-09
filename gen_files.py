import pandas as pd

# Create roots of the graph
pd.DataFrame(
    {
        'name:ID': ['People', 'Books'], ':LABEL': ['ROOTS', 'ROOTS']
    }
).to_csv('./data/nodes_roots.csv', index=False)

pd.DataFrame(
    [
        {
            'name:ID': 'Person 1',
            'location': 'Noida',
            'gender': 'Male',
            'reader_type': 'Advanced',      
            ':LABEL': 'PEOPLE'
        },
        {
            'name:ID': 'Person 2',
            'location': 'Bangalore',
            'gender': 'Female',
            'reader_type': 'Beginner',
            ':LABEL': 'PEOPLE'
        },
        {
            'name:ID': 'Person 3',
            'location': 'New Delhi',
            'gender': 'Female',
            'reader_type': 'Beginner',        
            ':LABEL': 'PEOPLE'
        },
        {
            'name:ID': 'Person 4',
            'location': 'Mumbai',
            'gender': 'Female',
            'reader_type': 'Intermediate',       
            ':LABEL': 'PEOPLE'
        },
    ]
).to_csv('./data/nodes_people.csv', index=False)

pd.DataFrame(
    [
        {
            'name:ID': 'Book 1',
            'author': 'XYZ',
            ':LABEL': 'BOOKS'
        },
        {
            'name:ID': 'Book 2',
            'author': 'ABC',
            ':LABEL': 'BOOKS'
        },
        {
            'name:ID': 'Book 3',
            'author': 'ABC',
            ':LABEL': 'BOOKS'
        },
        {
            'name:ID': 'Book 4',
            'author': 'XYZ',
            ':LABEL': 'BOOKS'
        },
    ]
).to_csv('./data/nodes_books.csv', index=False)

pd.DataFrame(
    [
        {
            ':START_ID': 'People',
            ':END_ID': 'Person 1',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'People',
            ':END_ID': 'Person 2',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'People',
            ':END_ID': 'Person 3',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'People',
            ':END_ID': 'Person 4',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'Books',
            ':END_ID': 'Book 1',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'Books',
            ':END_ID': 'Book 2',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'Books',
            ':END_ID': 'Book 3',
            ':TYPE': 'CHILDREN',
        },
        {
            ':START_ID': 'Books',
            ':END_ID': 'Book 4',
            ':TYPE': 'CHILDREN',
        },
    ]
).to_csv('./data/relations_roots.csv', index=False)

pd.DataFrame(
    [
        {
            ':START_ID': 'Person 1',
            ':END_ID': 'Book 2',
            'number_of_times': 2,
            'rating:int': 4,
            ':TYPE': 'READ'
        },
        {
            ':START_ID': 'Person 1',
            ':END_ID': 'Book 3',
            'number_of_times': 1,
            'rating:int': 5,
            ':TYPE': 'READ'
        },
        {
            ':START_ID': 'Person 4',
            ':END_ID': 'Book 4',
            'number_of_times': 3,
            'rating:int': 4,
            ':TYPE': 'READ'
        },
    ]
).to_csv('./data/relations_read.csv', index=False)

pd.DataFrame(
    [
        {
            ':START_ID': 'Person 1',
            ':END_ID': 'Book 1', 
            ':TYPE': 'FAVOURITE'
        },
        {
            ':START_ID': 'Person 2',
            ':END_ID': 'Book 2',
            ':TYPE': 'FAVOURITE'
        },
        {
            ':START_ID': 'Person 3',
            ':END_ID': 'Book 3',
            ':TYPE': 'FAVOURITE'
        },
    ]
).to_csv('./data/relations_favourite.csv', index=False)
