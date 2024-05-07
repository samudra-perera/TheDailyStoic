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
    <div className="min-h-screen flex justify-center bg-stone-50">
      <div className="max-w-3xl p-6 py-14 pt-10">
        <Markdown
          options={{
            overrides: {
              h1: {
                component: "h1",
                props: {
                  className:
                    "text-blue-950 text-2xl lg:text-3xl text-center pb-2",
                },
              },
              h2: {
                component: "h2",
                props: {
                  className:
                    "text-center text-xl lg:text-2xl pb-2 text-blue-800 border-solid border-0 border-b border-blue-900 mb-2 lg:mb-6",
                },
              },
              blockquote: {
                component: "blockquote",
                props: {
                  className: "p-6 pb-0 italic text-zinc-500",
                },
              },
              p: {
                component: "p",
                props: {
                  className: "pb-6",
                },
              },
              ul: {
                component: "ul",
                props: {
                  className: "italic pb-6 list-disc pl-5 text-blue-950",
                },
              },
            },
          }}
        >
          {content}
        </Markdown>
      </div>
    </div>
  );
};

export default App;
