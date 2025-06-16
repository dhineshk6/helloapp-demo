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
    print("[+] Wallet: {}".format(wallet_address))
    print("[+] Difficulty: {} (requires hash starting with {})".format(difficulty, '0' * difficulty))
    print("[*] Starting mining...\n")

    prefix = '0' * difficulty
    start_time = time.time()

    for attempt in range(1, max_attempts + 1):
        nonce = random.randint(0, 1_000_000_000)
        data = "{}{}".format(wallet_address, nonce).encode()
        hash_result = hashlib.sha256(data).hexdigest()

        if hash_result.startswith(prefix):
            elapsed = time.time() - start_time
            print("🎉 BLOCK MINED!")
            print("🧠 Nonce: {}".format(nonce))
            print("🔗 Hash: {}".format(hash_result))
            print("💰 Reward (simulated): Sent to wallet {}".format(wallet_address))
            print("⏱️ Time taken: {:.2f} seconds".format(elapsed))
            return True

        if attempt % 500000 == 0:
            print("[{}/{}] Still mining...".format(attempt, max_attempts))

    print("\n❌ No valid hash found. Better luck next time!")
    return False

# ------------------------------------
# Entry Point
# ------------------------------------
if __name__ == "__main__":
    mine_simulation(WALLET_ADDRESS, difficulty=6)
