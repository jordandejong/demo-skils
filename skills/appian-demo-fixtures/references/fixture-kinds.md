# Fixture kinds

Pick only what the script will show on screen.

| Kind | Typical ext | Must include |
|---|---|---|
| Invoice | pdf / xlsx | vendor, invoice no, date, lines, tax, total |
| Purchase order | pdf | PO no that the invoice can match |
| Email | eml / pdf | from, subject, body, attachment name |
| ID / KYC | pdf | name matching a record, expiry date |
| Policy / contract | pdf / docx | party names, effective date, clause the process cites |
| CSV seed | csv | headers = record field names, UTF-8 |
| Exception | pdf | one broken field (wrong total, missing tax) |

`manifest.json` example:

```json
{
  "files": [
    {
      "path": "tokyo-gas-invoice-1042.pdf",
      "kind": "invoice",
      "targetRecordType": "TGET Invoice",
      "expected": {"invoiceNumber": "1042", "currency": "JPY"}
    }
  ]
}
```
