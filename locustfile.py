from locust import HttpUser, TaskSet, task, between

class SimpleTasks(TaskSet):
    @task(1)
    def home(self):
        # Test the home route
        self.client.get("/")

    @task(2)
    def fast(self):
        # Test the fast route
        self.client.get("/fast")

    @task(3)
    def medium(self):
        # Test the medium route
        self.client.get("/medium")

    @task(4)
    def heavy(self):
        # Test the heavy route
        self.client.get("/heavy")

    @task(1)
    def echo(self):
        # Test the echo route
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

class HeavyTasks(TaskSet):
    @task(1)
    def home(self):
        self.client.get("/")
        
    @task(2)
    def fast(self):
        self.client.get("/fast")
        
    @task(3)
    def medium(self):
        self.client.get("/medium")
        
    @task(4)
    def heavy(self):
        self.client.get("/heavy")
        
    @task(1)
    def echo(self):
        payload = {"message": "Hello, Locust!"}
        self.client.post("/echo", json=payload)

class SimpleUser(HttpUser):
    tasks = [SimpleTasks]
    wait_time = between(1, 5)  # Simulate a wait time between requests
    weight = 1

    def on_start(self):
        print("SimpleUser started")

class HeavyUser(HttpUser):
    tasks = [HeavyTasks]
    wait_time = between(5, 10)
    weight = 1
