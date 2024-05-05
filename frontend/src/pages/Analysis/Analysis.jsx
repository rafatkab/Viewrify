import { useState, useEffect } from "react";

export default function Analysis() {
  const [transcript, setTranscript] = useState();

  useEffect(() => {
    const fetchData = async () => {
      try {
        // Make a fetch request to your backend API
        const url = localStorage.getItem("url");
        const response = await fetch(
          `http://127.0.0.1:8000/api/${url.substring(30)}`
        );

        // Check if the response is successful
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        // Parse the JSON response
        const result = await response.json();

        // Update the state with the fetched data
        setTranscript(result);
      } catch (error) {
        // Handle any errors
        console.log(error);
      }
    };

    fetchData();
  }, []);

  return <div>{transcript}</div>;
}
