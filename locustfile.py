from locust import HttpLocust, TaskSet, task 

json_post = {
   "CHAS":{
      "0":0
   },
   "RM":{
      "0":6.575
   },
   "TAX":{
      "0":296.0
   },
   "PTRATIO":{
      "0":15.3
   },
   "B":{
      "0":396.9
   },
   "LSTAT":{
      "0":4.98
   }
}


class MyTaskSet(TaskSet):

    @task
    def get_request(self):
        self.client.get("/predict")

    @task
    def post_predict(self):
        self.client.post("/predict", json_post)


class WebsitteUser(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 9000

