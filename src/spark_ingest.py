from pyspark.sql import SparkSession
from pyspark.sql.functions import input_file_name, lit
import os

def load_documents(input_dir="data/sample_docs"):
    spark = SparkSession.builder \
        .appName("SparkGPT-DocumentIngestion") \
        .getOrCreate()

    pdfs = spark.read.format("binaryFile").load(f"{input_dir}/*.pdf")
    txts = spark.read.text(f"{input_dir}/*.txt")
    mds = spark.read.text(f"{input_dir}/*.md")

    docs = pdfs.select(lit("pdf").alias("type"), input_file_name().alias("path")) \
        .union(txts.select(lit("text"), input_file_name().alias("path"))) \
        .union(mds.select(lit("markdown"), input_file_name().alias("path")))

    docs.write.mode("overwrite").format("delta").save("data/processed_docs")
    print("✅ Documents processed and saved to Delta format")
    spark.stop()
    return "data/processed_docs"

if __name__ == "__main__":
    load_documents()
