import re

message = 'currunt Python version is 3.13 in market there are 3.12, 3.11, 3.10'

# print('Python' in message)
# print('13' in message)
# print(message.find('is'))


matching = re.search(pattern = "[0-9][0-9]" , message)
print(matching)