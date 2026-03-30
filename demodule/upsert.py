import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config import get_config
config = get_config()


# approach 1: using default parameters
# def first_query(
#     target_catalog: str = config["catalog"],
#     target_schema: str = config["schema"],
#     target_table: str = config["table"]
#     ):
def first_query(
    target_catalog: str = config["catalog"],
    target_schema: str = config["schema"],
    target_table: str = config["table"]
    ):
    def select_query(
        target_catalog=target_catalog,
        target_schema=target_schema,
        target_table=target_table,
    ):
        return f"""select * from {target_catalog}.{target_schema}.{target_table} """
    return select_query()

from config.config import second_get_config
second_config = second_get_config()

def second_query(
    target_catalog: str = second_config["catalog"],
    target_schema: str = second_config["schema"],
    target_table: str = second_config["table"]
    ):
    def insert_query(
        target_catalog=target_catalog,
        target_schema=target_schema,
        target_table=target_table,
    ):
        return f""" select * {target_catalog}.{target_schema}.{target_table} 
        """
    return insert_query()
    
res=second_query()
print(res)

