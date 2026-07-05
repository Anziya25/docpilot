import type { ChatSource } from "../../types/chat";

interface Props {
    source: ChatSource;
}

export default function SourceCard({ source }: Props) {

    return (

        <div className="rounded-lg bg-slate-800 p-3 mt-2">

            <p className="text-blue-400">

                📄 {source.source}

            </p>

            <p className="text-sm text-slate-400">

                Page {source.page}

            </p>

        </div>

    );

}