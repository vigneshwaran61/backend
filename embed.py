import subprocess
import argparse
import os
import sys

def embed_hmac_metadata(input_path, output_path, hmac_value):
    cmd = [
        "ffmpeg", "-i", input_path,
        "-metadata", f"video_hmac={hmac_value}",
        "-c", "copy", output_path
    ]
    subprocess.run(cmd, check=True)

def main():
    parser = argparse.ArgumentParser(description="Embed combined ID as metadata into a video file.")
    parser.add_argument("input", help="Path to the input video file")
    parser.add_argument("combinedId", help="Combined ID in the form <hash>&<wallet_address>")

    args = parser.parse_args()
    input_file = args.input
    combined_id = args.combinedId

    # Extract wallet address
    try:
        file_hash, wallet_address = combined_id.split("&")
    except ValueError:
        print("Invalid combinedId format. Use: <hash>&<wallet_address>")
        sys.exit(1)

    # Create output directory for the wallet if it doesn't exist
    wallet_folder = os.path.join("/home/ubuntu/watermarked", wallet_address)
    os.makedirs(wallet_folder, exist_ok=True)

    # Output file path in wallet's folder
    filename = os.path.basename(input_file)
    output_file = os.path.join(wallet_folder, filename)

    try:
        embed_hmac_metadata(input_file, output_file, combined_id)
        print(f"✅ Watermarked video saved to: {output_file}")
    except subprocess.CalledProcessError:
        print("❌ Failed to watermark video. Please check the input file and FFmpeg installation.")

if __name__ == "__main__":
    main()
