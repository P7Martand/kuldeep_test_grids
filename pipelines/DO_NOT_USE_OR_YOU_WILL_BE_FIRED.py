with DAG():
    route_data = Task(
        task_id = "route_data", 
        component = "Dataset", 
        table = {"name" : "route_data", "sourceType" : "Seed"}
    )
    city_information = Task(
        task_id = "city_information", 
        component = "Dataset", 
        table = {"name" : "city_data", "sourceType" : "Seed"}
    )
    airport_information = Task(
        task_id = "airport_information", 
        component = "Dataset", 
        table = {"name" : "airport", "sourceType" : "Seed"}
    )
    model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data = Task(
        task_id = "model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data", 
        component = "Model", 
        modelName = "model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data"
    )
    city_information.out >> model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data.in_0
    route_data.out >> model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data.in_2
    (
        airport_information.out
        >> [model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data.in_4,
              model_DO_NOT_USE_OR_YOU_WILL_BE_FIRED_city_route_data.in_5]
    )
