from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from database.database import Member
from database.models import MemberRoles

from load import database 

class AvaibleRolesFilter(BoundFilter):
    """Filter accessed roles"""
    
    key = "available_roles"

    def __init__(self,available_roles:list[MemberRoles]):
        self.avaible_roles = available_roles
    
    async def check(self,message:types.Message):
        member = database.search_single_member(Member.user_id,message.from_user.id)
        
        if (member.role == "owner"):
            return True
         
        status = member.role in [role.value for role in self.avaible_roles]
        if (not status):
            await message.answer("Command not avaible")

        return status
