import type { ChatMessage as Message } from "../../types/chat";
import SourceCard from "./SourceCard";

interface Props {
    message: Message;
}

export default function ChatMessage({
    message,
}: Props) {

    const user = message.role === "user";

    return (

        <div
            className={`mb-6 flex ${user ? "justify-end" : "justify-start"
                }`}
        >

            <div
                className={`max-w-3xl rounded-2xl p-5 ${user
                        ? "bg-blue-600"
                        : "bg-slate-800"
                    }`}
            >

                <p className="whitespace-pre-wrap">

                    {message.content}

                </p>

                {message.sources?.map((source, index) => (

                    <SourceCard
                        key={index}
                        source={source}
                    />

                ))}

            </div>

        </div>

    );

}