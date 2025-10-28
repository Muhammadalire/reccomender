# 🚀 Start Local Backend - Quick Guide

## Step-by-Step Instructions

### 1. Install ngrok (One-time)

**macOS:**
```bash
brew install ngrok/ngrok/ngrok
```

**Or download from:** https://ngrok.com/download

---

### 2. Start Flask Backend

Open Terminal and run:

```bash
cd /Users/muhammadali/Documents/reccomender/api
python3 index.py
```

You should see:
```
✅ Books loaded: 98
 * Running on http://127.0.0.1:5001
```

**Keep this terminal open!**

---

### 3. Open New Terminal - Start ngrok

In a **NEW terminal window**, run:

```bash
ngrok http 5001
```

You'll see something like:
```
Session Status: online
Forwarding: https://abc1-234-56-789.ngrok-free.app -> http://localhost:5001
```

**Copy the https URL** (the one with `ngrok-free.app` or `ngrok.io`)

Example: `https://abc1-234-56-789.ngrok-free.app`

**Keep this terminal open too!**

---

### 4. Update Frontend

Edit `public/script.js` and replace line 1-9 with your ngrok URL:

```javascript
// API Configuration
const API_BASE_URL = 'https://YOUR-NGROK-URL-HERE.ngrok-free.app';
```

**Replace `YOUR-NGROK-URL-HERE` with your actual ngrok URL!**

---

### 5. Deploy Frontend to Vercel

```bash
cd /Users/muhammadali/Documents/reccomender
./deploy.sh
```

---

### 6. Test Your Site

1. Go to your Vercel URL
2. The frontend will connect to your local backend through ngrok
3. All features should work!

---

## 🔄 Every Time You Want to Use It

1. **Start Flask**: `cd api && python3 index.py`
2. **Start ngrok**: `ngrok http 5001` (in new terminal)
3. **Copy ngrok URL** if it changed
4. **Update frontend** if URL changed and redeploy

---

## ⚠️ Important Notes

1. **Both terminals must stay open** while your girlfriend uses the site
2. **Your laptop must stay on** and connected to internet
3. **ngrok URL changes** every time you restart ngrok (unless you have paid account)
4. **If laptop sleeps**, the site will stop working

---

## 🆘 Troubleshooting

### Flask won't start
```bash
# Make sure you're in the api directory
cd /Users/muhammadali/Documents/reccomender/api
python3 index.py
```

### ngrok not found
```bash
# Install ngrok
brew install ngrok/ngrok/ngrok

# Or download from https://ngrok.com/download
```

### Frontend can't connect
1. Check ngrok URL is correct in `script.js`
2. Make sure both terminals are still running
3. Check ngrok hasn't expired (free tier has time limits)

---

## 📊 Status Check

**Is it working?**
- ✅ Terminal 1: Shows Flask running
- ✅ Terminal 2: Shows ngrok forwarding
- ✅ Frontend deployed to Vercel
- ✅ Frontend has correct ngrok URL

**All good!** Your girlfriend can use it! 💖

---

**Remember: Your laptop must stay on!** 💻⚡
