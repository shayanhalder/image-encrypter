import api from "../api"
import { useRef } from "react"

function Home() {
    const inputRef = useRef<HTMLInputElement>(null)


    async function sendImage() {
        const formData = new FormData()
        if (inputRef.current && inputRef.current.files) {
            // console.log('ref: ', inputRef.current.files[0])
            const file = inputRef.current.files[0]
            // console.log('file: ', file)?
            formData.append('file', file)
            const response = await api.post('/api/encrypt-image-message/', formData)
            console.log('response: ', response)
            // const blob = response.blob()

            // if (response.status === 200) {
            //     localStorage.setItem(ACCESS_TOKEN, res.data.access)
            //     setIsAuthorized(true)
            // } else {
            //     setIsAuthorized(false)
            // }



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