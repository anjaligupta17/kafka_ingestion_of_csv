from kafka import KafkaProducer
import time
import csv

def main():
    # Kafka broker address
    bootstrap_servers = 'kafka:9092'
    # Kafka topic name
    topic = 'test_topic'

    # Create KafkaProducer instance
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Open the file in append mode
    with open('xyz.txt', 'a') as file:
        try:
            while True:
                data = read_csv_data()
                
                # Send data to Kafka topic
                producer.send(topic, value=data.encode())
                print(f"Produced to Kafka: {data}")

                # Write data to the text file
                file.write(data + '\n')
                file.flush()  # Flush buffer to ensure immediate write
                print(f"Written to file: {data}")

                time.sleep(1)  # Adjust the delay as needed
        except KeyboardInterrupt:
            print("Stopping producer...")
        except Exception as e:
            print(f"Error writing to file: {e}")
        finally:
            producer.close()

def read_csv_data():
    # Replace 'data.csv' with the path to your CSV file
    with open('/app/data/data.csv', 'r') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            # Append each row to the data list
            data.append(','.join(row))
        # Join all rows into a single string separated by newline characters
        return '\n'.join(data)

if __name__ == "__main__":
    main()
