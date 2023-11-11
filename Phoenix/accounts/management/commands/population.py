from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from accounts.models import CustomUser
import random
import string
import requests
import os
from pathlib import Path
import shutil


class Command(BaseCommand):
    help = 'Add a number of sample users to the database'

    def add_arguments(self, parser):
        parser.add_argument('number_of_users', type=int,
                            help='Number of users to be created')
        parser.add_argument('--admin', action='store_true',
                            help='Make all created users as admin')

    def handle(self, *args, **kwargs):
        number_of_users = kwargs['number_of_users']
        make_admin = kwargs['admin']

        # Path to the directory where images are stored
        IMAGE_DIR = Path(r"C:\Users\Ivy\Videos\Pic2 - Copy")
        CHOSEN_IMAGE_DIR = Path(
            r"C:\Users\Ivy\OneDrive\Desktop\Project-Phoenix\Phoenix\media\profile_pics")

        # File to keep track of the images that have been picked
        PICKED_IMAGES_FILE = IMAGE_DIR / 'safe project.txt'

        # Function to get a list of all image files in the directory

        def get_image_files(directory):
            return [f for f in os.listdir(directory) if f.endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Function to pick a unique random image

        def pick_unique_image(directory):
            all_images = set(get_image_files(directory))
            picked_images = set()

            # Load the set of already picked images if the file exists
            if PICKED_IMAGES_FILE.exists():
                with open(PICKED_IMAGES_FILE, 'r', encoding='utf-8') as file:
                    picked_images = set(file.read().splitlines())

            # Select an image that has not been picked yet
            available_images = list(all_images - picked_images)
            if not available_images:
                raise ValueError('No more unique images to pick.')

            selected_image = random.choice(available_images)

            # Add the selected image to the set of picked images
            picked_images.add(selected_image)
            with open(PICKED_IMAGES_FILE, 'w', encoding='utf-8') as file:
                file.write('\n'.join(picked_images))

            source_image_path = directory / selected_image
            destination_image_path = CHOSEN_IMAGE_DIR / selected_image
            shutil.move(str(source_image_path), str(destination_image_path))

            return selected_image

        def get_random_user_info():
            try:
                # Make a request to the Random User Generator API
                response = requests.get('https://randomuser.me/api/')
                response.raise_for_status()  # Check for response status

                # Parse the JSON result
                user_data = response.json()
                user = user_data['results'][0]

                # Extracting the necessary information
                first_name = user['name']['first']
                last_name = user['name']['last']
                street = f"{user['location']['street']['number']} {user['location']['street']['name']}"
                city = user['location']['city']
                state = user['location']['state']
                country = user['location']['country']
                postcode = user['location']['postcode']
                full_address = f"{street}, {city}, {state}, {postcode}, {country}"
                phone_number = user['phone']
                birthday = user['dob']['date']
                gender = user['gender']
                picture = user['picture']['large']

                # Checking if all information is available
                if all([first_name, last_name, full_address, phone_number, birthday, gender, city, country, picture]):
                    # Preparing the output
                    user_info = {
                        'First Name': first_name,
                        'Last Name': last_name,
                        'Address': full_address,
                        'Phone Number': phone_number,
                        'Birthday': birthday,
                        'Gender': gender,
                        'City': city,
                        'Country': country,
                        'Picture URL': picture
                    }
                    return user_info
                else:
                    return "Incomplete information received."

            except requests.HTTPError as http_err:
                return f"HTTP error occurred: {http_err}"
            except Exception as err:
                return f"An error occurred: {err}"

        # Get a random user's information and print it
        names = {'Zion': 'male', 'Kai': 'male', 'Maeve': 'female', 'Luca': 'male', 'Nova': 'female', 'Mia': 'female', 'Aaliyah': 'female', 'Mila': 'female', 'Aurora': 'female', 'Quinn': 'male', 'Ezra': 'male', 'Eliana': 'female', 'Lucy': 'female', 'Jayden': 'male', 'Amara': 'female', 'Kayden': 'male', 'Lilibet': 'female', 'Isabella': 'female', 'Alina': 'female', 'Elliot': 'male', 'River': 'male', 'Xavier': 'male', 'Zoey': 'female', 'Isla': 'female', 'Lyla': 'female', 'Alex': 'male', 'Molly': 'female', 'Andrea': 'female', 'Remi': 'male', 'Rowan': 'male', 'Elias': 'male', 'Alice': 'female', 'Hayden': 'male', 'Rohan': 'male', 'Ophelia': 'female', 'Kyle': 'male', 'Jude': 'male', 'Mya': 'female', 'Shia': 'female', 'Cecilia': 'female', 'Milo': 'male', 'Finn': 'male', 'Leilani': 'female', 'Aria': 'female', 'Atlas': 'male', 'Evan': 'male', 'Millie': 'female', 'Axel': 'male', 'Urban': 'male', 'Amaya': 'female', 'Kayla': 'female', 'Jesse': 'male', 'Ian': 'male', 'Riley': 'male', 'Bailey': 'female', 'Julia': 'female', 'Blake': 'male', 'Ari': 'male', 'Savannah': 'female', 'Freya': 'female', 'Ira': 'female', 'Sharon': 'female', 'Sydney': 'female', 'Raya': 'female', 'Skylar': 'female', 'Marcus': 'male', 'Marie': 'female', 'Malachi': 'male', 'Brianna': 'female', 'Rachel': 'female', 'Brielle': 'female', 'Silas': 'male', 'Hudson': 'male', 'Mika': 'male', 'Kian': 'male', 'Arlo': 'male', 'Charlie': 'male', 'Theo': 'male', 'Mateo': 'male', 'Aiden': 'male', 'Kyra': 'female', 'Arthur': 'male', 'Reese': 'male', 'Thea': 'female', 'Zoe': 'female', 'Valerie': 'female', 'Rae': 'female', 'Leo': 'male', 'Mina': 'female', 'Camille': 'female', 'Sean': 'male', 'Ayla': 'female', 'Asa': 'male', 'Zara': 'female', 'Alaina': 'female', 'Luna': 'female', 'Ava': 'female', 'Natasha': 'female', 'Nancy': 'female', 'Nia': 'female', 'Myra': 'female', 'Dante': 'male', 'Evie': 'female', 'Everly': 'female', 'Everett': 'male', 'Alana': 'female', 'Elise': 'female', 'Jasmine': 'female', 'Louise': 'female', 'Skyler': 'male', 'Margot': 'female', 'Sloane': 'female', 'Alyssa': 'female', 'Kieran': 'male', 'Hailey': 'female', 'Vivian': 'female', 'Hadassah': 'female', 'Octavia': 'female', 'Isabelle': 'female', 'Maria': 'female', 'Damien': 'male', 'Sasha': 'female', 'Lara': 'female', 'Nolan': 'male', 'Adira': 'female', 'Camila': 'female', 'Rhea': 'female', 'Lyra': 'female', 'Jalen': 'male', 'Maverick': 'male', 'Finley': 'male', 'Elaine': 'female', 'Khadijah': 'female', 'Harlow': 'male', 'Lennox': 'male', 'Morgan': 'male', 'Ariella': 'female', 'Wren': 'male', 'Miles': 'male', 'Lisa': 'female', 'Jade': 'female', 'Amelia': 'female', 'Dior': 'female', 'Elodie': 'female', 'Lea': 'female', 'Mackenzie': 'female', 'Josie': 'female', 'Yara': 'female', 'Otis': 'male', 'Elora': 'female', 'Alan': 'male', 'Giselle': 'female', 'Gigi': 'female', 'Damian': 'male', 'Gianna': 'female', 'Shelby': 'female', 'Zayne': 'male', 'Monica': 'female', 'Rhys': 'male', 'Sage': 'male', 'Rebecca': 'female', 'Arden': 'male', 'Caleb': 'male', 'Giovanni': 'male', 'Aditya': 'male', 'Emerson': 'male', 'Kimberly': 'female', 'Lila': 'female', 'Aubrey': 'female', 'Sloan': 'male', 'Arianna': 'female', 'Leia': 'female', 'Lorenzo': 'male', 'Rayne': 'female', 'Rafael': 'male', 'Michelle': 'female', 'Aliyah': 'female', 'Callan': 'male', 'Aleena': 'female', 'Ellis': 'male', 'Beau': 'male', 'Orion': 'male', 'Xander': 'male', 'Avi': 'male', 'Madeline': 'female', 'Marley': 'male', 'Adeline': 'female', 'Liam': 'male', 'Kaiden': 'male', 'Ximena': 'female', 'Anya': 'female', 'Avery': 'male', 'Amira': 'female', 'Jean': 'female', 'Eloise': 'female', 'Rylee': 'female', 'Jocelyn': 'female', 'Maira': 'female', 'Zuri': 'female', 'Nyla': 'female', 'Niko': 'male', 'Amelie': 'female', 'Katherine': 'female', 'Eden': 'female', 'Piper': 'female', 'Olivia': 'female', 'Trisha': 'female', 'Harry': 'male', 'Lucian': 'male', 'Kevin': 'male', 'Helena': 'female', 'Ashton': 'male', 'Ayana': 'female', 'Liana': 'female', 'Cali': 'female', 'Noelle': 'female', 'Kaira': 'female', 'Delilah': 'female', 'Emery': 'male', 'Ada': 'female', 'Malia': 'female', 'Asher': 'male', 'Azariah': 'male', 'Seraphina': 'female', 'Justin': 'male', 'Adrian': 'male', 'Aisha': 'female', 'Lilah': 'female', 'Penny': 'female', 'Brayden': 'male', 'Chase': 'male', 'Nola': 'female', 'Pia': 'female', 'Kylie': 'female', 'Judah': 'male', 'Alani': 'female', 'Chelsea': 'female', 'Colin': 'male', 'Rory': 'male', 'Ivan': 'male', 'Annalise': 'female', 'Mariam': 'female', 'Lachlan': 'male', 'Brooks': 'male', 'Lynn': 'female', 'Callie': 'female', 'Lucas': 'male', 'Darcy': 'female', 'Nikita': 'female', 'Harper': 'male',
                 'Remy': 'male', 'Grayson': 'male', 'Colette': 'female', 'Enoch': 'male', 'Ryder': 'male', 'Wesley': 'male', 'Keanu': 'male', 'Sahil': 'male', 'Elena': 'female', 'Nicholas': 'male', 'Kaya': 'male', 'Sienna': 'female', 'Amos': 'male', 'Quincy': 'male', 'Alma': 'female', 'Ana': 'female', 'Naomi': 'female', 'Juno': 'male', 'Adriel': 'male', 'Lee': 'male', 'Oliver': 'male', 'Nevaeh': 'female', 'Hadley': 'male', 'Darren': 'male', 'Stella': 'female', 'Tessa': 'female', 'Juliana': 'female', 'Azalea': 'female', 'Sunny': 'male', 'Phoenix': 'male', 'Rai': 'male', 'Braxton': 'male', 'Makayla': 'female', 'Kali': 'female', 'Colton': 'male', 'Collin': 'male', 'Tara': 'female', 'Akira': 'male', 'Alaia': 'female', 'Amani': 'female', 'Brooke': 'female', 'Sawyer': 'male', 'Lorraine': 'female', 'Kaden': 'male', 'Kalani': 'male', 'Dennis': 'male', 'Beckett': 'male', 'Imani': 'female', 'Dillon': 'male', 'Mabel': 'female', 'Cole': 'male', 'Aliza': 'female', 'Cecil': 'male', 'Ace': 'male', 'Ethan': 'male', 'Huxley': 'male', 'Oakley': 'male', 'Gracie': 'female', 'Maren': 'female', 'Sophie': 'female', 'Sanjana': 'female', 'Reyna': 'female', 'Zaid': 'male', 'Flora': 'female', 'Ronan': 'male', 'Mona': 'female', 'Rhiannon': 'female', 'Cairo': 'male', 'Olive': 'female', 'Scott': 'male', 'Elina': 'female', 'Skye': 'female', 'Alexandra': 'female', 'Parker': 'male', 'Rian': 'male', 'Willa': 'female', 'Alena': 'female', 'Lauren': 'female', 'Margaret': 'female', 'Tiana': 'female', 'Claudia': 'female', 'Emmet': 'male', 'Elia': 'male', 'Devin': 'male', 'Nora': 'female', 'Mimi': 'female', 'Sadie': 'female', 'Cooper': 'male', 'Ambrose': 'male', 'Joan': 'female', 'Chiara': 'female', 'Zola': 'female', 'Ellie': 'female', 'Ravi': 'male', 'Rylan': 'male', 'Noa': 'female', 'Amaris': 'female', 'Ines': 'female', 'Hunter': 'male', 'George': 'male', 'Raine': 'female', 'Stanley': 'male', 'Levi': 'male', 'Heather': 'female', 'May': 'female', 'Rosie': 'female', 'Winston': 'male', 'Nellie': 'female', 'Amora': 'female', 'Lily': 'female', 'Blair': 'male', 'Bryce': 'male', 'Lorelei': 'female', 'August': 'male', 'Declan': 'male', 'Kelvin': 'male', 'Amir': 'male', 'Rocco': 'male', 'Israel': 'male', 'Alayna': 'female', 'Kendall': 'male', 'Shay': 'male', 'Adalyn': 'female', 'Francis': 'male', 'Misha': 'male', 'Mikayla': 'female', 'Ellen': 'female', 'Elisa': 'female', 'Zane': 'male', 'Lilian': 'female', 'Rei': 'male', 'Gemma': 'female', 'Abel': 'male', 'Noah': 'male', 'Marina': 'female', 'Ayden': 'male', 'Davina': 'female', 'Lola': 'female', 'Mayra': 'female', 'Veda': 'female', 'Marion': 'female', 'Killian': 'male', 'Imogen': 'female', 'Preston': 'male', 'June': 'female', 'Maureen': 'female', 'Christine': 'female', 'Mae': 'female', 'Bennett': 'male', 'Lilith': 'female', 'Fallon': 'female', 'Isaac': 'male', 'Remington': 'male', 'Adaline': 'female', 'Leon': 'male', 'Fiona': 'female', 'Nisha': 'female', 'Della': 'female', 'Cruz': 'male', 'Mira': 'female', 'Iva': 'female', 'Joyce': 'female', 'Winifred': 'female', 'Kailani': 'female', 'Harley': 'male', 'Theodore': 'male', 'Tyson': 'male', 'Thalia': 'female', 'Reece': 'male', 'Emelia': 'female', 'Leila': 'female', 'Rio': 'male', 'Leigh': 'female', 'Ahmed': 'male', 'Maximus': 'male', 'Romy': 'female', 'Emmett': 'male', 'Reya': 'female', 'Dakota': 'male', 'Genevieve': 'female', 'Sabine': 'female', 'Cheryl': 'female', 'Odette': 'female', 'Maya': 'female', 'Javier': 'male', 'Sana': 'female', 'Gia': 'female', 'Azriel': 'male', 'Sergio': 'male', 'Harvey': 'male', 'Ali': 'male', 'Jael': 'female', 'Jenny': 'female', 'Kaleb': 'male', 'Zia': 'male', 'Paxton': 'male', 'Jolene': 'female', 'Charlotte': 'female', 'Roman': 'male', 'Zena': 'female', 'Raina': 'female', 'Teddy': 'male', 'Cayden': 'male', 'Amyra': 'female', 'Melissa': 'female', 'Kyler': 'male', 'Kenji': 'male', 'Felix': 'male', 'Jasper': 'male', 'Maxine': 'female', 'Daisy': 'female', 'Colby': 'male', 'Vera': 'female', 'Sidney': 'male', 'Adonis': 'male', 'Martha': 'female', 'Kye': 'male', 'Kathleen': 'female', 'Liya': 'female', 'Lyric': 'male', 'Mavis': 'female', 'Kayleigh': 'female', 'Kane': 'male', 'Jayce': 'male', 'Mara': 'female', 'Livia': 'female', 'Elyse': 'female', 'Elliott': 'male', 'Theresa': 'female', 'Briar': 'male', 'Saira': 'female', 'Simone': 'female', 'Magdalena': 'female', 'Hallie': 'female', 'Yana': 'female', 'Keziah': 'female', 'Nathan': 'male', 'Cleo': 'female', 'Karina': 'female', 'Greyson': 'male', 'Caiden': 'male', 'Alisa': 'female', 'Layla': 'female', 'Jovi': 'male', 'Kit': 'male', 'Hayley': 'female', 'Sutton': 'male', 'Cain': 'male', 'Presley': 'male', 'Rayna': 'female'}

        try:
            for _ in range(number_of_users):
                random_user_info = get_random_user_info()
                no_of_words = random.randint(1, 3)
                name_gen = list(set([random.choice(list(names.keys()))
                                for i in range(no_of_words)]))
                user_name = " ".join(name_gen)
                # username = ''.join(random.choice(
                #     string.ascii_lowercase) for i in range(10))
                username = "".join(name_gen)
                while username in CustomUser.objects.values_list(
                        'username', flat=True):
                    number = random.randint(1, 999)
                    username += str(number)
                email = f"{username}@example.com"
                password = 'testpassword'
                random_user_info['Birthday'] = random_user_info['Birthday'].split("T")[
                    0]
                try:
                    image_path = pick_unique_image(IMAGE_DIR)
                    print(f'Picked image: {image_path}')
                except ValueError as e:
                    print(e)
                if make_admin:
                    CustomUser.objects.create_superuser(
                        username=username, email=email, password=password)
                else:
                    CustomUser.objects.create_user(
                        username=username, email=email, password=password, first_name=name_gen[0], last_name=" ".join(name_gen[1:]), birthday=random_user_info['Birthday'], phone_number=random_user_info['Phone Number'], address=random_user_info["Address"], gender=names[name_gen[0]].title(), city=random_user_info["City"], country=random_user_info["Country"], image="profile_pics\\" + image_path)

                    self.stdout.write(self.style.SUCCESS(
                        f'Successfully created user: {username}'))

            # Call the 'clearsessions' command
            call_command('clearsessions')

        except Exception as e:
            raise CommandError(f"Error occurred: {e}")

        self.stdout.write(self.style.SUCCESS(
            f'Successfully added {number_of_users} users!'))
