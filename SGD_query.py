#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("https://yeastmine.yeastgenome.org:443/yeastmine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# The view specifies the output columns
query.add_view(
    "expressionScores.expressioncondition.expressiondataset.pubmedID",
    "expressionScores.expressioncondition.expressiondataset.numGenes",
    "expressionScores.expressioncondition.expressiondataset.numConds",
    "expressionScores.expressioncondition.expressiondataset.publicationYear",
    "expressionScores.expressioncondition.expressiondataset.author",
    "expressionScores.expressioncondition.expressiondataset.name"
)

# You can edit the constraint values below
query.add_constraint("expressionScores.expressioncondition.expressiondataset.numGenes", ">=", "4000", code = "A")
query.add_constraint("expressionScores.expressioncondition.expressiondataset.publicationYear", ">=", "2008", code = "C")
query.add_constraint("expressionScores.expressioncondition.expressiondataset.expressiondatasettags.tagname", "CONTAINS", "stress", code = "D")

# Uncomment and edit the code below to specify your own custom logic:
# query.set_logic("A and C and D and C and C and D and C and C and D")

for row in query.rows():
    print row["expressionScores.expressioncondition.expressiondataset.pubmedID"], \
        row["expressionScores.expressioncondition.expressiondataset.numGenes"], \
        row["expressionScores.expressioncondition.expressiondataset.numConds"], \
        row["expressionScores.expressioncondition.expressiondataset.publicationYear"], \
        row["expressionScores.expressioncondition.expressiondataset.author"], \
        row["expressionScores.expressioncondition.expressiondataset.name"]
