from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

def encrypt_image_message(file: InMemoryUploadedFile, message: str) -> InMemoryUploadedFile:
    content = file.read()
    
    byte_stream = BytesIO(content)
    end_index = content.index(bytes.fromhex("FFD9"))
    byte_stream.seek(end_index + 2)    
    byte_stream.write(bytes(message, encoding='utf-8'))
    byte_stream.seek(0)
    
    encrypted_file = InMemoryUploadedFile(
        file=byte_stream,
        field_name=file.field_name,
        name=file.name,
        content_type=file.content_type,
        size=len(content),
        charset=file.charset
    )
    
    return encrypted_file
    
    
    
    
def decrypt_image_message(file: InMemoryUploadedFile) -> str:
    content:str = file.read()
    offset = content.index(bytes.fromhex("FFD9"))
    
    file.seek(offset + 2) 
    
    output = file.read()
    return output.decode()
    
     



