import hashlib
import time
from tqdm import tqdm
from sklearn.linear_model import LinearRegression
import numpy as np

# ------------------------------------
# User-defined wallet address
# ------------------------------------
WALLET_ADDRESS = "YOUR_BITCOIN_WALLET_ADDRESS_HERE"

# ------------------------------------
# Simulated Mining (Proof of Work)
# ------------------------------------
def mine_block(wallet_address, difficulty=5):
    prefix = '0' * difficulty
    block_data = f"Simulated block data with wallet: {wallet_address}"

    print(f"\n[⛏️ ] Mining started... Difficulty: {difficulty}")
    for nonce in tqdm(range(10000000)):
        block = f'{block_data}{nonce}'.encode()
        hash_result = hashlib.sha256(block).hexdigest()
        if hash_result.startswith(prefix):
            print(f"\n🎉 Lucky hit! You mined a block!")
            print(f"✅ Nonce: {nonce}")
            print(f"✅ Hash: {hash_result}")
            print(f"💸 Reward sent to: {wallet_address}")
            return nonce, hash_result
    print("\n[!] Mining simulation complete. No valid nonce found.")
    return None, None

# ------------------------------------
# ML BTC Price Predictor
# ------------------------------------
def simulate_ml_prediction():
    print("\n[📊] Predicting BTC price with ML (linear regression)...")

    # Dummy BTC price data (for 10 days)
    X = np.array([[i] for i in range(1, 11)])
    y = np.array([30000, 30500, 31000, 31500, 32000, 31800, 32200, 32500, 32800, 33000])

    model = LinearRegression()
    model.fit(X, y)

    prediction_day = np.array([[11]])
    predicted_price = model.predict(prediction_day)
    print(f"📈 Predicted BTC Price on Day 11: ${predicted_price[0]:.2f}")
    return predicted_price[0]

# ------------------------------------
# Main Execution
# ------------------------------------
def main():
    print("\n==== 💻 BITCOIN MINER SIMULATOR + ML ====")
    print(f"[+] Using your wallet: {WALLET_ADDRESS}")
    
    simulate_ml_prediction()
    nonce, result_hash = mine_block(WALLET_ADDRESS, difficulty=5)

    if result_hash:
        print(f"\n✅ Block mined with hash: {result_hash}")
    else:
        print(f"\n❌ No luck this time. Try again!")

if __name__ == "__main__":
    main()
