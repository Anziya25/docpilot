import { useState } from "react";
import { Send } from "lucide-react";

interface Props {
    onSend: (question: string) => void;
    disabled?: boolean;
}

export default function ChatInput({
    onSend,
    disabled = false,
}: Props) {

    const [question, setQuestion] = useState("");

    const send = () => {

        if (!question.trim()) return;

        onSend(question);

        setQuestion("");
    };

    return (

        <div className="flex gap-3">

            <input
                value={question}
                onChange={(e) => setQuestion(e.target.value)}
                onKeyDown={(e) => {

                    if (e.key === "Enter") send();

                }}
                placeholder="Ask anything..."
                className="flex-1 rounded-xl border border-slate-700 bg-slate-900 p-4 text-white outline-none"
            />

            <button
                onClick={send}
                disabled={disabled}
                className="rounded-xl bg-blue-600 px-5 text-white hover:bg-blue-700"
            >

                <Send size={18} />

            </button>

        </div>

    );
}