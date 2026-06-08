import requests
import base64
import time
import json
import sys


access_token="eyJraWQiOiIwODlhNzU2Yy02N2Q0LTQ5MmMtODM5MS1hODg2NTFlMGUwY2EiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJBbml0aGEiLCJ1c2VyLWF1dGhvcml0aWVzIjpbImRhdGFmbG93LWRiLXNjcmlwdCIsImVkaXQtcGlwZWxpbmUiLCJlZGl0LWRhdGEtc291cmNlIiwiZWRpdC1rdWJlcm5ldGVzIiwiZGVsZXRlLXBpcGVsaW5lIiwiZWRpdC1henVyZS1jbHVzdGVyIiwiZGF0YWZsb3ctZGF0YS1ydWxlIiwidmlldy1kYXRhLXF1YWxpdHktcnVsZSIsImRhdGFmbG93LWRhdGEtY29tcGFyZSIsImRhdGFmbG93LWRiLXNpbmsiLCJ2aWV3LWRhdGEtc291cmNlIiwidmlldy1kb21haW5zIiwidmlldy1henVyZS10ZXN0cGxhbiIsImRhdGFmbG93LWNyb3NzLXNvdXJjZS1jb21wb25lbnQiLCJkYXRhZmxvdy10YWJsZWF1LXNvdXJjZS1jb21wb25lbnQiLCJ2aWV3LWRhdGEtbW9kZWwiLCJleHRlcm5hbC12YXVsdCIsImVkaXQtZGF0YXNldCIsInZpZXctYXp1cmUtY2x1c3RlciIsImVkaXQtYXp1cmUtdGVzdHBsYW4iLCJlZGl0LXJlcG9ydCIsImVkaXQtZGF0YS1xdWFsaXR5LXJ1bGUiLCJhZGQtY29udGFpbmVyIiwidmlldy1zY2hlZHVsZXIiLCJ2aWV3LXN1YmplY3QtYXJlYSIsInZpZXctcmVwb3J0IiwiZGF0YWZsb3ctY29nbm9zLXNvdXJjZS1jb21wb25lbnQiLCJydW4tdGVzdGNhc2UiLCJlZGl0LWxpdnlzZXJ2ZXIiLCJ2aWV3LWVtci1jbHVzdGVyIiwiZGF0YWZsb3ctZGF0YS1vYnNlcnZhYmlsaXR5Iiwidmlldy1nbG9iYWwtcGFyYW1ldGVyIiwiZGVsZXRlLWRhdGEtbW9kZWwiLCJkYXRhZmxvdy1vYS11cGdyYWRlLWNvbXBvbmVudCIsIm1vbml0b3JpbmciLCJkYXRhZmxvdy1wb3dlcmJpLXJlZ3Jlc3Npb24tY29tcG9uZW50IiwiZGF0YWZsb3ctdGFibGVhdS1yZWdyZXNzaW9uLWNvbXBvbmVudCIsInJ1bi1waXBlbGluZSIsImVtYWlsLXRlbXBsYXRlIiwidmlldy1waXBlbGluZSIsImVkaXQtdGVtcGxhdGUiLCJsaWNlbnNlIiwicGFzc3dvcmQtdmF1bHQiLCJkYXRhZmxvdy1tZXRhZGF0YS1jb21wYXJlIiwiZWRpdC1zdWJqZWN0LWFyZWEiLCJkYXRhZmxvdy1kYXRhLXByb2ZpbGUiLCJ2aWV3LWt1YmVybmV0ZXMiLCJkYXRhZmxvdy1tZXRyaWMtY29tcGFyZSIsImFkZC1yb2xlIiwicnVuLWRhdGFmbG93IiwiaW50ZWdyYXRpb24iLCJlZGl0LXNjaGVkdWxlciIsInZpZXctdGVzdGNhc2UiLCJhZG1pbi1zY2hlZHVsZXIiLCJub3RpZmljYXRpb25zIiwibWFuYWdlLWNsdXN0ZXIiLCJ2aWV3LXRlbXBsYXRlIiwidmlldy1kYXRhc2V0IiwiZGF0YWZsb3ctdGFibGVhdS11cGdyYWRlLWNvbXBvbmVudCIsImVkaXQtZG9tYWlucyIsImRlbGV0ZS10ZXN0Y2FzZSIsInJ1bi1kYXRhLW1vZGVsIiwiYXBwLXByb3BlcnRpZXMiLCJlZGl0LWdsb2JhbC1wYXJhbWV0ZXIiLCJtYW5hZ2UtZGF0YS1zb3VyY2UiLCJ2aWV3LWRhdGFmbG93Iiwic2VjdXJpdHkiLCJnaXQiLCJ2aWV3LWxpdnlzZXJ2ZXIiLCJvcGVyYXRvcnMiLCJkYXRhZmxvdy1wb3dlcmJpLXNvdXJjZS1jb21wb25lbnQiLCJ3b3JrZXItbW9uaXRvciIsImRlbGV0ZS1kYXRhZmxvdyIsImRhdGFmbG93LW9hLXJlZ3Jlc3Npb24tY29tcG9uZW50IiwiZWRpdC1kYXRhZmxvdyIsImRhdGFmbG93LXBvd2VyYmktdXBncmFkZS1jb21wb25lbnQiLCJlZGl0LWRhdGEtbW9kZWwiLCJtYXBwaW5nLW1hbmFnZXIiLCJlZGl0LWVtci1jbHVzdGVyIiwiZGF0YWZsb3ctb2Etc291cmNlLWNvbXBvbmVudCIsImRhdGFmbG93LXRhcmdldCIsImVudmlyb25tZW50IiwicGx1Z2luIiwiZGF0YWZsb3ctcXVpY2tzaWdodC1zb3VyY2UtY29tcG9uZW50IiwibXVsdGlwbGUtZGF0YS1jb21wYXJlIiwiZWRpdC10ZXN0Y2FzZSIsImRhdGFmbG93LWxvb2t1cCIsImF1ZGl0LWxvZ3MiLCJjdXN0b20tZmllbGRzIiwibWFuYWdlLWFjY2VzcyJdLCJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjYwNTUvZGF0YW9wc3NlY3VyaXR5IiwiYXVkIjoiZGF0YW9wc3N1aXRlLWFwcGxpY2F0aW9uLWNsaWVudCIsIm5iZiI6MTc4MDkxODA2MywicHJkdmVyIjoiMjAyNi4xLjAuMCIsImxpY2V4cCI6Ik4iLCJzY29wZSI6WyJjdXN0b20iXSwicHdleHAiOiJOIiwiZXhwIjoxNzgwOTE5ODYzLCJpYXQiOjE3ODA5MTgwNjMsImp0aSI6ImQ1ZDEzNDVkLTE4OWUtNGRiMi1hYmFmLThhMTdlMGE3ZTVlNSJ9.AtMUgiEQfDf5Rg1roTgKrdn53dV45v8bVy_Vygcpb3lgOlmu20mKLPyq0DHBSzdcbyaFuN9rgvYSOstE-KtGtWjTnVs2ESQfkMBxTpbVxUkHAfjLowTURx4FxWLt3eEaYdvOVROqoc7P62di6HEg5vnA38LsGhKiCH-0Edo6CBHPnrgft6oIjsake2-zMEh01QBZO5vWtRQc2WiUwHXpYX7Slnk5cWqY8VmKYt8PK4M8JWWrlA8wXnU6r72PRbKy7qmlBwhn6H2f-TwfVi9JsCvhGke5fAWRSHiSrVCepgr_a4BkrRW33cvFApkD2EuLgImQJvRT8tfOllQffT82EQ"

def trigger_pipeline():
    pipeline_url = "http://192.168.6.205:6055/piper/jobs"
    pipe_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    pipe_payload = {
        "pipelineId": pipeline_id,
        "runName": "Trigger Pipeline using Github actions",
    }

    print(" Triggering Pipeline...")
    pipeline_response = requests.post(pipeline_url, headers=pipe_headers, json=pipe_payload)

    if pipeline_response.status_code != 200:
        print(f"Pipeline trigger failed: {pipeline_response.status_code}, {pipeline_response.text}")
        sys.exit(1)

    pipeline_data = pipeline_response.json()
    pipeline_run_id = pipeline_data.get("id") or pipeline_data.get("jobId")
    print(f" Pipeline triggered successfully, Run ID: {pipeline_run_id}")

    return access_token, pipeline_run_id


def pipeline_status(bearer_token, pipeline_run_id):
    status_url = f"http://192.168.6.205:6055/piper/jobs/{pipeline_run_id}/status"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
    }

    print(" Checking pipeline status every 60 seconds...")

    while True:
        response = requests.get(status_url, headers=headers)
        if response.status_code != 200:
            print(f" Status check failed: {response.status_code}, {response.text}")
            sys.exit(1)

        try:
            data = response.json()
        except json.JSONDecodeError:
            print("Failed to parse JSON response")
            sys.exit(1)

        status = data.get("status")
        print(f"Pipeline Status: {status}")

        if status in ["COMPLETED", "FAILED", "ERROR"]:
            print(f" Pipeline finished with status: {status}")
            return status

        time.sleep(60)  


token, run_id = trigger_pipeline()
final_status = pipeline_status(token, run_id)

if final_status == "COMPLETED":
    sys.exit(0)
else:
    sys.exit(1)
