import json

company_name = input("Sisesta oma ettevõtte nimi: ")


while True:
        contact_email = input("Sisesta oma isiklikk email address: ")
        if "@" in contact_email:
            pass
        else:
            print("NOO")



data_collection_type = input("Millised andmed salvestame: ")
data_usege = input("Kuidas andmed kasutatakse: ")
data_storage_limit = input("Kui kaua andem salvestatakse: ")
cookie_agreement = input("Kas nõustute e-posti aadressis '@' kontrollimisega? (jah/ei): ")

privacy_data = {
    "company_name": company_name,
    "contact_email": contact_email,
    "data_collection_type": data_collection_type,
    "data_usege": data_usege,
    "data_storage_limit": data_storage_limit,
    "cookie_agreement": cookie_agreement
}

with open("privacy_template.json", "w", encoding="utf-8") as file:
    json.dump(privacy_data, file, indent=4)
print("Kõik on salvestatud")

html_template = """
<!DOCTYPE html>
<html>
<head>
<title>Privaasuspooliitika</title>
</head>
<body>
    <h1>Poliitika pühendanud ettevõttele - {company_name}</h1>
    <p>Kontakt: {contact_email}</p>
    <h2>Millised andmed kogume?</h2>
    <p>{data_collection_type}</p>
    <h2>Kuidas andmed kasutatakse</h2>
    <p>{data_usege}</p>
    <h2>Kui kaua andmed salvestatakse</h2>
    <p>{data_storage_limit}</p>
    <h2>Küpsiste kokkulepe</h2>
    <p>Kas nõustute, et kontrollime e-posti aadressi sisaldavust '@' märgiga: {cookie_agreement}</p>
</body>
</html>
"""

privacy_policy = html_template.format(**privacy_data)

with open("privacy_template.html", "w", encoding="utf-8") as file:
    file.write(privacy_policy)

print("HTML fail on genereeritud edukalt.")




