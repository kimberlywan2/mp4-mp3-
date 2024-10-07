import os
from moviepy.editor import VideoFileClip

def mp4_to_mp3_converter():
    print("Welcome to the MP4 to MP3 Converter")

    while True:
        # Download MP4 file (in this case, we'll ask for the file path)
        mp4_path = input("Enter the path to your MP4 file: ")
        
        if not os.path.exists(mp4_path):
            print("File not found. Please ensure the path is correct.")
            continue

        # Extract audio from MP4 and convert to MP3
        try:
            video = VideoFileClip(mp4_path)
            audio = video.audio
            
            # Generate output MP3 filename
            mp3_path = os.path.splitext(mp4_path)[0] + ".mp3"
            
            # Convert audio to MP3
            audio.write_audiofile(mp3_path)
            
            # Close the video file
            video.close()
            
            print(f"MP3 file has been saved as: {mp3_path}")
        except Exception as e:
            print(f"An error occurred during conversion: {str(e)}")
            continue

        # Ask if the user wants to convert another file
        another = input("Do you want to convert another file? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you for using the MP4 to MP3 Converter. Goodbye!")

# Run the converter
if __name__ == "__main__":
    mp4_to_mp3_converter()
