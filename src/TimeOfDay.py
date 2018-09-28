# From Java version in https://www.youtube.com/watch?v=APUCMSPiNh4

MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
MINUTES_IN_DAY = MINUTES_IN_HOUR * HOURS_IN_DAY

class TimeOfDay:
  def __init__(self, hours=0, minutes=0):
    self.total_time_in_minutes = hours * MINUTES_IN_HOUR + minutes
  
  def hour():
    return self.total_time_in_minutes / MINUTES_IN_HOUR

  def minute():
    return self.total_time_in_minutes % MINUTES_IN_HOUR

  @classmethod
  def with_hour(cls, new_hour):
    return cls(hours=new_hour)