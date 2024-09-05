import api from "../api"
import { useState, useRef } from "react"

function Home() {
    const inputRef = useRef<HTMLInputElement>(null)
    const [message, setMessage] = useState<string>("")
    const [fileName, setFileName] = useState<string>("")

    async function sendImage() {
        const formData = new FormData()
        if (inputRef.current && inputRef.current.files) {
            const file = inputRef.current.files[0]
            formData.append('file', file)
            formData.set('body', `{"file_name": "${fileName}"}`)
            const response = await api.post('/api/encrypt-image-message/', formData)
            console.log('response: ', response)
        }
    }


    function handleFileChange(e: any) {
        const uploadName = e.target.files[0].name
        setFileName(uploadName);
    }

    function handleNameChange(e: any) {
        setFileName(e.target.value)
    }


    return (
        <div>
            <h1>Home</h1>
            <div>
                <label htmlFor='imageUpload'> Upload image file: </label> <br />
                <input type='file' id='imageUpload' name='imageUpload' accept='image/*' ref={inputRef} onChange={handleFileChange} /> <br />
                <input type='text' placeholder="Insert message here" value={message} onChange={(e) => setMessage(e.target.value)} />
                <input type='text' placeholder="Insert file name here" value={fileName} onChange={handleNameChange} />
                <button type='submit' onClick={sendImage}> Submit </button>

            </div>

        </div>


    )
}


export default Home