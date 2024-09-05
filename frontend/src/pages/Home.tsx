import api from "../api"
import { useRef } from "react"

function Home() {
    const inputRef = useRef<HTMLInputElement>(null)


    async function sendImage() {
        const formData = new FormData()
        if (inputRef.current && inputRef.current.files) {
            const file = inputRef.current.files[0]
            formData.append('file', file)
            formData.set('body', '{"file_name": "test101.jpg"}')

            // const body = {
            //     'file': formData,
            //     'file_name': 'frontend_test.jpg'
            // }

            const response = await api.post('/api/encrypt-image-message/', formData)
            // const response = await api.post('/api/encrypt-image-message/', body)
            console.log('response: ', response)

        }


    }


    return (
        <div>
            <h1>Home</h1>
            <div>
                <label htmlFor='imageUpload'> Upload image file: </label> <br />
                <input type='file' id='imageUpload' name='imageUpload' accept='image/*' ref={inputRef} /> <br />
                <button type='submit' onClick={sendImage}> Submit </button>

            </div>

        </div>


    )
}


export default Home