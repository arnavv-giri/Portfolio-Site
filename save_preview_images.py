import base64, os

output_dir = r"C:\Users\arnav\OneDrive\Desktop\portfolio\Portfolio-Site\public"

THRIFTBAZAAR_B64 = open(r"C:\Users\arnav\OneDrive\Desktop\portfolio\Portfolio-Site\tb.b64").read().replace('\n','')
BANKMATE_B64 = open(r"C:\Users\arnav\OneDrive\Desktop\portfolio\Portfolio-Site\bm.b64").read().replace('\n','')
GROWSMART_B64 = open(r"C:\Users\arnav\OneDrive\Desktop\portfolio\Portfolio-Site\gs.b64").read().replace('\n','')

images = {
    "thriftbazaar-preview.png": THRIFTBAZAAR_B64,
    "bankmate-preview.png": BANKMATE_B64,
    "growsmart-preview.png": GROWSMART_B64,
}

for filename, b64data in images.items():
    path = os.path.join(output_dir, filename)
    with open(path, "wb") as f:
        f.write(base64.b64decode(b64data))
    print(f"Saved: {path}")
