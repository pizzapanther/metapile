# Metapile

## Setup

```
pip install -r requirements.txt
python manage migrate
```

## Processing Images

```
python manage.py processimages waldo-recruiting
```

## Description

Process images command lists a bucket and process the image's Exif info. This data is stored in a Postgres JSON field. You view a list of all images at the root URL. The data is communicated via a GraphQL API. Clicking on a button reveals the EXIF data for each image.

### Deployed at: https://metapile.herokuapp.com/
