from typing import Any    
    
import inflect     
from sqlalchemy.ext.declarative import as_declarative, declared_attr    
   
p = inflect.engine()  #Generate tables in plural  
    
@as_declarative()    
class Base:    
    id: Any    
    __name__: str    

    @declared_attr    
    def __tablename__(cls) -> str:    
        return p.plural(cls.__name__.lower())