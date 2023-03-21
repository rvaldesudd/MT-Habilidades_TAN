#main objective Use libraries and plan your project to create Python programs that are more advanced. 
#in bash --- pip freeze > requirements.txt
from datetime import *
from dateutil.relativedelta import *
now = datetime.now()
print(now)

now = now + relativedelta(months=1, weeks=1, hour=10)

print(now)
