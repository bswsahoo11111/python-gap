import sys
from demodule import upsert   # import your query functions
# from config import config     # import your config module

from config.config import get_config
config = get_config()

from config.config import second_get_config
second_config = second_get_config()

def main(args):
    """
    Entry point for Databricks job.
    Args are passed in from Databricks job parameters.
    """
    # Unpack job parameters
    # Example: ["gdp_pii_preprod","customer360","audit_table","select"]
    target_catalog, target_schema, target_table, operation = args

    # # Build a config dictionary dynamically
    # cfg = {
    #     "catalog": target_catalog,
    #     "schema": target_schema,
    #     "table": target_table
    # }

    # Dispatch based on operation
    if operation == "select":
        query = upsert.first_query(
            target_catalog=config["catalog"],
            target_schema=config["schema"],
            target_table=config["table"]
        )
    elif operation == "insert":
        query = upsert.second_query(
            target_catalog=second_config["catalog"],
            target_schema=second_config["schema"],
            target_table=second_config["table"]
        )
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    print("Generated SQL:")
    print(query)

if __name__ == "__main__":
    # Databricks passes job parameters as sys.argv[1:]
    main(sys.argv[1:])
