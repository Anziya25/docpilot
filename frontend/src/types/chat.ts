export interface ChatSource {
    source: string;
    page?: number;
    file_type?: string;
}

export interface ChatMessage {
    role: "user" | "assistant";
    content: string;
    sources?: ChatSource[];
}