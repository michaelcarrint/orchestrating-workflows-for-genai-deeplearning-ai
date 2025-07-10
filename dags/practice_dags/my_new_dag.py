
from airflow.sdk import dag, task, chain  # ✅ keep this if required by Astro

@dag
def my_new_dag():

    @task
    def my_task_1():
        return {"my_word": "Airflow!"}
    
    @task 
    def my_task_2(data):
        print(data["my_word"])

    # Call tasks
    _my_task_1 = my_task_1()
    _my_task_2 = my_task_2(_my_task_1)  # ✅ pass as positional arg

my_new_dag()

