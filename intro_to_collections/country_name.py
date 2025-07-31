person_to_country = {
    'Alice': 'USA',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

def get_country(person):
    print (f'{person} is from {person_to_country[person]}')

get_country('Monika')
