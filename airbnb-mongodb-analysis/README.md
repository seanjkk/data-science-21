# AirBnB MongoDB Analysis

## Part 1: Data Selection and Cleaning

### Data Set Details

The data set I chose for this analysis was Airbnb data for Tokyo, Japan. The data set is from Inside Airbnb and can be found [here](http://insideairbnb.com/get-the-data.html) in CSV format.

Here is a preview of the first 3 rows:

| id | listing_url | scrape_id | last_scraped | name | description | neighborhood_overview | picture_url | host_id | host_url | host_name | host_since | host_location | host_about | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url | host_picture_url | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications | host_has_profile_pic | host_identity_verified | neighbourhood | neighbourhood_cleansed | neighbourhood_group_cleansed | latitude | longitude | property_type | room_type | accommodates | bathrooms | bathrooms_text | bedrooms | beds | amenities | price | minimum_nights | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 197677 | https://www.airbnb.com/rooms/197677 | 2.02E+13 | ######## | Oshiage Holiday Apartment | ... |  | https://a0.muscache.com/pictures/38437056/d27fa43f_original.jpg | 964081 | https://www.airbnb.com/users/show/964081 | Yoshimi & Marek | ######## | Tokyo | Would love to travel all over the world and meet and feel the different   people and cultures. | within a day | 100% | 100% | f | https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_small | https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_x_medium | Sumida District | 1 | 1 | ['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id'] | t | f |  | Sumida Ku |  | 35.71707 | 139.8261 | Entire rental unit | Entire home/apt | 4 |  | 1 bath | 1 | 2 | ["Shampoo", "Kitchen", "Essentials",   "Microwave", "Washer", "Wifi", "Dishes and   silverware", "Air conditioning", "Iron",   "Dedicated workspace", "Hair dryer", "Long term   stays allowed", "Dryer", "Hangers", "Smoke   alarm", "Carbon monoxide alarm", "Lockbox",   "Fire extinguisher", "Heating", "Hot water",   "TV"] | ######## | 3 | 365 | 3 | 3 | 365 | 365 | 3 | 365 |  | t | 28 | 58 | 88 | 363 | ######## | 165 | 0 | 0 | ######## | ######## | 4.76 | 4.73 | 4.91 | 4.83 | 4.82 | 4.51 | 4.78 | M130003350 | f | 1 | 1 | 0 | 0 | 1.49 |


### Data Cleaning

I cleaned the data using the Pandas module in Python. Looking at the CSV file, I noticed there were columns that were completely, or almost all blank. I decided to remove these columns. I then removed all rows with NaN values. I used the CSV module to import this data into a new file called listings_clean.csv.

```py
import csv
import pandas as pd

df = pd.read_csv("data/listings.csv")

# Dropping columns that are empty/mostly empty or might cause errors
drop_columns = ['description', 'neighborhood_overview', 'host_url', 'host_about', 'host_response_time', 'host_response_rate', 'host_acceptance_rate', 'neighbourhood', 'neighbourhood_group_cleansed', 'bathrooms', 'calendar_updated']

df = df.drop(drop_columns, axis=1)

# Dropping rows with null values
df = df.dropna()

df.to_csv(r"data/listings_clean.csv", index = False, encoding="utf-8")
```

## Part 2: MongoDB Analysis

1. Show exactly two documents from the listings collection in any order

```
db.listings.find().limit(2)
```
I use find and set limit to 2. Because this shows all fields, the result is very long.

Here is the result:
>{ "_id" : ObjectId("6196c56b051c47f3e6955c8a"), "id" : 197677, "listing_url" : "https://www.airbnb.com/rooms/197677", "scrape_id" : NumberLong("20211028222535"), "last_scraped" : "2021-10-29", "name" : "Oshiage Holiday Apartment", "picture_url" : "https://a0.muscache.com/pictures/38437056/d27fa43f_original.jpg", "host_id" : 964081, "host_name" : "Yoshimi & Marek", "host_since" : "2011-08-13", "host_location" : "Tokyo", "host_is_superhost" : "f", "host_thumbnail_url" : "https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Sumida District", "host_listings_count" : 1, "host_total_listings_count" : 1, "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id']", "host_has_profile_pic" : "t", "host_identity_verified" : "f", "neighbourhood_cleansed" : "Sumida Ku", "latitude" : 35.71707, "longitude" : 139.82608, "property_type" : "Entire rental unit", "room_type" : "Entire home/apt", "accommodates" : 4, "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 2, "amenities" : "[\"Shampoo\", \"Kitchen\", \"Essentials\", \"Microwave\", \"Washer\", \"Wifi\", \"Dishes and silverware\", \"Air conditioning\", \"Iron\", \"Dedicated workspace\", \"Hair dryer\", \"Long term stays allowed\", \"Dryer\", \"Hangers\", \"Smoke alarm\", \"Carbon monoxide alarm\", \"Lockbox\", \"Fire extinguisher\", \"Heating\", \"Hot water\", \"TV\"]", "price" : "$11,000.00", "minimum_nights" : 3, "maximum_nights" : 365, "minimum_minimum_nights" : 3, "maximum_minimum_nights" : 3, "minimum_maximum_nights" : 365, "maximum_maximum_nights" : 365, "minimum_nights_avg_ntm" : 3, "maximum_nights_avg_ntm" : 365, "has_availability" : "t", "availability_30" : 28, "availability_60" : 58, "availability_90" : 88, "availability_365" : 363, "calendar_last_scraped" : "2021-10-29", "number_of_reviews" : 165, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "2012-09-25", "last_review" : "2019-11-14", "review_scores_rating" : 4.76, "review_scores_accuracy" : 4.73, "review_scores_cleanliness" : 4.91, "review_scores_checkin" : 4.83, "review_scores_communication" : 4.82, "review_scores_location" : 4.51, "review_scores_value" : 4.78, "license" : "M130003350", "instant_bookable" : "f", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 1, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 1.49 }
{ "_id" : ObjectId("6196c56b051c47f3e6955c8b"), "id" : 776070, "listing_url" : "https://www.airbnb.com/rooms/776070", "scrape_id" : NumberLong("20211028222535"), "last_scraped" : "2021-10-29", "name" : "Kero-kero house room 1", "picture_url" : "https://a0.muscache.com/pictures/efd9f039-dbd2-4996-9467-7742a0c0813b.jpg", "host_id" : 801494, "host_name" : "Kei", "host_since" : "2011-07-10", "host_location" : "Japan", "host_is_superhost" : "t", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/ba6d4f6d-7784-4101-a15c-1ffe99ccc92b.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/ba6d4f6d-7784-4101-a15c-1ffe99ccc92b.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Kita District", "host_listings_count" : 1, "host_total_listings_count" : 1, "host_verifications" : "['email', 'phone', 'manual_online', 'reviews', 'manual_offline', 'jumio', 'offline_government_id', 'selfie', 'government_id', 'identity_manual']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood_cleansed" : "Kita Ku", "latitude" : 35.73844, "longitude" : 139.76917, "property_type" : "Private room in residential home", "room_type" : "Private room", "accommodates" : 2, "bathrooms_text" : "1 shared bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Air conditioning\", \"Shampoo\", \"Iron\", \"Ethernet connection\", \"Hot water\", \"First aid kit\", \"Hair dryer\", \"Essentials\", \"Microwave\", \"Private entrance\", \"Heating\", \"Refrigerator\", \"Hangers\", \"Extra pillows and blankets\", \"Cable TV\", \"Bed linens\", \"TV with standard cable\", \"Smoke alarm\", \"Wifi\", \"Dishes and silverware\"]", "price" : "$7,950.00", "minimum_nights" : 3, "maximum_nights" : 14, "minimum_minimum_nights" : 3, "maximum_minimum_nights" : 3, "minimum_maximum_nights" : 14, "maximum_maximum_nights" : 14, "minimum_nights_avg_ntm" : 3, "maximum_nights_avg_ntm" : 14, "has_availability" : "t", "availability_30" : 27, "availability_60" : 48, "availability_90" : 65, "availability_365" : 245, "calendar_last_scraped" : "2021-10-29", "number_of_reviews" : 228, "number_of_reviews_ltm" : 0, "number_of_reviews_l30d" : 0, "first_review" : "2013-09-17", "last_review" : "2020-01-18", "review_scores_rating" : 4.97, "review_scores_accuracy" : 4.96, "review_scores_cleanliness" : 4.92, "review_scores_checkin" : 4.97, "review_scores_communication" : 4.97, "review_scores_location" : 4.84, "review_scores_value" : 4.91, "license" : "M130000243", "instant_bookable" : "t", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 0, "calculated_host_listings_count_private_rooms" : 1, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 2.31 }

2. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.

```
db.listings.find().limit(10).pretty()
```
I set the limit to 10, and use the pretty() function. Please note that I did not know how to retain the formatting in markdown, and hence the formatting is different.

First three results:
>{
        "_id" : ObjectId("6196c56b051c47f3e6955c8a"),
        "id" : 197677,
        "listing_url" : "https://www.airbnb.com/rooms/197677",
        "scrape_id" : NumberLong("20211028222535"),
        "last_scraped" : "2021-10-29",
        "name" : "Oshiage Holiday Apartment",
        "picture_url" : "https://a0.muscache.com/pictures/38437056/d27fa43f_original.jpg",
        "host_id" : 964081,
        "host_name" : "Yoshimi & Marek",
        "host_since" : "2011-08-13",
        "host_location" : "Tokyo",
        "host_is_superhost" : "f",
        "host_thumbnail_url" : "https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/users/964081/profile_pic/1319512318/original.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Sumida District",
        "host_listings_count" : 1,
        "host_total_listings_count" : 1,
        "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'jumio', 'government_id']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "f",
        "neighbourhood_cleansed" : "Sumida Ku",
        "latitude" : 35.71707,
        "longitude" : 139.82608,
        "property_type" : "Entire rental unit",
        "room_type" : "Entire home/apt",
        "accommodates" : 4,
        "bathrooms_text" : "1 bath",
        "bedrooms" : 1,
        "beds" : 2,
        "amenities" : "[\"Shampoo\", \"Kitchen\", \"Essentials\", \"Microwave\", \"Washer\", \"Wifi\", \"Dishes and silverware\", \"Air conditioning\", \"Iron\", \"Dedicated workspace\", \"Hair dryer\", \"Long term stays allowed\", \"Dryer\", \"Hangers\", \"Smoke alarm\", \"Carbon monoxide alarm\", \"Lockbox\", \"Fire extinguisher\", \"Heating\", \"Hot water\", \"TV\"]",
        "price" : "$11,000.00",
        "minimum_nights" : 3,
        "maximum_nights" : 365,
        "minimum_minimum_nights" : 3,
        "maximum_minimum_nights" : 3,
        "minimum_maximum_nights" : 365,
        "maximum_maximum_nights" : 365,
        "minimum_nights_avg_ntm" : 3,
        "maximum_nights_avg_ntm" : 365,
        "has_availability" : "t",
        "availability_30" : 28,
        "availability_60" : 58,
        "availability_90" : 88,
        "availability_365" : 363,
        "calendar_last_scraped" : "2021-10-29",
        "number_of_reviews" : 165,
        "number_of_reviews_ltm" : 0,
        "number_of_reviews_l30d" : 0,
        "first_review" : "2012-09-25",
        "last_review" : "2019-11-14",
        "review_scores_rating" : 4.76,
        "review_scores_accuracy" : 4.73,
        "review_scores_cleanliness" : 4.91,
        "review_scores_checkin" : 4.83,
        "review_scores_communication" : 4.82,
        "review_scores_location" : 4.51,
        "review_scores_value" : 4.78,
        "license" : "M130003350",
        "instant_bookable" : "f",
        "calculated_host_listings_count" : 1,
        "calculated_host_listings_count_entire_homes" : 1,
        "calculated_host_listings_count_private_rooms" : 0,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 1.49
}
>
>{
        "_id" : ObjectId("6196c56b051c47f3e6955c8b"),
        "id" : 776070,
        "listing_url" : "https://www.airbnb.com/rooms/776070",
        "scrape_id" : NumberLong("20211028222535"),
        "last_scraped" : "2021-10-29",
        "name" : "Kero-kero house room 1",
        "picture_url" : "https://a0.muscache.com/pictures/efd9f039-dbd2-4996-9467-7742a0c0813b.jpg",
        "host_id" : 801494,
        "host_name" : "Kei",
        "host_since" : "2011-07-10",
        "host_location" : "Japan",
        "host_is_superhost" : "t",
        "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/ba6d4f6d-7784-4101-a15c-1ffe99ccc92b.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/pictures/user/ba6d4f6d-7784-4101-a15c-1ffe99ccc92b.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Kita District",
        "host_listings_count" : 1,
        "host_total_listings_count" : 1,
        "host_verifications" : "['email', 'phone', 'manual_online', 'reviews', 'manual_offline', 'jumio', 'offline_government_id', 'selfie', 'government_id', 'identity_manual']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "t",
        "neighbourhood_cleansed" : "Kita Ku",
        "latitude" : 35.73844,
        "longitude" : 139.76917,
        "property_type" : "Private room in residential home",
        "room_type" : "Private room",
        "accommodates" : 2,
        "bathrooms_text" : "1 shared bath",
        "bedrooms" : 1,
        "beds" : 1,
        "amenities" : "[\"Air conditioning\", \"Shampoo\", \"Iron\", \"Ethernet connection\", \"Hot water\", \"First aid kit\", \"Hair dryer\", \"Essentials\", \"Microwave\", \"Private entrance\", \"Heating\", \"Refrigerator\", \"Hangers\", \"Extra pillows and blankets\", \"Cable TV\", \"Bed linens\", \"TV with standard cable\", \"Smoke alarm\", \"Wifi\", \"Dishes and silverware\"]",
        "price" : "$7,950.00",
        "minimum_nights" : 3,
        "maximum_nights" : 14,
        "minimum_minimum_nights" : 3,
        "maximum_minimum_nights" : 3,
        "minimum_maximum_nights" : 14,
        "maximum_maximum_nights" : 14,
        "minimum_nights_avg_ntm" : 3,
        "maximum_nights_avg_ntm" : 14,
        "has_availability" : "t",
        "availability_30" : 27,
        "availability_60" : 48,
        "availability_90" : 65,
        "availability_365" : 245,
        "calendar_last_scraped" : "2021-10-29",
        "number_of_reviews" : 228,
        "number_of_reviews_ltm" : 0,
        "number_of_reviews_l30d" : 0,
        "first_review" : "2013-09-17",
        "last_review" : "2020-01-18",
        "review_scores_rating" : 4.97,
        "review_scores_accuracy" : 4.96,
        "review_scores_cleanliness" : 4.92,
        "review_scores_checkin" : 4.97,
        "review_scores_communication" : 4.97,
        "review_scores_location" : 4.84,
        "review_scores_value" : 4.91,
        "license" : "M130000243",
        "instant_bookable" : "t",
        "calculated_host_listings_count" : 1,
        "calculated_host_listings_count_entire_homes" : 0,
        "calculated_host_listings_count_private_rooms" : 1,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 2.31
}
>
>{
        "_id" : ObjectId("6196c56b051c47f3e6955c8c"),
        "id" : 1196177,
        "listing_url" : "https://www.airbnb.com/rooms/1196177",
        "scrape_id" : NumberLong("20211028222535"),
        "last_scraped" : "2021-10-29",
        "name" : "Stay with host Cozy private room Senju area",
        "picture_url" : "https://a0.muscache.com/pictures/72890882/05ecbdaa_original.jpg",
        "host_id" : 5686404,
        "host_name" : "Yukiko",
        "host_since" : "2013-03-30",
        "host_location" : "Adachi City, Tokyo, Japan",
        "host_is_superhost" : "t",
        "host_thumbnail_url" : "https://a0.muscache.com/im/users/5686404/profile_pic/1365075938/original.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/users/5686404/profile_pic/1365075938/original.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Adachi District",
        "host_listings_count" : 2,
        "host_total_listings_count" : 2,
        "host_verifications" : "['email', 'phone', 'reviews', 'jumio', 'offline_government_id', 'government_id']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "t",
        "neighbourhood_cleansed" : "Adachi Ku",
        "latitude" : 35.74475,
        "longitude" : 139.79731,
        "property_type" : "Private room in residential home",
        "room_type" : "Private room",
        "accommodates" : 2,
        "bathrooms_text" : "1 shared bath",
        "bedrooms" : 1,
        "beds" : 2,
        "amenities" : "[\"Shampoo\", \"Kitchen\", \"Essentials\", \"Luggage dropoff allowed\", \"Children\\u2019s books and toys\", \"Washer\", \"Microwave\", \"Cooking basics\", \"Wifi\", \"Dishes and silverware\", \"Air conditioning\", \"Private entrance\", \"Iron\", \"First aid kit\", \"Dedicated workspace\", \"Hair dryer\", \"Long term stays allowed\", \"Dryer\", \"Hangers\", \"Smoke alarm\", \"Oven\", \"Host greets you\", \"Carbon monoxide alarm\", \"Coffee maker\", \"Fire extinguisher\", \"Heating\", \"Stove\", \"Children\\u2019s dinnerware\", \"Hot water\", \"Refrigerator\", \"Extra pillows and blankets\", \"TV\"]",
        "price" : "$3,000.00",
        "minimum_nights" : 2,
        "maximum_nights" : 30,
        "minimum_minimum_nights" : 2,
        "maximum_minimum_nights" : 2,
        "minimum_maximum_nights" : 1125,
        "maximum_maximum_nights" : 1125,
        "minimum_nights_avg_ntm" : 2,
        "maximum_nights_avg_ntm" : 1125,
        "has_availability" : "t",
        "availability_30" : 28,
        "availability_60" : 58,
        "availability_90" : 88,
        "availability_365" : 88,
        "calendar_last_scraped" : "2021-10-29",
        "number_of_reviews" : 95,
        "number_of_reviews_ltm" : 0,
        "number_of_reviews_l30d" : 0,
        "first_review" : "2013-10-19",
        "last_review" : "2020-03-17",
        "review_scores_rating" : 4.71,
        "review_scores_accuracy" : 4.87,
        "review_scores_cleanliness" : 4.75,
        "review_scores_checkin" : 4.92,
        "review_scores_communication" : 4.88,
        "review_scores_location" : 4.67,
        "review_scores_value" : 4.75,
        "license" : "M130007760",
        "instant_bookable" : "f",
        "calculated_host_listings_count" : 1,
        "calculated_host_listings_count_entire_homes" : 0,
        "calculated_host_listings_count_private_rooms" : 1,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 0.97
}

3. Choose two hosts who are superhosts, and show all of the listings offered by both of the two hosts

```
db.listings.find(
    {$or: [
        {'host_id': 4626879},
        {'host_id': 9782688}
    ] },
    { 
        'name': 1,
        'price': 1,
        'neighbourhood': 1,
        'host_name': 1,
        'host_is_superhost': 1
    }
)
```
I use $or to set the two specific hosts, and only show name, price, neighbourhood, host_name and host_is_superhost.

First three results:
>{ "_id" : ObjectId("6196c56b051c47f3e6955cb2"), "name" : "SHINJUKU ★Designer Pencil House★ Airport Transfer", "host_name" : "Tracey", "host_is_superhost" : "t", "price" : "$21,848.00" }
{ "_id" : ObjectId("6196c56b051c47f3e6955cc2"), "name" : "*NEW*TOKYO HOUSE group&family upto7 & carpark WIFI", "host_name" : "Kevin", "host_is_superhost" : "t", "price" : "$17,376.00" }
{ "_id" : ObjectId("6196c56b051c47f3e6955fdf"), "name" : "SHINJUKU W ★ FujiHouse 2 rooms ★ Great Value", "host_name" : "Tracey", "host_is_superhost" : "t", "price" : "$11,841.00" }

4. Find all the unique host_name values
```
db.listings.distinct('host_name')
```
I use distinct to find the unique values.

First three results:
>"& And  Hostel Minamisenju",
>        
>"2a",
>
>"A+K Tokyo",

5. Find all of the places that have more than 2 beds in a neighborhood of your choice, ordered by review_scores_rating descending

```
db.listings.find(
    {$and: [
        {'beds': {
            $gt: 2
        }},
        {'neighbourhood_cleansed': 'Minato Ku'}
    ] },
    { 
        'name': 1,
        'beds': 1,
        'review_scores_rating': 1,
        'price': 1
    }
    ).sort(
        {'review_scores_rating': -1}
    )
```
I use $and to set a specific neighbourhood, then set beds to greater than 2. I only show name, beds, review_scores_rating and price. I then sort by review_score_rating in descending order.

First three results:
>{ "_id" : ObjectId("6196c56b051c47f3e69569fa"), "name" : "★Monthly Rental★3BR/Shirokane/Shibuya/Roppongi", "beds" : 6, "price" : "$10,857.00", "review_scores_rating" : 5 }
>
>{ "_id" : ObjectId("6196c56b051c47f3e6956afc"), "name" : "HOYO東京Akasaka#603/3min from Akasaka sta+wifi", "beds" : 4, "price" : "$4,929.00", "review_scores_rating" : 5 }
>
>{ "_id" : ObjectId("6196c56b051c47f3e6956bd2"), "name" : "【14日隔离 -安心入住】60㎡～两室一厅，有电 梯，宽敞舒适高品质公寓，生活便利，车站步行4分", "beds" : 3, "price" : "$14,950.00", "review_scores_rating" : 5 }

6. Show the number of listings per host

```
db.listings.aggregate(
    {$group: {
         _id: '$host_id', 
         listingCount: {$sum: 1}
        }
    }
)
```
I use aggregate, then $group to group by unique host_id, and find the listings count by summation.

First three results:
>{ "_id" : 292188822, "listingCount" : 1 }
>
>{ "_id" : 307789969, "listingCount" : 2 }
>
>{ "_id" : 230616333, "listingCount" : 5 }

7. Find the average review_scores_rating per neighbourhood, and only show the ones above a 95, sorted in descending order of rating

```
db.listings.aggregate(
    [
        {$match: {number_of_reviews: {$gt:95}}},
        {$group: {_id: '$neighbourhood_cleansed', avgRating: {$avg: '$review_scores_rating'}}},
        {$sort: {avgRating: -1}}
    ]
)
```
I use aggregate, then $match to only include those with number_of_reviews greater than 95. Then I use $group to group by neighborhood, and use $avg to get the average rating. Finally, I sort by average rating in descending order.

First three results:
>{ "_id" : "Katsushika Ku", "avgRating" : 4.899333333333333 }
>
>{ "_id" : "Itabashi Ku", "avgRating" : 4.882 }
>
>{ "_id" : "Edogawa Ku", "avgRating" : 4.84 }