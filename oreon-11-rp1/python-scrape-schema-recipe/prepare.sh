#!/bin/bash

wget https://github.com/micahcochran/scrape-schema-recipe/archive/v0.2.2/scrape-schema-recipe-0.2.2.tar.gz
tar -xf scrape-schema-recipe-0.2.2.tar.gz 
cd scrape-schema-recipe-0.2.2
cd scrape_schema_recipe
cd test_data/
# remove test data due to licenses
rm *.html 
cd ..
cd ..
cd ..
tar -cvf scrape-schema-recipe-cleaned-0.2.2.tar scrape-schema-recipe-0.2.2
gzip scrape-schema-recipe-cleaned-0.2.2.tar 
