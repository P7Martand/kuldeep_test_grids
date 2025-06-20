Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    model_latlog_single_point = Task(
        task_id = "model_latlog_single_point", 
        component = "Model", 
        modelName = "model_latlog_single_point"
    )
    raw_points = Task(
        task_id = "raw_points", 
        component = "Dataset", 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    model_latlog_charts = Task(task_id = "model_latlog_charts", component = "Model", modelName = "model_latlog_charts")
    model_latlog_create_point = Task(
        task_id = "model_latlog_create_point", 
        component = "Model", 
        modelName = "model_latlog_create_point"
    )
    model_latlog_points = Task(task_id = "model_latlog_points", component = "Model", modelName = "model_latlog_points")
    model_latlog_distance_comparison = Task(
        task_id = "model_latlog_distance_comparison", 
        component = "Model", 
        modelName = "model_latlog_distance_comparison"
    )
    raw_points.out >> model_latlog_create_point.in_0
    (
        model_latlog_create_point.out_0
        >> [model_latlog_charts.in_0, model_latlog_distance_comparison.in_0, model_latlog_points.in_0]
    )
    model_latlog_points.out_0 >> [model_latlog_single_point.in_0, model_latlog_distance_comparison.in_0]
