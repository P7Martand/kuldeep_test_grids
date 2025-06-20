Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    map_1 = Task(
        task_id = "map_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "map", "sourceType" : "Seed", "alias" : ""}
    )
    airport = Task(
        task_id = "airport", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "airport", "sourceType" : "Seed", "alias" : ""}
    )
    test_new_seed_with_date = Task(
        task_id = "test_new_seed_with_date", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_new_seed_with_date", "sourceType" : "Seed", "alias" : ""}
    )
    candlestick_data = Task(
        task_id = "candlestick_data", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "candlestick_data", "sourceType" : "Seed", "alias" : ""}
    )
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
    city_data = Task(
        task_id = "city_data", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "city_data", "sourceType" : "Seed", "alias" : ""}
    )
    test_seed = Task(
        task_id = "test_seed", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_seed", "sourceType" : "Seed", "alias" : ""}
    )
    ashtest = Task(
        task_id = "ashtest", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "ashtest", "sourceType" : "Table", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    route_data = Task(
        task_id = "route_data", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "route_data", "sourceType" : "Seed", "alias" : ""}
    )
    map = Task(
        task_id = "map", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "map", "sourceType" : "Seed", "alias" : ""}
    )
    create_point_gem_seed = Task(
        task_id = "create_point_gem_seed", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Seed", "alias" : ""}
    )
    raw_test2 = Task(
        task_id = "raw_test2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_test2", "sourceType" : "Seed", "alias" : ""}
    )
