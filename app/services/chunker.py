"""
Text Chunker

Splits LangChain Documents into
smaller chunks for embedding.
"""

from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class TextChunker:
    """
    Splits documents into smaller chunks.
    """

    def __init__(self):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=CHUNK_SIZE,

            chunk_overlap=CHUNK_OVERLAP,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split LangChain Documents into smaller chunks.
        """

        chunks = self.splitter.split_documents(documents)

        return chunks