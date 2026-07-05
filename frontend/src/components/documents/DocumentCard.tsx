import { FileText } from "lucide-react";

interface Props {
  name: string;
}

export default function DocumentCard({ name }: Props) {
  return (
    <div className="flex items-center gap-3 rounded-xl bg-slate-900 border border-slate-800 p-4">

      <FileText className="text-blue-500" size={22} />

      <span className="text-white">{name}</span>

    </div>
  );
}