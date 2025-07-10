
from airflow.sdk import dag, task, chain

@dag
def my_new_dag():

    @task
    def my_task_1():
        return {"my_world": "Airflow!"}

    _my_task_1 = my_task_1()

    @task
    def my_task_2():
        print(my_dict["my_word"])

    _my_task_2 = my_task_2(my_dict=_my_task_1) 


my_new_dag()
