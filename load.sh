#!/bin/sh
echo "Ingesting data and ceating graphs"

./bin/neo4j-admin database import full --ignore-empty-strings=true --skip-duplicate-nodes=true --ignore-extra-columns=true --high-parallel-io=on \
--skip-bad-relationships=true --delimiter="," --array-delimiter="|" --quote="'" --nodes=import/nodes_roots.csv \
--nodes=import/nodes_people.csv --nodes=import/nodes_books.csv \
--relationships=import/relations_roots.csv --relationships=import/relations_read.csv --relationships=import/relations_favourite.csv neo4j