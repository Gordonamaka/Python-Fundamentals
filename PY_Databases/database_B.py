# Database Design

"""
Database design is an art form of its own with particular skills and experience.

Our goal is to avoid the really bad mistakes and design clean and easily understood databases

Others may performance turn things later

Database design starts with a picture

Basic Rule: Never put the same string data in twice - use a relationship instead.
"""

# Database Normalization (3NF)
"""
Do not replicate data - reference data - point at data
Use integers for keys and for references
Add a special 'key' column to each table which we will make references to. By convention, many programmers call this column 'id'
-
Primary key - Generally an integer auto-increment field
Logical key - What the outside world uses for lookup
Foreign Key - Generally an integer key pointing to a row in another table
-
Best Practices :
Never use your logical key as the primary key

Logical keys can and do change, albeit slowly

Relationships that are based on matching string feilds are less efficient than integers
"""

# Relational Databases: Join Operation

# select Album.title, Artist.name FROM Album join Artist on Album.artist_id = Artist.id

#   What we want to see ||    The tables that hold the data || How the tables are linked

# Joining two tables without an ON Clause gives all possible combinations of rows.