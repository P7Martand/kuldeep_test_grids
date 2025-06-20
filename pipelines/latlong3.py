Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    test_seed = Task(
        task_id = "test_seed", 
        component = "Dataset", 
        table = {"name" : "test_seed", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    create_point_gem_seed_3 = Task(
        task_id = "create_point_gem_seed_3", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
    )
    create_point_gem_seed_1 = Task(
        task_id = "create_point_gem_seed_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
    )
    create_point_gem_seed_2 = Task(
        task_id = "create_point_gem_seed_2", 
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
    dataLatLong_csv_1 = SourceTask(
        task_id = "dataLatLong_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          separator = ",", 
          nullValue = "", 
          schema = {
            "fields": [{"name" : "seq", "dataType" : {"type" : "int64"}},                         {"name" : "from_city", "dataType" : {"type" : "utf8"}},                         {"name" : "to_city", "dataType" : {"type" : "utf8"}},                         {"name" : "from_lat", "dataType" : {"type" : "float64"}},                         {"name" : "from_lon", "dataType" : {"type" : "float64"}},                         {"name" : "to_lat", "dataType" : {"type" : "float64"}},                         {"name" : "to_lon", "dataType" : {"type" : "float64"}},                         {"name" : "Alteryx_Distance_KM", "dataType" : {"type" : "float64"}},                         {"name" : "Formula_Distance_KM", "dataType" : {"type" : "float64"}},                         {"name" : "Difference_Alteryx_KM_2", "dataType" : {"type" : "float64"}},                         {"name" : "h3_approx_distance", "dataType" : {"type" : "float64"}},                         {"name" : "Difference_Alteryx_KM", "dataType" : {"type" : "float64"}}], 
            "providerType": "arrow"
          }, 
          header = True
        ), 
        filePath = "/datasets/orchestration_datasets/csv/arun/dataLatLong.csv"
    )
    ashtest = Task(
        task_id = "ashtest", 
        component = "Dataset", 
        table = {
          "name": "ashtest", 
          "sourceType": "Table", 
          "sourceName": "qa_team.qa_database", 
          "alias": "", 
          "additionalProperties": None
        }, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    model_latlong3_single_point_1 = Task(
        task_id = "model_latlong3_single_point_1", 
        component = "Model", 
        modelName = "model_latlong3_single_point_1"
    )
    dataLatLong_csv_1 = Task(
        task_id = "dataLatLong_csv_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy_tmp__mbrjvs6c__latlong3__dataLatLong_csv_1", 
          "sourceType": "Source", 
          "sourceName": "prophecy_tmp_source__latlong3", 
          "alias": ""
        }
    )
    model_latlong3_single_point_1_1 = Task(
        task_id = "model_latlong3_single_point_1_1", 
        component = "Model", 
        modelName = "model_latlong3_single_point_1_1"
    )
    model_latlong3_single_point_1_2 = Task(
        task_id = "model_latlong3_single_point_1_2", 
        component = "Model", 
        modelName = "model_latlong3_single_point_1_2"
    )
    model_latlong3_single_point_1_3 = Task(
        task_id = "model_latlong3_single_point_1_3", 
        component = "Model", 
        modelName = "model_latlong3_single_point_1_3"
    )
    dataLatLong_csv_1.out0 >> dataLatLong_csv_1.input_port_0_1
    test_new_seed_with_date.out >> model_latlong3_single_point_1_3.in_0
    create_point_gem_seed_3.out >> model_latlong3_single_point_1.in_0
    test_seed.out >> model_latlong3_single_point_1_1.in_0
    dataLatLong_csv_1.output_port_0_1 >> model_latlong3_single_point_1_2.in_0
    create_point_gem_seed_1.out >> create_point_gem_seed_2.in0
