Config = {"parameter1" : "'10'", "b" : "'bvalue'"}
Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Config = Config, Schedule = Schedule):
    airport = Task(
        task_id = "airport", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "airport", "sourceType" : "Seed", "alias" : ""}
    )
    data_csv_1 = SourceTask(
        task_id = "data_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(allowLazyQuotes = False, allowEmptyColumnNames = True, separator = ",", nullValue = "", header = True), 
        filePath = "/avpreetTest/data.csv"
    )
    csv_all_type_dataset_normal_colnames_csv_1 = SourceTask(
        task_id = "csv_all_type_dataset_normal_colnames_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(allowLazyQuotes = False, allowEmptyColumnNames = True, separator = ",", nullValue = "", header = True), 
        filePath = "/orch_dataset/csv_data/csv_all_type_dataset_normal_colnames.csv"
    )
    test_seed_1 = Task(
        task_id = "test_seed_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_seed", "sourceType" : "Seed", "alias" : ""}
    )
    test_seed = Task(
        task_id = "test_seed", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_seed", "sourceType" : "Seed", "alias" : ""}
    )
    create_point_gem_seed = Task(
        task_id = "create_point_gem_seed", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Seed", "alias" : ""}
    )
    asda = Task(
        task_id = "asda", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "asda", "sourceType" : "Table", "sourceName" : "Q.asd", "alias" : ""}
    )
    test_new_seed_with_date_1 = Task(
        task_id = "test_new_seed_with_date_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_new_seed_with_date", "sourceType" : "Seed", "alias" : ""}
    )
    raw_test2 = Task(
        task_id = "raw_test2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "raw_test2", "sourceType" : "Seed", "alias" : ""}
    )
    route_data = Task(
        task_id = "route_data", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "route_data", "sourceType" : "Seed", "alias" : ""}
    )
    ashtest = Task(
        task_id = "ashtest", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "ashtest", "sourceType" : "Table", "sourceName" : "qa_team.qa_database", "alias" : ""}
    )
    create_point_gem_seed_1 = Task(
        task_id = "create_point_gem_seed_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
    )
    test_new_seed_with_date = Task(
        task_id = "test_new_seed_with_date", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_new_seed_with_date", "sourceType" : "Seed", "alias" : ""}
    )
    all_type_csv_csv_1 = SourceTask(
        task_id = "all_type_csv_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(allowLazyQuotes = False, allowEmptyColumnNames = True, separator = ",", nullValue = "", header = True), 
        filePath = "/orch_dataset/csv_data/all_type_csv.csv"
    )
    seedtest2 = Task(
        task_id = "seedtest2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "seedtest2", "sourceType" : "Seed", "alias" : ""}
    )
    city_data = Task(
        task_id = "city_data", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "city_data", "sourceType" : "Seed", "alias" : ""}
    )
    s1 = Task(
        task_id = "s1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "s1", "sourceType" : "Seed", "alias" : ""}
    )
