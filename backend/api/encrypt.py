from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO

def encrypt_image_message(file: InMemoryUploadedFile, message: str) -> InMemoryUploadedFile:
    file_content = file.read()
    
    file_content += bytes(message, encoding='utf-8')
    byte_stream = BytesIO(file_content) 
    
    encrypted_file = InMemoryUploadedFile(
        file=byte_stream,
        field_name=file.field_name,
        name=file.name,
        content_type=file.content_type,
        size=len(file_content),
        charset=file.charset
    )
    
    return encrypted_file
    # new_content = bytes.fromhex("FFD8 FFFE 0022") + bytes.fromhex("5468 6973 4973 4153 7570 6572 5365 6372 6574 4465 6372 7970 7469 6F6E4B657921")
    # index = file_content.index(bytes.fromhex("FFD8"))
    # file.seek(index + 2)
    # remaining = file.read()
    # print('type of remaining: ', type(remaining))
    # print('remaining first line: ', remaining[:20])
    
    # new_content += remaining
    # content = file.read()
    
    
    
def decrypt_image_message(file: InMemoryUploadedFile) -> str:
    content:str = file.read()
    offset = content.index(bytes.fromhex("FFD9"))
    
    file.seek(offset + 2) 
    
    output = file.read()
    return output.decode()
    
     



