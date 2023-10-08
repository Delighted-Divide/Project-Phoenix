from django.test import TestCase
import random
import string
from .models import CustomUser
# Create your tests here.


class UserModelTest(TestCase):
    def test_user_creation(self):
        def CustomuserCreation(username):
            return CustomUser(username=username, password='testpassword', email=f"{username}@example.com")

        number_of_users = 2000
        make_admin = False
        names = ['Zion', 'Kai', 'Maeve', 'Luca', 'Nova', 'Mia', 'Aaliyah', 'Mila', 'Aurora', 'Quinn', 'Ezra', 'Eliana', 'Ivy',
                 'Jayden', 'Amara', 'Kayden', 'Lilibet', 'Isabella', 'Alina', 'Elliot', 'River', 'Xavier', 'Zoey', 'Isla',
                 'Lyla', 'Alex', 'Molly', 'Andrea', 'Remi', 'Rowan', 'Elias', 'Alice', 'Hayden', 'Rohan', 'Ophelia', 'Kyle',
                 'Jude', 'Mya', 'Shia', 'Cecilia', 'Milo', 'Finn', 'Leilani', 'Aria', 'Atlas', 'Evan', 'Millie', 'Axel',
                 'Urban',
                 'Amaya', 'Kayla', 'Jesse', 'Ian', 'Riley', 'Bailey', 'Julia', 'Blake', 'Ari', 'Savannah', 'Freya', 'Ira',
                 'Sharon', 'Sydney', 'Raya', 'Skylar', 'Marcus', 'Marie', 'Malachi', 'Brianna', 'Rachel', 'Brielle', 'Silas',
                 'Hudson', 'Mika', 'Kian', 'Arlo', 'Charlie', 'Theo', 'Mateo', 'Aiden', 'Kyra', 'Arthur', 'Reese', 'Thea',
                 'Zoe',
                 'Valerie', 'Rae', 'Leo', 'Mina', 'Camille', 'Sean', 'Ayla', 'Asa', 'Zara', 'Alaina', 'Luna', 'Ava', 'Natasha',
                 'Nancy', 'Nia', 'Myra', 'Dante', 'Evie', 'Everly', 'Everett', 'Alana', 'Elise', 'Jasmine', 'Louise', 'Skyler',
                 'Margot', 'Sloane', 'Alyssa', 'Kieran', 'Hailey', 'Vivian', 'Hadassah', 'Octavia', 'Isabelle', 'Maria',
                 'Damien', 'Sasha', 'Lara', 'Nolan', 'Adira', 'Camila', 'Rhea', 'Lyra', 'Jalen', 'Maverick', 'Finley', 'Elaine',
                 'Khadijah', 'Harlow', 'Lennox', 'Morgan', 'Ariella', 'Wren', 'Miles', 'Lisa', 'Jade', 'Amelia', 'Dior',
                 'Elodie', 'Lea', 'Mackenzie', 'Josie', 'Yara', 'Otis', 'Elora', 'Alan', 'Giselle', 'Gigi', 'Damian', 'Gianna',
                 'Shelby', 'Zayne', 'Monica', 'Rhys', 'Sage', 'Rebecca', 'Arden', 'Caleb', 'Giovanni', 'Aditya', 'Emerson',
                 'Kimberly', 'Lila', 'Aubrey', 'Sloan', 'Arianna', 'Leia', 'Lorenzo', 'Rayne', 'Rafael', 'Michelle', 'Aliyah',
                 'Callan', 'Aleena', 'Ellis', 'Beau', 'Orion', 'Xander', 'Avi', 'Madeline', 'Marley', 'Adeline', 'Liam',
                 'Kaiden', 'Ximena', 'Anya', 'Avery', 'Amira', 'Jean', 'Eloise', 'Rylee', 'Jocelyn', 'Maira', 'Zuri', 'Nyla',
                 'Niko', 'Amelie', 'Katherine', 'Eden', 'Piper', 'Olivia', 'Trisha', 'Harry', 'Lucian', 'Kevin', 'Helena',
                 'Ashton', 'Ayana', 'Liana', 'Cali', 'Noelle', 'Kaira', 'Delilah', 'Emery', 'Ada', 'Malia', 'Asher', 'Azariah',
                 'Seraphina', 'Justin', 'Adrian', 'Aisha', 'Lilah', 'Penny', 'Brayden', 'Chase', 'Nola', 'Pia', 'Kylie',
                 'Judah',
                 'Alani', 'Chelsea', 'Colin', 'Rory', 'Ivan', 'Annalise', 'Mariam', 'Lachlan', 'Brooks', 'Lynn', 'Callie',
                 'Lucas', 'Darcy', 'Nikita', 'Harper', 'Remy', 'Grayson', 'Colette', 'Enoch', 'Ryder', 'Wesley', 'Keanu',
                 'Sahil', 'Elena', 'Nicholas', 'Kaya', 'Sienna', 'Amos', 'Quincy', 'Alma', 'Ana', 'Naomi', 'Juno', 'Adriel',
                 'Lee', 'Oliver', 'Nevaeh', 'Hadley', 'Darren', 'Stella', 'Tessa', 'Juliana', 'Azalea', 'Sunny', 'Phoenix',
                 'Rai', 'Braxton', 'Makayla', 'Kali', 'Colton', 'Collin', 'Tara', 'Akira', 'Alaia', 'Amani', 'Brooke', 'Sawyer',
                 'Lorraine', 'Kaden', 'Kalani', 'Dennis', 'Beckett', 'Imani', 'Dillon', 'Mabel', 'Cole', 'Aliza', 'Cecil',
                 'Ace',
                 'Ethan', 'Huxley', 'Oakley', 'Gracie', 'Maren', 'Sophie', 'Sanjana', 'Reyna', 'Zaid', 'Flora', 'Ronan', 'Mona',
                 'Rhiannon', 'Cairo', 'Olive', 'Scott', 'Elina', 'Skye', 'Alexandra', 'Parker', 'Rian', 'Willa', 'Alena',
                 'Lauren', 'Margaret', 'Tiana', 'Claudia', 'Emmet', 'Elia', 'Devin', 'Nora', 'Mimi', 'Sadie', 'Cooper',
                 'Ambrose', 'Joan', 'Chiara', 'Zola', 'Ellie', 'Ravi', 'Rylan', 'Noa', 'Amaris', 'Ines', 'Hunter', 'George',
                 'Raine', 'Stanley', 'Levi', 'Heather', 'May', 'Rosie', 'Winston', 'Nellie', 'Amora', 'Lily', 'Blair', 'Bryce',
                 'Lorelei', 'August', 'Declan', 'Kelvin', 'Amir', 'Rocco', 'Israel', 'Alayna', 'Kendall', 'Shay', 'Adalyn',
                 'Francis', 'Misha', 'Mikayla', 'Ellen', 'Elisa', 'Zane', 'Lilian', 'Rei', 'Gemma', 'Abel', 'Noah', 'Marina',
                 'Ayden', 'Davina', 'Lola', 'Mayra', 'Veda', 'Marion', 'Killian', 'Imogen', 'Preston', 'June', 'Maureen',
                 'Christine', 'Mae', 'Bennett', 'Lilith', 'Fallon', 'Isaac', 'Remington', 'Adaline', 'Leon', 'Fiona', 'Nisha',
                 'Della', 'Cruz', 'Mira', 'Iva', 'Joyce', 'Winifred', 'Kailani', 'Harley', 'Theodore', 'Tyson', 'Thalia',
                 'Reece', 'Emelia', 'Leila', 'Rio', 'Leigh', 'Ahmed', 'Maximus', 'Romy', 'Emmett', 'Reya', 'Dakota',
                 'Genevieve',
                 'Sabine', 'Cheryl', 'Odette', 'Maya', 'Javier', 'Sana', 'Gia', 'Azriel', 'Sergio', 'Harvey', 'Ali', 'Jael',
                 'Jenny', 'Kaleb', 'Zia', 'Paxton', 'Jolene', 'Charlotte', 'Roman', 'Zena', 'Raina', 'Teddy', 'Cayden', 'Amyra',
                 'Melissa', 'Kyler', 'Kenji', 'Felix', 'Jasper', 'Maxine', 'Daisy', 'Colby', 'Vera', 'Sidney', 'Adonis',
                 'Martha', 'Kye', 'Kathleen', 'Liya', 'Lyric', 'Mavis', 'Kayleigh', 'Kane', 'Jayce', 'Mara', 'Livia', 'Elyse',
                 'Elliott', 'Theresa', 'Briar', 'Saira', 'Simone', 'Magdalena', 'Hallie', 'Yana', 'Keziah', 'Nathan', 'Cleo',
                 'Karina', 'Greyson', 'Caiden', 'Alisa', 'Layla', 'Jovi', 'Kit', 'Hayley', 'Sutton', 'Cain', 'Presley', 'Rayna']

        for _ in range(number_of_users):
            no_of_words = random.randint(1, 3)
            name_gen = list(set([random.choice(names)
                            for i in range(no_of_words)]))
            user_name = " ".join(name_gen)
            # username = ''.join(random.choice(
            #     string.ascii_lowercase) for i in range(10))
            username = "".join(name_gen)
            email = f"{username}@example.com"
            password = 'testpassword'
            while username in CustomUser.objects.values_list(
                    'username', flat=True):
                number = random.randint(1, 999)
                username += str(number)
            if make_admin:
                CustomUser.objects.create_superuser(
                    username=username, email=email, password=password)
            else:
                CustomUser.objects.create_user(
                    username=username, email=email, password=password)
            # print(CustomuserCreation(username))
            # print("_"*400)
            # print()
            # self.assertEqual(CustomUser.objects.get(id=_).__str__(),
            #                  username)
            # Call the 'clearsessions' command
        # for i in CustomUser.objects.values_list('username', flat=True):
        #     print(i)
        self.assertEqual(CustomUser.objects.count(),
                         number_of_users)
