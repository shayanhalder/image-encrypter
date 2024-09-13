import styles from "./Slider.module.css"

export default function Slider({ choice, setChoice }: any){ 
    const leftStyle = choice ==  "Encrypt" ? (" " + styles.selected) : ""
    const rightStyle = choice == "Decrypt" ? (" " + styles.selected) : ""

    function select(e : any) {
        console.log(e)
        setChoice(e.target.innerText);
    }

    return (
        <div className={styles.container}>
                <div className={styles.choice + leftStyle} onClick={select}>
                    Encrypt
                </div>
                <div className={styles.choice + rightStyle} onClick={select}>
                    Decrypt
                </div>
        </div>
    )
}