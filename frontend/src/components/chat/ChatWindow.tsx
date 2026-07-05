import type { ChatMessage } from "../../types/chat";
import ChatMessageComponent from "./ChatMessage";

interface Props {
    messages: ChatMessage[];
}

export default function ChatWindow({
    messages,
}: Props) {

    return (

        <div className="rounded-xl border border-slate-700 bg-slate-900 p-6 min-h-[500px]">

            <h2 className="mb-6 text-xl font-bold text-white">

                AI Chat

            </h2>

            {messages.length === 0 && (

                <p className="text-slate-400">

                    Ask anything about your uploaded documents.

                </p>

            )}

            {messages.map((message, index) => (

                <ChatMessageComponent
                    key={index}
                    message={message}
                />

            ))}

        </div>

    );

}