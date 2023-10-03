import numpy as np
from onnxruntime import InferenceSession
from transformers import AutoTokenizer
import faiss

from app.config import paths, Parms
from app.utility.utils import ModelProcessor


class EmbeddingModel:
    def __init__(self):
        super().__init__()
        self.onnx_path = str(paths.MODEL_DIR.joinpath("encoder.onnx_uint8.onnx"))
        self.faiss_path = str(paths.FAISS_DIR.joinpath("faiss_onnx_uint8"))

        self.sess = InferenceSession(self.onnx_path, providers=["CPUExecutionProvider"])
        self.tokenizer = AutoTokenizer.from_pretrained(paths.MODEL_DIR)
        self.faiss_index = faiss.read_index(self.faiss_path)

    def encode(self, query: str, normalize_embeddings=True) -> np.ndarray:
        model_inputs = self.tokenizer(query, return_tensors="pt")
        inputs_onnx = {k: v.cpu().detach().numpy() for k, v in model_inputs.items()}
        sequence = self.sess.run(None, inputs_onnx)
        query_embedding = ModelProcessor.mean_pooling(
            sequence, inputs_onnx["attention_mask"]
        )[0][0]

        if normalize_embeddings:
            query_embedding = query_embedding / np.linalg.norm(query_embedding)

        return query_embedding

    def search(self, query: str):
        embedding = np.expand_dims(self.encode(query), axis=0)
        _, ids = self.faiss_index.search(embedding, Parms.TOP_K)
        return ids[0].tolist()