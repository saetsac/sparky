import pyspark\nprint(pyspark.SparkContext().parallelize(range(0, 10)).count())
