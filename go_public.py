import sys
import subprocess
from pyngrok import ngrok

print("=" * 60)
print("🌍 PUBLIC HEADLINE GENERATOR")
print("=" * 60)

try:
    # Install Flask if needed
    print("\n📦 Checking dependencies...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "Flask"], check=False)
    
    print("✅ Dependencies ready!\n")
    
    # Create ngrok tunnel
    print("🔗 Creating public link with ngrok...")
    print("(This may take a moment...)\n")
    
    public_url = ngrok.connect(5000)
    print("=" * 60)
    print("🎉 SUCCESS! Your website is now PUBLIC!")
    print("=" * 60)
    print(f"\n📱 Share this link with anyone:\n   {public_url}\n")
    print("=" * 60)
    print("\nℹ️  Important:")
    print("- Keep this window OPEN")
    print("- Your site stays live while this runs")
    print("- Links expire when you close this window")
    print("- Press Ctrl+C to stop\n")
    print("=" * 60)
    
    # Keep the tunnel alive
    input("\nPress Enter when you want to stop...")
    
except ImportError:
    print("❌ ngrok not installed. Installing now...\n")
    subprocess.run([sys.executable, "-m", "pip", "install", "pyngrok"], check=True)
    print("\n✅ Installed! Please run this script again.\n")
except Exception as e:
    print(f"❌ Error: {e}")
    print("\nTroubleshooting:")
    print("1. Make sure app.py is in the same folder")
    print("2. Run: pip install pyngrok")
    print("3. Try again\n")
