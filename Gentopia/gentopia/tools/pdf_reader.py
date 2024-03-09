# Recreated using file_operation.py and PyPDF2 resource

from typing import AnyStr
from PyPDF2 import PdfReader
from gentopia.tools.basetool import *

class PDFReadArgs(BaseModel):
    file_path: str = Field(..., description="path to read the pdf")

class PDFReader(BaseTool):
    """reads pdf from disk"""

    name = "pdf_reader"
    description = "Read pdf from hardisk."

    args_schema: Optional[Type[BaseModel]] = PDFReadArgs

    def _run(self, file_path) -> AnyStr:
        try:
            text = ''
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            return f"Failed to read PDF file: {str(e)}"

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError

if __name__ == "__main__":
    pdf = PDFReader()._run("dummy_smallpdf.pdf")
    # pdf_text = PDFReader()._run(pdf_path)
    print(pdf)
