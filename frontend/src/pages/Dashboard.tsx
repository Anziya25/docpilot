import { useState } from "react";

import Layout from "../components/layout/Layout";

import UploadZone from "../components/documents/UploadZone";
import DocumentList from "../components/documents/DocumentList";

import ChatWindow from "../components/chat/ChatWindow";
import ChatInput from "../components/chat/ChatInput";

import api from "../services/api";

import type { DocumentFile } from "../types/document";
import type { ChatMessage } from "../types/chat";

export default function Dashboard() {

  const [documents, setDocuments] = useState<DocumentFile[]>([]);
  const [messages, setMessages] = useState<ChatMessage[]>([]);

  const [uploading, setUploading] = useState(false);
  const [building, setBuilding] = useState(false);
  const [asking, setAsking] = useState(false);

  const [status, setStatus] = useState("Waiting for upload...");

  // ==========================================
  // Upload
  // ==========================================

  const uploadFiles = async (files: File[]) => {

    console.log("uploadFiles called");
    console.log(files);

    if (files.length === 0) return;

    setUploading(true);
    setStatus("Uploading...");

    try {

      for (const file of files) {

        console.log("Uploading:", file.name);

        const formData = new FormData();

        formData.append("file", file);

        const response = await api.post("/upload", formData);

        console.log(response.data);

        console.log("Upload Success");

        setDocuments(prev => [

          ...prev,

          {
            id: Date.now().toString(),
            name: file.name,
            type: file.type,
          }

        ]);

      }

      setStatus("Upload Successful");

    }

    catch (error: any) {

      console.log("========== ERROR ==========");

      console.log(error);

      console.log(error.response);

      console.log(error.response?.status);

      console.log(error.response?.data);

      console.log(error.message);

      setStatus("Upload Failed");

    }

    finally {

      setUploading(false);

    }

  };

  // ==========================================
  // Build Vector Store
  // ==========================================

  const buildKnowledgeBase = async () => {

    if (documents.length === 0) {

      alert("Upload a document first.");

      return;

    }

    setBuilding(true);

    setStatus("Building Knowledge Base...");

    try {

      const response = await api.post("/index");

      console.log(response.data);

      setStatus("Knowledge Base Ready");

    }

    catch (error) {

      console.error(error);

      setStatus("Knowledge Base Failed");

    }

    finally {

      setBuilding(false);

    }

  };

  // ==========================================
  // Chat
  // ==========================================

  const askQuestion = async (question: string) => {

    if (!question.trim()) return;

    setMessages(prev => [

      ...prev,

      {

        role: "user",

        content: question,

      }

    ]);

    setAsking(true);

    try {

      const response = await api.post("/chat", {

        question,

      });

      setMessages(prev => [

        ...prev,

        {

          role: "assistant",

          content: response.data.answer,

          sources: response.data.sources,

        }

      ]);

    }

    catch (error) {

      console.error(error);

    }

    finally {

      setAsking(false);

    }

  };

  return (

    <Layout>

      <div className="grid grid-cols-3 gap-8">

        <div className="space-y-6">

          <DocumentList documents={documents} />

          <button
            onClick={buildKnowledgeBase}
            disabled={building || uploading}
            className="w-full rounded-xl bg-green-600 py-3 font-semibold text-white hover:bg-green-700 disabled:bg-gray-500"
          >
            {building ? "Building..." : "Build Knowledge Base"}
          </button>

          <div className="rounded-xl border border-slate-700 bg-slate-900 p-5">

            <h3 className="text-lg font-semibold text-white">

              Status

            </h3>

            <p className="mt-2 text-slate-400">

              {status}

            </p>

          </div>

        </div>

        <div className="col-span-2 space-y-6">

          <UploadZone

            onFilesSelected={uploadFiles}

          />

          {uploading && (

            <div className="rounded-xl bg-blue-600 p-4 text-center text-white">

              Uploading...

            </div>

          )}

          <ChatWindow

            messages={messages}

          />

          <ChatInput

            onSend={askQuestion}

            disabled={asking}

          />

        </div>

      </div>

    </Layout>

  );

}