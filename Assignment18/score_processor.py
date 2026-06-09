class ScoreProcessor:

    def process_score_file(self, file_path: str) -> int:
        file = None

        try:
            # Open the file
            file = open(file_path, "r")

            # Read and clean file content
            content = file.read().strip()

            # Convert content to integer
            score = int(content)

            # Multiply score by 10
            result = score * 10

        except FileNotFoundError:
            print("Error: File not found.")
            raise

        except ValueError:
            print("Error: Invalid data format. File must contain a number.")
            raise

        else:
            print("Data processed successfully")
            return result

        finally:
            # Cleanup block
            if file:
                file.close()

            print("File cleanup completed")


# Main execution
if __name__ == "__main__":

    processor = ScoreProcessor()

    result = processor.process_score_file("score.txt")

    print("Final Result:", result)