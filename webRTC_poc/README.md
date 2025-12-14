# WebRTC .local Leak + Internal Recon PoC

## Summary

This PoC simulates:
1. Victims leaking `.local` hostname via WebRTC
2. Port scanning internal `.local` host (port `80`, `443`)
3. Fetching fake internal user data (`user.json`) hosted using server.py
4. Sending data to a controlled server (C2)

All client-side behavior is self-contained and **does not store or abuse real data**.

---

## How to Run (Locally)

### 1. Serve the Main Page or Just open the index.html on your browser
```bash
python3 -m http.server 8000
```

### 2. Run c2.py
Make sure you set up a virtual environment to install flask-cors
```
   python3 -m venv venv && source venv/bin/activate
   pip3 install flask-cors
   python3 c2.py
```
### 3. Run the server  
```
	sudo python3 server.py
```

### 4. Next click on the 'Join Now' button on the index.html page you opened.
