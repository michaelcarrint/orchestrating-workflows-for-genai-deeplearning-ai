
from airflow.sdk import dag, task, chain

@dag
def my_second_new_dag():

    @task
    def my_task_1():
        print("This is task_1 running")
        return 100

    @task
    def my_task_2():
        print("This is task_2 also running")
        return 42

    @task
    def my_task_3(num1, num2):
        return num1 + num2

    @task
    def my_task_4():
        return "math"
        
    _my_task_1 = my_task_1()
    _my_task_2 = my_task_2()
    _my_task_3 = my_task_3(num1=my_task_1, num2=my_task_2)
    _my_task_4 = my_task_4()

    chain([_my_task_2, _my_task_3], _my_task_4)

my_second_new_dag()
    
