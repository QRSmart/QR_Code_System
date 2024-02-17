import { React, useRef, useState} from "react"


const Navbar = () => {

    const [state, setState] = useState(false)
    const navRef = useRef()

    // Replace # path with your path
    const navigation = [
        { 
            title: "About Us", 
            path: "/About" 
        },
        { 
            title: "FAQs", 
            path: "/swagger/index.html" 
        },
        { 
            title: "Contact Us", 
            path: "/swagger/index.html" 
        },
    ]

    

    return (
        <>
            <div className="navbar" id="navbar">
                <nav className="body-font">
                    <h2 className="heading-2">QR<span className="text-qr-color">Smart</span></h2>
                    <ul>
                        {
                                navigation.map((item, idx) => {
                                    return (
                                        <li key={idx} className="nav-text">
                                            <a href={item.path}>
                                                { item.title }
                                            </a>
                                        </li>
                                    )
                                })
                            }
                    </ul>
                    <div className="connexion">
                        <a className="btn-default">Login</a>
                        <a className="btn-primary">Signup</a>

                    </div>
                </nav>
            </div>
        </>
    )
}

export default Navbar;