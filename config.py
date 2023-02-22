class System:
    webdriver_path = r"C:\Users\David_Daimond\.wdm\drivers\chromedriver\win32\109.0.5414\chromedriver.exe"


class WebPage:
    url = "https://reqres.in/"

    endpoints_block_class = "endpoints"
    endpoint_tag = "li"

    response_block_class = 'response'
    response_code_class = 'response-code'  # need text
    response_output_tag = 'pre'  # need text


class API:
    url = "https://reqres.in/api/"

    methods = {
        "LIST_USERS_GET": "https://reqres.in/api/users",  # requires page param
        "SINGLE_USER_GET": "https://reqres.in/api/users/",  # requires id
        "LIST_RESOURCE_GET": "https://reqres.in/api/unknown",
        "SINGLE_RESOURCE_GET": "https://reqres.in/api/unknown/",  # requires id
        "CREATE_POST": "https://reqres.in/api/users",
        "UPDATE_PUT": "https://reqres.in/api/users/",  # requires id
        "UPDATE_PATCH": "https://reqres.in/api/users/",  # requires id
        "DELETE_DELETE": "https://reqres.in/api/users/",  # requires id
        "REGISTER_SUCCESSFUL_POST": "https://reqres.in/api/register",
        "REGISTER_UNSUCCESSFUL_POST": "https://reqres.in/api/register",
        "LOGIN_SUCCESSFUL_POST": "https://reqres.in/api/login",
        "LOGIN_UNSUCCESSFUL_POST": "https://reqres.in/api/login",
        "DELAYED_RESPONSE_GET": "https://reqres.in/api/users",  # requires delay param
    }

    users_schema = {'id': int,
                    'email': str,
                    'first_name': str,
                    'last_name': str,
                    'avatar': str,
                    }
    resources_schema = {'id': int,
                        'name': str,
                        'year': int,
                        'color': str,
                        'pantone_value': str,
                        }

    users_list = [{"id": 1, "email": "george.bluth@reqres.in", "first_name": "George", "last_name": "Bluth",
                   "avatar": "https://reqres.in/img/faces/1-image.jpg"},
                  {"id": 2, "email": "janet.weaver@reqres.in", "first_name": "Janet", "last_name": "Weaver",
                   "avatar": "https://reqres.in/img/faces/2-image.jpg"},
                  {"id": 3, "email": "emma.wong@reqres.in", "first_name": "Emma", "last_name": "Wong",
                   "avatar": "https://reqres.in/img/faces/3-image.jpg"},
                  {"id": 4, "email": "eve.holt@reqres.in", "first_name": "Eve", "last_name": "Holt",
                   "avatar": "https://reqres.in/img/faces/4-image.jpg"},
                  {"id": 5, "email": "charles.morris@reqres.in", "first_name": "Charles", "last_name": "Morris",
                   "avatar": "https://reqres.in/img/faces/5-image.jpg"},
                  {"id": 6, "email": "tracey.ramos@reqres.in", "first_name": "Tracey", "last_name": "Ramos",
                   "avatar": "https://reqres.in/img/faces/6-image.jpg"},
                  {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
                   "avatar": "https://reqres.in/img/faces/7-image.jpg"},
                  {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
                   "avatar": "https://reqres.in/img/faces/8-image.jpg"},
                  {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
                   "avatar": "https://reqres.in/img/faces/9-image.jpg"},
                  {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
                   "avatar": "https://reqres.in/img/faces/10-image.jpg"},
                  {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
                   "avatar": "https://reqres.in/img/faces/11-image.jpg"},
                  {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
                   "avatar": "https://reqres.in/img/faces/12-image.jpg"}
                  ]

    resources_list = [{"id": 1, "name": "cerulean", "year": 2000, "color": "#98B2D1", "pantone_value": "15-4020"},
                      {"id": 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375", "pantone_value": "17-2031"},
                      {"id": 3, "name": "true red", "year": 2002, "color": "#BF1932", "pantone_value": "19-1664"},
                      {"id": 4, "name": "aqua sky", "year": 2003, "color": "#7BC4C4", "pantone_value": "14-4811"},
                      {"id": 5, "name": "tigerlily", "year": 2004, "color": "#E2583E", "pantone_value": "17-1456"},
                      {"id": 6, "name": "blue turquoise", "year": 2005, "color": "#53B0AE", "pantone_value": "15-5217"},
                      {"id": 7, "name": "sand dollar", "year": 2006, "color": "#DECDBE", "pantone_value": "13-1106"},
                      {"id": 8, "name": "chili pepper", "year": 2007, "color": "#9B1B30", "pantone_value": "19-1557"},
                      {"id": 9, "name": "blue iris", "year": 2008, "color": "#5A5B9F", "pantone_value": "18-3943"},
                      {"id": 10, "name": "mimosa", "year": 2009, "color": "#F0C05A", "pantone_value": "14-0848"},
                      {"id": 11, "name": "turquoise", "year": 2010, "color": "#45B5AA", "pantone_value": "15-5519"},
                      {"id": 12, "name": "honeysuckle", "year": 2011, "color": "#D94F70", "pantone_value": "18-2120"}]
