Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)

with DAG(Schedule = Schedule):
    dataLatLongPoint_csv_1 = SourceTask(
        task_id = "dataLatLongPoint_csv_1", 
        component = "OrchestrationSource", 
        kind = "S3Source", 
        connector = Connection(kind = "s3", id = "s3"), 
        format = CSVFormat(
          allowLazyQuotes = False, 
          allowEmptyColumnNames = True, 
          description = "Distance comparison data between cities, aiding in geographical analysis and route optimization.", 
          separator = ",", 
          nullValue = "", 
          schema = {
            "providerType": "Arrow", 
            "fields": [{
                          "name": "seq", 
                          "dataType": {"type" : "int64"}, 
                          "description": "A unique sequence number for each record in the dataset"
                        },                         {
                          "name": "from_city", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The city from which the distance measurement starts"
                        },                         {
                          "name": "to_city", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "The destination city for the route"
                        },                         {
                          "name": "from_wkt", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Well-Known Text representation of the starting location"
                        },                         {
                          "name": "to_wkt", 
                          "dataType": {"type" : "utf8"}, 
                          "description": "Well-known text representation of the destination city"
                        },                         {
                          "name": "Alteryx_Distance_KM", 
                          "dataType": {"type" : "float64"}, 
                          "description": "Distance between two cities calculated using Alteryx in kilometers"
                        },                         {
                          "name": "Formula_Distance_KM", 
                          "dataType": {"type" : "float64"}, 
                          "description": "Calculated distance between two cities based on a specific formula"
                        },                         {
                          "name": "Difference_Alteryx_KM_2", 
                          "dataType": {"type" : "float64"}, 
                          "description": "The difference in distance calculated by Alteryx compared to another method."
                        },                         {
                          "name": "h3_approx_distance", 
                          "dataType": {"type" : "float64"}, 
                          "description": "Approximate distance calculated using H3 indexing method."
                        },                         {
                          "name": "Difference_Alteryx_KM", 
                          "dataType": {"type" : "float64"}, 
                          "description": "The difference in distance calculated by Alteryx compared to another method."
                        }]
          }, 
          additionalProperties = {"copilot" : {"datasetDescriptionStatus" : "fromCopilot"}}, 
          header = True
        ), 
        filePath = "/datasets/orchestration_datasets/csv/arun/dataLatLongPoint.csv"
    )
    model_latlog_test2_single_point_1_2 = Task(
        task_id = "model_latlog_test2_single_point_1_2", 
        component = "Model", 
        modelName = "model_latlog_test2_single_point_1_2"
    )
    create_point_gem_seed_2 = Task(
        task_id = "create_point_gem_seed_2", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
    )
    model_latlog_test2_single_point_1 = Task(
        task_id = "model_latlog_test2_single_point_1", 
        component = "Model", 
        modelName = "model_latlog_test2_single_point_1"
    )
    seedtest2 = Task(
        task_id = "seedtest2", 
        component = "Dataset", 
        table = {"name" : "seedtest2", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    model_latlog_test2_single_point_1_1 = Task(
        task_id = "model_latlog_test2_single_point_1_1", 
        component = "Model", 
        modelName = "model_latlog_test2_single_point_1_1"
    )
    create_point_gem_seed_1 = Task(
        task_id = "create_point_gem_seed_1", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
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
    test_seed = Task(
        task_id = "test_seed", 
        component = "Dataset", 
        table = {"name" : "test_seed", "sourceType" : "Seed"}, 
        writeOptions = {"writeMode" : "overwrite"}
    )
    dataLatLong_csv_1 = Task(
        task_id = "dataLatLong_csv_1", 
        component = "Dataset", 
        table = {
          "name": "prophecy_tmp__mbz0tvui__latlog_test2__dataLatLong_csv_1", 
          "sourceType": "Source", 
          "sourceName": "prophecy_tmp_source__latlog_test2", 
          "alias": ""
        }
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
    city_distance_analysis_csv = Task(
        task_id = "city_distance_analysis_csv", 
        component = "OrchestrationTarget", 
        kind = "S3Target", 
        connector = Connection(kind = "s3", id = "s3"), 
        properties = {
          "filePath": {
            "type": "concat_operation", 
            "properties": {
              "elements": [{
                              "type": "literal", 
                              "properties": {"value" : "/datasets/orchestration_datasets/csv/arun/dataLatLongPoint.csv"}
                            }]
            }
          }
        }, 
        format = {
          "properties": {
            "allowLazyQuotes": False, 
            "allowEmptyColumnNames": True, 
            "separator": ",", 
            "nullValue": "null", 
            "additionalProperties": {"copilot" : {"datasetDescriptionStatus" : "fromUser"}}, 
            "header": True
          }, 
          "kind": "csv", 
          "category": "file"
        }, 
        isNew = False
    )
    model_latlog_test2_single_point_1_3 = Task(
        task_id = "model_latlog_test2_single_point_1_3", 
        component = "Model", 
        modelName = "model_latlog_test2_single_point_1_3"
    )
    test_new_seed_with_date = Task(
        task_id = "test_new_seed_with_date", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "test_new_seed_with_date", "sourceType" : "Seed", "alias" : ""}
    )
    model_latlog_test2_create_point_1_1 = Task(
        task_id = "model_latlog_test2_create_point_1_1", 
        component = "Model", 
        modelName = "model_latlog_test2_create_point_1_1"
    )
    create_point_gem_seed_3 = Task(
        task_id = "create_point_gem_seed_3", 
        component = "Dataset", 
        writeOptions = {"writeMode" : "overwrite"}, 
        table = {"name" : "create_point_gem_seed", "sourceType" : "Table", "sourceName" : "sony.orch_test", "alias" : ""}
    )
    test_new_seed_with_date.out >> model_latlog_test2_single_point_1_3.in_0
    dataLatLongPoint_csv_1.out0 >> seedtest2.in0
    test_seed.out >> model_latlog_test2_single_point_1_1.in_0
    (
        model_latlog_test2_create_point_1_1.out_0
        >> [city_distance_analysis_csv.in0, model_latlog_test2_single_point_1_2.in_0]
    )
    create_point_gem_seed_1.out >> create_point_gem_seed_2.in0
    dataLatLong_csv_1.out0 >> dataLatLong_csv_1.input_port_0_1
    create_point_gem_seed_3.out >> model_latlog_test2_single_point_1.in_0
    dataLatLong_csv_1.output_port_0_1 >> model_latlog_test2_create_point_1_1.in_0
