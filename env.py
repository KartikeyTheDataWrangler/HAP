import os

os.environ['GDRIVE_CREDENTIALS_DATA'] = '{ \
  "type": "service_account",\
  "project_id": "hip-limiter-394909",\
  "private_key_id": "36bd78d1199a87448f7c20b26c7e5d9bc7ec8437",\
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC9l3Ebfz4GaYue\nGg16BDN+Fd3K/AEB9DpVih2IMcYvR75bbb5xYM+jKLbKtHFlLRx7CYgfGihBAFvJ\nSmDXFP4eKRgUaTk+jGchjXGbTnHsJzYjpxfATRaef50Ium0j4CW0CzAwCsXtrROu\n+8Ev+CEHYKLvHalmh3Vck40CH171CRJ3XGzx14s41sLz292NIUl1T4IAT7NM1CP4\nQZ5pkO86XSQm77l+xT35nDftZCu8VTM+oRBkgEouVtKUfQiy8IOy2IU7ZV7B3TGE\nQMr3iKCZIe0OaX+ZkslgHkSDnih4b7WOXYZPQuy+bi0DqgSVupGR8NGx5C+5Q56L\n6TapTEZ/AgMBAAECggEAWQtyQ6xg+MkEmpZ44uhrONpTR71RSdYnubo7QZbDEry6\n8p0aF40VKHf8VjsmkRL9b+obpSP3aQQel+1Xi10gNxEs7pU3HiH6ZB9XDs7qobQO\n8PLPLHHoYDvmiM1qajGh86xXjxDYQleKSaKTaxC6joj8LZs8T1vqqrbgQPFz+1hc\n+tDdqYWJ566cn5hkpabxKSQ3ad5NRZM9x/pvjR0pKEC+gtOjvUhFj0jocqiQxHY8\nab4vxMlwNL0j4F9c6zHKfivkU6kAa0+KMSyLmvKf1r4yLuajdDoU8KiR5dJF+8wH\ndop322YmFV7O9Ra0Yu3Dc1GUU8dm+kTpGZejNcYnCQKBgQD9Zu1zRbYlIfp9tOAC\nObiKvsCHSUMK9ggslp3Y4HlaoJINtdJit1Iu2hHmiAVEOn3eSippP338YiNxjS/e\nEFsyag96yzFb7d5fZ92Kkf/9yn7s2uFoU/0cyIwm0tN+GlXT92UB8p9uOkAO6bm1\niW24MuJt8wbT3RgPSrVFD/qrFwKBgQC/iQn3T7G09QbkcGpdwp5afBy1Rq1ivVlN\nOzjPqkd2jFQ4NUXavq7r8jizpdO2X+McFXKcW5IWY33U2J3K9vYQG9urt1CGapYv\nZF50WkmMqyXio0vbSGINulootzLNv1BPMbIfiVrN3kQhPNf3G41ff4Z9SLD7SUsu\nhjtNPoDA2QKBgEbD/b/ZUfqguJFud7hnYi/tAVtGjGB9QN8i2MX+OiWi/eayRiSn\nSV4oLCOTDNV2+DuhvqJRxt86kOdfJGUBcFZt5BDIueoQTa+bE/VkvHalnDiND7HQ\n8ridEPaunb1zoVBmoGCg3wErZ0RC5UfbLzbnjvBhlCCKd/OdS24T/k7VAoGBAIM2\nvYYYqZRffC5JOQUsi9FPT1d8qNGJCEGZfaz+aWC0eAndrRJTKYBoeyHPS7+X5v1Z\nUB//t4/w7sY+87KVBzM38oCr39WF9YdYCkFJjTN6GEUwO4ppBwuCi7ty7bH4C2uF\njxJ9xaBdUW03wnf9/xbaRWdUwjIUHxYrTTr4w7nZAoGBAOvk64lEsIiUKyRcSWdi\nXUk2QkcwRKG8LMtSDm6Et/3pHwu2nzEHgjLtR5NQ1VXGVHmBE5t8qrweqVrFr7T5\niXXQC7h52sPiITYHxB6Ok9xBReOtn+K7p3ZjfFgBeh72bphWiIZuUypTfo+rseeS\n+WTeCAGKb8pzSH5Nk1gglzps\n-----END PRIVATE KEY-----\n",\
  "client_email": "belth-231@hip-limiter-394909.iam.gserviceaccount.com",\
  "client_id": "108075611789569099366",\
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",\
  "token_uri": "https://oauth2.googleapis.com/token",\
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",\
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/belth-231%40hip-limiter-394909.iam.gserviceaccount.com",\
  "universe_domain": "googleapis.com"\
}'


print(os.getenv('GDRIVE_CREDENTIALS_DATA'))