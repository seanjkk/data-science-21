# SQL CRUD

## Part 1: Restaurant Finder

### Tables

```sql
--- Creating table for restaurants
CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price_tier TEXT,
    neighborhood TEXT,
    opening_hours TIME,
    rating INTEGER,
    kid_friendly BOOLEAN NOT NULL
);

--- Creating table for reviews
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY,
    restaurant_id INTEGER,
    name TEXT,
    review TEXT
);
```

### Mock Data

Mock data is [`here`](data/restaurants.csv)

```sql
--- Importing csv data
.mode csv

CREATE TABLE temp_table (
    id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price_tier TEXT,
    neighborhood TEXT,
    opening_hours TIME,
    rating INTEGER,
    kid_friendly BOOLEAN NOT NULL
);

.import data/restaurants.csv temp_table --skip 1

INSERT INTO restaurants SELECT * FROM temp_table;

DROP TABLE temp_table;
```

### Queries

1. All cheap restaurants in a particular neighborhood
```sql
SELECT name 
FROM restaurants 
WHERE price_tier="cheap" 
    AND neighborhood="manhattan";
```

2. All Thai restaurants with 3 stars or more, ordered by number of stars in descending order
```sql
SELECT name 
FROM restaurants 
WHERE category="thai" 
    AND rating>2 
ORDER BY rating DESC;
```

3. Find all restaurants that are open now
```sql
--- I assume all the restaurants open at 10:00 AM
--- opening_hours contains the time for when the restaurant closes

SELECT name 
FROM restaurants 
WHERE opening_hours>=strftime('%H:%M', 'now') 
    AND strftime('%H:%M', 'now')>=10:00;
```


4. Delete all restaurants that are not good for kids
```sql
DELETE FROM restaurants 
WHERE kid_friendly=0;
```

5. Find number of restaurants in each NYC neighborhood
```sql
SELECT neighborhood, COUNT(id) 
FROM restaurants 
GROUP BY neighborhood;
```

## Part 2: Social Media App

### Tables
```sql
--- Creating table for users
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email TEXT,
    username TEXT,
    password TEXT
);

--- Creating table for posts
CREATE TABLE posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    recipient_id INTEGER,
    post TEXT,
    is_message BOOLEAN,
    post_time DATETIME,
    is_visible BOOLEAN
);
```

### Mock Data

Mock data for users is [`here`](data/users.csv) and mock data for posts is [`here`](data/posts.csv)

```sql
--- Importing csv data
.mode csv

CREATE TABLE temp_users (
    id INTEGER PRIMARY KEY,
    email TEXT,
    username TEXT,
    password TEXT
);

.import data/users.csv temp_users --skip 1

INSERT INTO users SELECT * FROM temp_users;

DROP TABLE temp_users;

CREATE TABLE temp_posts (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    recipient_id INTEGER,
    post TEXT,
    is_message BOOLEAN,
    post_time DATETIME,
    is_visible BOOLEAN
);

.import data/posts.csv temp_posts --skip 1

INSERT INTO posts SELECT * FROM temp_posts;

DROP TABLE temp_posts;

```

### Queries

1. Register a new user
```sql
INSERT INTO users (
    id,
    email,
    username,
    password
)
VALUES (
    1001,
    "sample_email@gmail.com",
    "sample_username",
    "sample_password"
);
```

2. Create a message from user to another user
```sql
INSERT INTO posts(
    id,
    user_id,
    recipient_id,
    post,
    is_message,
    post_time,
    is_visible
)
VALUES(
    2001,
    1,
    2,
    "Hello",
    TRUE,
    strftime('%m%d%Y %H:%M', 'now'),
    TRUE
);
```

3. Create a story from user
```sql
INSERT INTO posts(
    id,
    user_id,
    recipient_id,
    post,
    is_message,
    post_time,
    is_visible
)
VALUES(
    2002,
    1,
    ,
    "Hello everyone",
    FALSE,
    strftime('%m%d%Y %H:%M', 'now'),
    TRUE
);
```

4. Show 10 most recent visible messages and stories, in order of recency
```sql
SELECT post 
FROM posts 
WHERE is_visible=TRUE 
ORDER BY post_time DESC
LIMIT 10 ;
```

5. Show 10 most recent messages sent by particular user to particular user, in order of recency
```sql
SELECT post 
FROM posts 
WHERE user_id = 1 
    AND recipient_id = 2 
ORDER BY post_time DESC
LIMIT 10;
```

6. Make all stories that are more than 24 hours old invisible
```sql
UPDATE posts 
SET is_visible=FALSE 
WHERE datediff(hour, post_time, strftime('%m%d%Y %H:%M', 'now'))>24 
    AND is_message=FALSE;
```

7. Show all invisible messages and stories, in order of recency
```sql
SELECT post 
FROM posts 
WHERE is_visible=FALSE 
ORDER BY post_time DESC;
```

8. Show the number of posts by each user
```sql
SELECT user_id, COUNT(post) 
FROM posts 
GROUP BY user_id;
```

9. Show the post text and email address of all posts and the user who made them within the last 24 hours
```sql
SELECT posts.post, users.email, users.username 
FROM posts 
INNER JOIN users 
    ON posts.user_id=users.id 
WHERE datediff(hour, posts.post_time, strftime('%m%d%Y %H:%M', 'now'))<24;
```

10. Show the email addresses of all users who have not posted anything yet
```sql
SELECT users.email 
FROM posts 
LEFT JOIN users 
    ON posts.user_id=users.id 
WHERE COUNT(post)=0;
```
