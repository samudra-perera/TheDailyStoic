import formatDate from "../utils/DateFormatter";
import { useEffect, useState } from "react";
import Markdown from "markdown-to-jsx";

const App = () => {
  const [content, setContent] = useState<string>("");
  const today = new Date();

  useEffect(() => {
    const date_format = formatDate(today);
    const page_location = `/Markdown_Files/${date_format}.md`;

    fetch(page_location)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Failed to fetch md file");
        }
        return res.text();
      })
      .then((text) => setContent(text))
      .catch((err) => {
        console.error("Error fetching markdown", err);
        setContent("Failed to load the content");
      });
  }, [today]);

  return (
    <div className="min-h-screen flex justify-center">
      <div className="max-w-3xl p-4 py-14">
        <Markdown>{content}</Markdown>
      </div>
    </div>
  );
};

export default App;
