import hashlib
import time
import random

# ------------------------------------
# Your Wallet Address
# ------------------------------------
WALLET_ADDRESS = "your_btc_wallet_here"  # Replace with your BTC address

# ------------------------------------
# Mining Function (Luck-based)
# ------------------------------------
def mine_simulation(wallet_address, difficulty=6, max_attempts=5_000_000):
    print("\n==== ⛏️ Bitcoin Luck Mining Simulator ====")
    print(f"[+] Wallet: {wallet_address}")
    print(f"[+] Difficulty: {difficulty} (requires hash starting with {'0' * difficulty})")
    print("[*] Starting mining...\n")

    prefix = '0' * difficulty
    start_time = time.time()

    for attempt in range(1, max_attempts + 1):
        nonce = random.randint(0, 1_000_000_000)
        data = f"{wallet_address}{nonce}".encode()
        hash_result = hashlib.sha256(data).hexdigest()

        if hash_result.startswith(prefix):
            elapsed = time.time() - start_time
            print("🎉 BLOCK MINED!")
            print(f"🧠 Nonce: {nonce}")
            print(f"🔗 Hash: {hash_result}")
            print(f"💰 Reward (simulated): Sent to wallet {wallet_address}")
            print(f"⏱️ Time taken: {elapsed:.2f} seconds")
            return True

        if attempt % 500000 == 0:
            print(f"[{attempt}/{max_attempts}] Still mining...")

    print("\n❌ No valid hash found. Better luck next time!")
    return False

# ------------------------------------
# Entry Point
# ------------------------------------
if __name__ == "__main__":
    mine_simulation(WALLET_ADDRESS, difficulty=6)
