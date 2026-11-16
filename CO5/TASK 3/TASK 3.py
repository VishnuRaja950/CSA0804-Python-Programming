
import csv
import sqlite3
import time
import cProfile
import pstats
import random
import os
from datetime import datetime, timedelta
from collections import defaultdict

# Generate air-quality data
def generate_data(station_count, filename, database):
    random.seed(42)

    start_date = datetime(2026, 1, 1)
    total_hours = 365 * 24

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS air_quality (
            station TEXT,
            date_time TEXT,
            pm25 REAL
        )
    """)

    cursor.execute("DELETE FROM air_quality")

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Station", "Date_Time", "PM2.5"])

        records = []

        for station_number in range(1, station_count + 1):
            station_name = f"Station_{station_number}"

            for hour in range(total_hours):
                date_time = start_date + timedelta(hours=hour)
                pm25 = round(random.uniform(10, 150), 2)

                row = (
                    station_name,
                    date_time.strftime("%Y-%m-%d %H:%M:%S"),
                    pm25
                )

                writer.writerow(row)
                records.append(row)

                if len(records) >= 10000:
                    cursor.executemany(
                        "INSERT INTO air_quality VALUES (?, ?, ?)",
                        records
                    )
                    records.clear()

        if records:
            cursor.executemany(
                "INSERT INTO air_quality VALUES (?, ?, ?)",
                records
            )

    connection.commit()
    connection.close()


# Method 1: Python CSV processing without Pandas
def python_method(filename):
    totals = defaultdict(float)
    counts = defaultdict(int)

    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            station = row["Station"]
            value = float(row["PM2.5"])

            totals[station] += value
            counts[station] += 1

    averages = {}

    for station in totals:
        averages[station] = totals[station] / counts[station]

    return averages


# Method 2: SQLite database processing
def sql_method(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT station, AVG(pm25)
        FROM air_quality
        GROUP BY station
    """)

    results = dict(cursor.fetchall())

    connection.close()
    return results


# Performance testing
def performance_test(station_count):
    filename = "air_quality_data.csv"
    database = "air_quality.db"

    print("\nGenerating data for", station_count, "stations...")

    generate_data(station_count, filename, database)

    # Test Python processing
    start = time.perf_counter()
    python_results = python_method(filename)
    python_time = time.perf_counter() - start

    # Test SQL processing
    start = time.perf_counter()
    sql_results = sql_method(database)
    sql_time = time.perf_counter() - start

    # Verify both methods produce matching results
    assert python_results.keys() == sql_results.keys()

    for station in python_results:
        assert abs(
            python_results[station] - sql_results[station]
        ) < 0.000001

    print("Number of stations:", station_count)
    print("Records processed:", station_count * 8760)
    print("Python processing time:", round(python_time, 4), "seconds")
    print("SQL processing time:", round(sql_time, 4), "seconds")
    print("Results verified: Both methods match")


# Main program
if __name__ == "__main__":

    print("CITY AIR-QUALITY MONITORING NETWORK")
    print("TASK 3 - PERFORMANCE ANALYSIS")
    print("----------------------------------")

    for stations in [1, 12, 120]:
        performance_test(stations)

    # Profiling Python processing
    print("\nPROFILING PYTHON PROCESSING")

    profiler = cProfile.Profile()
    profiler.enable()

    python_method("air_quality_data.csv")

    profiler.disable()

    stats = pstats.Stats(profiler)
    stats.sort_stats("cumulative")
    stats.print_stats(10)

    print("\nTask 3 completed successfully.")
