import { useCallback } from "react";
import { useDropzone } from "react-dropzone";
import { UploadCloud } from "lucide-react";

interface Props {
  onFilesSelected: (files: File[]) => void;
}

export default function UploadZone({
  onFilesSelected,
}: Props) {

const onDrop = useCallback((acceptedFiles: File[]) => {

    console.log("Files dropped:", acceptedFiles);

    onFilesSelected(acceptedFiles);

}, [onFilesSelected]);

  const {
    getRootProps,
    getInputProps,
    isDragActive,
  } = useDropzone({
    onDrop,
    multiple: true,
    accept: {
      "application/pdf": [".pdf"],
      "text/plain": [".txt"],
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        [".docx"],
    },
  });

  return (
    <div
      {...getRootProps()}
      className={`border-2 border-dashed rounded-2xl p-12 cursor-pointer transition

      ${
        isDragActive
          ? "border-blue-500 bg-blue-500/10"
          : "border-slate-700 hover:border-blue-500"
      }`}
    >
      <input {...getInputProps()} />

      <div className="flex flex-col items-center">

        <UploadCloud
          size={60}
          className="text-blue-500"
        />

        <h2 className="text-2xl font-semibold mt-4 text-white">
          Upload Documents
        </h2>

        <p className="text-slate-400 mt-2">
          Drag & Drop PDF, DOCX or TXT files
        </p>

        <button
          className="mt-6 bg-blue-600 hover:bg-blue-700 rounded-xl px-6 py-3 text-white"
        >
          Browse Files
        </button>

      </div>

    </div>
  );
}