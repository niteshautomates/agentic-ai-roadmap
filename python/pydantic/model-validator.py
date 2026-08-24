from pydantic import BaseModel, model_validator

class EventBooking(BaseModel):
    start_hour: int
    end_hour: int

    @model_validator(mode='after')
    def validate_hours(self):
        if self.end_hour <= self.start_hour:
            raise ValueError('end_hour must be greater than start_hour')
        return self

item = EventBooking(start_hour=10, end_hour=9)  # This will raise a ValueError
print(item)    