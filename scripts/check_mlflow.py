import mlflow

mlflow.set_tracking_uri(r"file:///C:/Users/hi/AI-CloudSec-System-1/mlruns")
experiment_name = "Team2_Feature_Engineering_Traffic_Data"
mlflow.set_experiment(experiment_name)

client = mlflow.tracking.MlflowClient()
experiment = client.get_experiment_by_name(experiment_name)

if experiment is None:
    print(f"No experiment found with name '{experiment_name}'")
else:
    print(f"Experiment ID: {experiment.experiment_id}")
    runs = client.search_runs([experiment.experiment_id])
    if not runs:
        print("No runs found in this experiment.")
    else:
        print(f"Found {len(runs)} run(s):")
        for r in runs:
            print(f" - Run ID: {r.info.run_id}, Status: {r.info.status}")
