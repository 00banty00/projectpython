def create_spark_session():
    """
    Create SparkSession with standard configurations
    :return: SparkSession object
    """

    # Create SparkSession object with desired configurations
    # Adding enable hive support libary in spark function
    spark = (SparkSession.builder.config("spark.databricks.hive.metastore.glueCatalog.enabled", "true")
             .config("spark.sql.hive.convertMetastoreParquet", "false")
             .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2")
             .config("spark.speculation", "false")
             .enableHiveSupport()
             .getOrCreate()
             )

    # Update environment name
    # Note: using spark.bucketname.env to pass the environment so that emr_spark_step_function does not break
    S3PathResolver.environment = spark.sparkContext.getConf().get("spark.bucketname.env")
    # Update publication directory name
    S3PathResolver.publication = spark.sparkContext.getConf().get("spark.publication.env")

    return spark

    