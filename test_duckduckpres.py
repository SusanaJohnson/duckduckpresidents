from pip._vendor import requests
from json import dumps

url = 'https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json'

def test_ddg0():


    response = requests.get(url).json()

    presidents =[""]
    names = []
    listOfPresidents = ["George Washington",
                        "John Adams",
                        "Thomas Jefferson",
                        "James Madison",
                        "James Monroe",
                        "John Quincy Adams",
                        "Andrew Jackson",
                        "Martin Van Buren",
                        "William Henry Harrison",
                        "John Tyler",
                        "James K. Polk",
                        "Zachary Taylor",
                        "Millard Fillmore",
                        "Franklin Pierce",
                        "James Buchanan",
                        "Abraham Lincoln",
                        "Andrew Johnson",
                        "Ulysses S. Grant",
                        "Rutherford B. Hayes",
                        "James A. Garfield",
                        "Chester A. Arthur",
                        "Grover Cleveland",
                        "Benjamin Harrison",
                        "William McKinley",
                        "Theodore Roosevelt",
                        "William Howard Taft",
                        "Woodrow Wilson",
                        "Warren G. Harding",
                        "Calvin Coolidge",
                        "Herbert Hoover",
                        "Franklin D. Roosevelt",
                        "Harry S. Truman",
                        "Dwight D. Eisenhower",
                        "John F. Kennedy",
                        "Lyndon B. Johnson",
                        "Richard Nixon",
                        "Gerald Ford",
                        "Jimmy Carter",
                        "Ronald Reagan",
                        "George H. W. Bush",
                        "Bill Clinton",
                        "George W. Bush",
                        "Barack Obama",
                        "Donald Trump"
                        ]

    for pres in response['RelatedTopics']:
        name = pres['Text'].split('-')[0].strip()
        lengthName = 0
        if 'Bibliography' in name:
            lenghtName = len(name)
            name = name[16: len(name)]
        if ("President of the United States" not in pres['Text']):
            if ("Historical rankings of presidents of the United States" not in pres['Text']):
                if ("Lifespan timeline of presidents of the United States" not in pres['Text']):
                    if ("Mesonoemacheilus menoni" not in pres['Text']):
                        if ("Sid Sriram" not in pres['Text']):
                            names.append(name)


    for n in range(45):
        assert names[n] in listOfPresidents