from ..repositories.users import UserActions as userRespository

def getUserByName(firstname)
    user = userRespository.get_by_first_name(first_name)
    