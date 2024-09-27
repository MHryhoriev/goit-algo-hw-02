from queue import Queue
import uuid
import time
import random

def generate_unique_id() -> str:
    """
    Generate a unique identifier using UUID4.

    Returns:
        str: A string representation of the unique identifier.
    """
    return str(uuid.uuid4())

def generate_request(queue: Queue) -> None:
    """
    Generate a new request with a unique identifier and add it to the queue.

    Args:
        queue (Queue): The queue to which the request will be added.

    Returns:
        None
    """
    request_id = generate_unique_id()
    queue.put(request_id)
    print(f"The request with the unique identifier '{request_id}' has been successfully added to the queue for processing.")

def process_request(queue: Queue) -> None:
    """
    Process a request from the queue.

    Args:
        queue (Queue): The queue from which the request will be processed.

    Returns:
        None
    """
    if queue.empty():
        print("The request could not be processed: the queue is empty. Please add requests to the queue first.")
    else:
        processed_request = queue.get()
        print(f"The request with the unique identifier '{processed_request}' was successfully processed.")

def main():
    queue = Queue()
    
    for _ in range(10):
        generate_request(queue)
        time.sleep(random.uniform(0.5, 1.5))

    print("\nThe processing of requests begins...\n")
        
    while not queue.empty():
        process_request(queue)
        time.sleep(random.uniform(0.5, 1.5))

    print("\nAll requests have been processed.")

if __name__ == "__main__":
    main()
