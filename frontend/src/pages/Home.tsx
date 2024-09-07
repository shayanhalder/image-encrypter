import api from "../api"
import { useState, useRef } from "react"


interface postResponse {
    data: {
        status: string,
        text: string,
        url: string,
        message: string
    }
}


function Home() {
    const inputRef = useRef<HTMLInputElement>(null)
    const [message, setMessage] = useState<string>("")
    const [fileName, setFileName] = useState<string>("")
    const [imageURL, setImageURL] = useState<string>("")
    const [mode, setMode] = useState<string>("Encrypt")
    const [secretMessage, setSecretMessage] = useState<string>("")

    const ENDPOINT = mode === "Encrypt" ? '/api/encrypt-image-message/' : '/api/decrypt-image-message/'

    async function sendImage() {
        // console.log('username is: ', localStorage.getItem('username'))
        const formData = new FormData()
        if (inputRef.current && inputRef.current.files && mode == "Encrypt") {
            const file = inputRef.current.files[0]
            formData.append('file', file)
            const body = {
                file_name: fileName,
                message: message,
                username: localStorage.getItem("username")
            }
            formData.set('body', JSON.stringify(body))
            const response: postResponse = await api.post(ENDPOINT, formData)
            console.log('response: ', response)
            if (response.data.status == "409") {
                alert(response.data.text)
            }

            const url = response.data.url
            setImageURL(url)
        } else if (inputRef.current && inputRef.current.files) {
            const file = inputRef.current.files[0]
            formData.append('file', file)
            const body = {
                username: localStorage.getItem("username")
            }
            formData.set('body', JSON.stringify(body))
            const response: postResponse = await api.post(ENDPOINT, formData)
            console.log('response: ', response)
            setSecretMessage(response.data.message)
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
                <select onChange={(e) => setMode(e.target.value)}>
                    <option> Encrypt </option>
                    <option> Decrypt </option>
                </select>

                <label htmlFor='imageUpload'> Upload image file: </label> <br />
                <input type='file' id='imageUpload' name='imageUpload' accept='image/*' ref={inputRef} onChange={handleFileChange} /> <br />
                {
                    mode == "Encrypt" && (
                        <><input type='text' placeholder="Insert message here" value={message} onChange={(e) => setMessage(e.target.value)} /> <br /><br />
                            <input type='text' placeholder="Insert file name here" value={fileName} onChange={handleNameChange} /><br />
                        </>
                    )
                }
                <br />
                <button type='submit' onClick={sendImage}> Submit </button>
                {
                    secretMessage && (
                        <h3> Decrypted message: {secretMessage} </h3>
                    )
                }
            </div>
            <div>
                <img src={imageURL} />
            </div>

        </div>


    )
}


export default Home