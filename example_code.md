# Goals

[x] - wrapping driver object with your driver
[x] - having a reference to the original driver
[x] - setting the config directly of via functions for the driver
[x] - logging every function
[meh] - error on every possible situation

[ ] - Proxy support
[ ] - Cookies support
[ ] - 
[ ] - 

[ ] - downloading drivers automatically
[ ] - tqdm for downloading drivers?
[x] - maybe halo for waiting for elements

# This is what I want the library to look like

## Finding and Waiting

```python
from donerkebab import *

driver = donerkebab.Chrome()

driver.set_max_wait_time(10);
driver.set_logging_level('MESSAGE');

driver.open('https://google.com') #Opened google.com

# Waits until this element loads, 
myDiv = driver.getFirst('div') # Located `div`

print(myDiv.text)

for el in myDiv.childs:
    print(el.text)

myDiv.parent # Usefull error if there is no parent

myDiv.
.id
.class
.name # gives out the full css name, 'div.container#root'



```