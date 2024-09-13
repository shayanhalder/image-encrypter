import api from "../api"
import { useState, useRef } from "react"
import Slider from "../components/Slider/Slider"

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
            let body = {
                file_name: fileName,
                message: message,
                username: localStorage.getItem("username"),
                override: false
            }
            formData.set('body', JSON.stringify(body))
            let response: postResponse = await api.post(ENDPOINT, formData)
            console.log('response: ', response)
            if (response.data.status == "409") {
                alert(response.data.text)
                const action = prompt(`Do you want to replace ${fileName}? `)
                if (action == "yes") {
                    body['override'] = true
                    console.log('new body: ', body)
                    formData.set('body', JSON.stringify(body))
                    response = await api.post(ENDPOINT, formData)
                }
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
            <div className="menu">
                <Slider left='Encrypt' right='Decrypt'></Slider>
                <input type='file' id='imageUpload' name='imageUpload' accept='image/*' ref={inputRef} onChange={handleFileChange} /> 
                {
                    mode == "Encrypt" && (
                        <>
                            <input type='text' placeholder="Insert file name here" value={fileName} onChange={handleNameChange} /> 
                            <textarea placeholder="Insert message here" value={message} onChange={(e) => setMessage(e.target.value)} />  
                        </>
                    )
                }
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