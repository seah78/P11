from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get('/')
        
    @task(20)
    def clubsBoard(self):
        self.client.get('/clubsBoard')

    @task
    def show_summary(self):
        self.client.post('/showSummary', {"email": "john@simplylift.co"})

    @task(7)
    def purchase_place(self):
        self.client.post('/purchasePlaces', {"club": "Simply Lift", "competition": "Fall Classic", "places": 4})
        
    @task
    def book(self):
        self.client.get('/book/Spring Festival/Simply Lift')