import { useState } from "react"
import styles from "./Slider.module.css"

export default function Slider({ left, right }: any){ 
    const [choice, setChoice] = useState<string>(left);
    const leftStyle = choice ==  left ? (" " + styles.selected) : ""
    const rightStyle = choice == right ? (" " + styles.selected) : ""

    function select(e : any) {
        console.log(e)
        setChoice(e.target.innerText);
    }

    return (
        <div className={styles.container}>
                <div className={styles.choice + leftStyle} onClick={select}>
                    {left}
                </div>
                <div className={styles.choice + rightStyle} onClick={select}>
                    {right}
                </div>
        </div>
    )
}