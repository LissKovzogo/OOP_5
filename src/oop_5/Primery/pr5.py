from typing import Optional

def find_user_id(name:str)-> Optional[int]:
    users = {"Alice":1,"Bob":2}
    return users.get(name)

uid = find_user_id("Charlie")
print(uid+1)