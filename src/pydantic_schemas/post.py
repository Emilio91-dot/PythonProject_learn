from pydantic import BaseModel, validator



class Post(BaseModel):
    id: int
    title: str


    ##name: str = Field(alias="_name")

    @validator('id')
    def check_that_id_is_less_than_two(cls, v):
        if v > 2:
            raise ValueError('ID must be less than 2')
        else:
            return v



##{'id': 1, 'title': 'Post 1', '_name": 'Igor'}