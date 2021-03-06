
---

**In order to use this library, you need to have an Anymate account. Please visit [anymate.io](https://www.anymate.io) for more information.**

---

Anymate Python SDK is written in Python 3.
The SDK is available as open source and can be found on [our github page][githublink]. 
You can find the documentation for the SDK as part of the [Anymate Developer docs][anymatedocs].

We have also published it at [pypi.org][pypilink]. Installing the Anymate package is done with the following command: 

``` python
    #Install through pip
    pip install --upgrade anymate
```

Once installed, you just need to import anymate in your python program and you are ready to go

``` python
   import anymate
```

After anymate has been imported, you have to initialize the client to communicate with Anymate.
The functions exposed in the client mirror the endpoints available in the API. We recommend going to the individual pages to learn more.


The SDK is built to automatically take care of authentication with Anymate as well as refreshing access_tokens as needed. Once the anymate.client is initialized, you don't have to worry about it.

You can see an example of a simple automation based on the Allocator Pattern below, where the automation script is working in one process and creating new tasks in another.

``` Python
    #Import the anymate library
    import anymate


    #Setting up variables for future use
    client_id = "My client id"
    client_secret = "My API secret"
    username = "Mate Username"
    password = "Mate Password"

    #The process where the script is working
    myProcessKey = "myProcessKey"

    #The target Process where we want to create tasks in
    targetProcessKey = "targetProcessKey"
    
    #Initialize the client
    client = anymate.client(client_id, client_secret, username, password)

    #Check if the script should start work
    is_ok_to_run = client.OkToRun(myProcessKey)
    if not is_ok_to_run.okToRun:
       #If there is nothing to do, then stop the script here
       return

    # Business logic not included. We assume that "new_tasks" is an array with objects ready for anymate.

    #Let Anymate know that work has begun
    run = client.start_or_get_run(myProcessKey)

    for task in new_tasks:
        #create a task for each object in the array 'new_tasks'
        client.create_task(targetProcessKey, task)
    
    #Let Anymate know the work is done
    client.finish_run(dict(runId=run.runId))

      
```

Making a script to take Tasks from the Queue and perform work on them is equally simple.

``` python

# Import the anymate library
import anymate

# Setting up variables for future use
client_id = "My client id"
client_secret = "My API secret"
username = "Mate Username"
password = "Mate Password"

# The process where the script is working
myProcessKey = "myProcessKey"


# Initialize the client
client = anymate.client(client_id, client_secret, username, password)

# Check if the script should start work
is_ok_to_run = client.OkToRun(myProcessKey)
if not is_ok_to_run.okToRun:
    # If there is nothing to do, then stop the script here
    return

# Business logic not included. We assume that "new_tasks" is an array with objects ready for anymate.

# Take first task from the queue - notice it is returned as a dictionary
task = client.take_next(myProcessKey)

#Our workloop continues while the TaskId is above 0. If the queue is empty, the TaskId will be -1.
while task['taskId'] > 0:
    #Businesslogic omitted. We have created a dummy function to take the Task as input and return if it is solved (true) or goes to manual (false)
    task_is_solved = PerformBusinessLogic(task)
    if task_is_solved:
        #Task was solved - solved and manual takes both dictionaries and objects, as long as they have the right keys/attributes.
        solved_result = client.solved(dict(taskId=task['taskId'], reason='Solved', comment = 'Task was solved'))
    else:
        #Send task to Manual
        manual_result = client.manual(dict(taskId=task['taskId'], reason='Manual', comment='Task was sent to Manual'))

    #Logic to handle exceptions and errors omitted
    task = client.take_next(myProcessKey)

```

## Enterprise On-Premises

The anymate SDK supports customers who have Anymate installed On-Premises with an Enterprise license out of the box.
In order to let anymate know you are running on a on-premises license, simply initialize the client with On Premises mode enabled.

``` python 
import anymate

# Initialize Client as always
client_id = "My client id"
client_secret = "My API secret"
username = "Mate Username"
password = "Mate Password"
client = anymate.client(client_id, client_secret, username, password)

#Define a Client uri and an auth uri
client_base_uri = "http://localanymate
auth_base_uri = "http://localanymateauth

#Set On Premises mode
client.set_on_premises_mode(client_base_uri, auth_base_uri)

#From here on, you can use the client as you otherwise would

```

[anymatedocs]: http://docs.anymate.io/developer/SDK/python/
[githublink]: https://github.com/anymate/AnymatePythonSDK/
[pypilink]: https://pypi.org/project/anymate/
