from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col


def main():
    spark = SparkSession.builder \
        .appName("ContadorPalabras") \
        .getOrCreate()
    # data mock
    data = [("loro loro", "lg apple"),
            ("gato perro", "hp lg"),
            ("perro mono", "nike riot")]
    column = ["animal", "marca"]
    # df creation
    animal_df = spark.createDataFrame(data, column)
    # df iteration
    palabra_df = None
    for c in column:
        print(f"columna: {c}")
        temp_df = animal_df.select(explode(split(col(c), " ")).alias("palabra"))
        if palabra_df == None:
            palabra_df = temp_df
        else:
            palabra_df = palabra_df.union(temp_df)
    # total words
    total_df = palabra_df.groupBy("palabra").count()
    total_df.show
    spark.stop()

if __name__ == "__main__":
    main()