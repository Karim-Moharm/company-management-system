
## GET /api/resource/project
```bash
curl --location 'http://127.0.0.1:8000/api/resource/Project/API2' \
--header 'Cookie: sid=Guest; system_user=no; full_name=Guest; user_id=Guest; user_lang=en' \
--header 'Authorization: token API_KEY:API_SECRET'
```

Response

```json
{"data":[{"name":"API1"},{"name":"API2"},{"name":"API3"},{"name":"Company Managment System"},{"name":"Penetation Testing"}]}
```

![alt text](../imgs/image(1).png)


---

## GET /api/resource/project/API1

```bash
curl --location 'http://127.0.0.1:8000/api/resource/Project/API1' \
--header 'Cookie: sid=Guest; system_user=no; full_name=Guest; user_id=Guest; user_lang=en' \
--header 'Authorization: token a0e7ec64a62c939:ebf4278767d0090'
```

Response

```json
{
    "data": {
        "name": "API1",
        "owner": "Administrator",
        "creation": "2025-12-18 22:10:20.030736",
        "modified": "2025-12-18 22:10:20.030736",
        "modified_by": "Administrator",
        "docstatus": 0,
        "idx": 0,
        "project_name": "API1",
        "company": "comp1",
        "department": "Engineering",
        "description": "<div class=\"ql-editor read-mode\"><p>test</p></div>",
        "start_date": "2025-12-08",
        "doctype": "Project",
        "assigned_employees": []
    }
}
```

![alt text](../imgs/image(2).png)

---

## POST /api/resource/project

```bash
curl --location 'http://127.0.0.1:8000/api/resource/Project/' \
--header 'Cookie: sid=Guest; system_user=no; full_name=Guest; user_id=Guest; user_lang=en' \
--header 'Content-Type: application/json' \
--header 'Authorization: token a0e7ec64a62c939:ebf4278767d0090' \
--data '{
        "project_name": "Company Managment sys",
        "company": "comp1",
        "department": "Engineering",
        "description": "<div class=\"ql-editor read-mode\"><p>test</p></div>",
        "start_date": "2025-12-19",
        "doctype": "Project",
        "assigned_employees": []
    }'
```



![alt text](<../imgs/post-project.png>)