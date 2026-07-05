import DocumentCard from "./DocumentCard";
import  type { DocumentFile } from "../../types/document";

interface Props {
  documents: DocumentFile[];
}

export default function DocumentList({ documents }: Props) {
  return (
    <div className="space-y-3">

      <h2 className="text-xl font-semibold text-white">
        Uploaded Documents
      </h2>

      {documents.length === 0 && (
        <p className="text-slate-400">
          No documents uploaded.
        </p>
      )}

      {documents.map((doc) => (
        <DocumentCard
          key={doc.id}
          name={doc.name}
        />
      ))}
    </div>
  );
}