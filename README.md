# aws_hooks_connection_airflow
This is a sample implementation for connecting to aws s3 bucket usign airflow hooks
Steps: 
- Create a new IAM role called e.g. airflow_aws_user and allow programatical access, generate a key and password and save it. 
- under Airflow UI Go to Admin >> Connections >>create a new connection
- Connection ID called "aws_credentials"
- Connection Type "Amazon Web Services" : 
	- if it's not already installed use command : "pip install apache-airflow-providers-amazon"
- Add login as ID and password. 
- Define a variables : 
- Airflow UI >> Admin>>Variables >> add [Key : s3_bucket, Val : awssampledbuswest2]
- Follow the code in Dag and run it.
