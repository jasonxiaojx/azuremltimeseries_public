from azureml.core import Workspace, Dataset

subscription_id = 'REPLACE'
resource_group = 'REPLACE'
workspace_name = 'REPLACE'

workspace = Workspace(subscription_id, resource_group, workspace_name)

dataset = Dataset.get_by_name(workspace, name='MSFT')
dataset = dataset.to_pandas_dataframe()

print(dataset.head())
print(dataset.dtypes)