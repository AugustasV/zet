# Wide-Column Database
* Names and format of columns can vary accross rows, tables.
* Flexible, could be geo-distributed.
* Fast.
* Highly scalable.
It's pretty stable and works properly on distributed systems. Data could be stored in seperate nodes. There is small chance that data could be lost in case of one node would be gone, because data is written on all nodes at once, without waiting report of sucessful write.
# Difference between Wide-Column and key Value Store database
Key value store database is pretty simple, just `Key` and `Value`.
Wide-column databases key-value store could be across multiple columns.
# Use cases
* Log Data
* IoT
* Time-series
* Real-time analytics
# Databases example
Apache Cassandra
Scylla

---
Source [Wide column database](https://blog.logrocket.com/nosql-wide-column-stores-demystified/)
