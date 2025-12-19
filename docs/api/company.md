# GET /api/resource/Company

```
curl --location 'http://127.0.0.1:8000/api/resource/Company/' \
--header 'Cookie: sid=Guest; system_user=no; full_name=Guest; user_id=Guest; user_lang=en' \
--header 'Authorization: token a0e7ec64a62c939:ebf4278767d0090'
```

Response
```json
{"data":[{"name":"3uclikf0e2"},{"name":"braiin22"},{"name":"comp1"},{"name":"BrainWise"}]}
```

![alt text](<../imgs/get-company.png>)


---

# GET /api/resource/Company
![alt text](<../imgs/retrieve-company.png>)

Response
```json
{"data":{"name":"BrainWise","owner":"Administrator","creation":"2025-12-18 23:29:56.161877","modified":"2025-12-19 11:37:37.628249","modified_by":"Administrator","docstatus":0,"idx":0,"company_name":"BrainWise","number_of_departments":1,"number_of_employees":2,"number_of_projects":2,"doctype":"Company"}}
```