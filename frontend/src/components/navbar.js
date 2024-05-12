import { React, useRef, useState} from "react"
import { Bell, UserRound, Settings, User } from "lucide-react"

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
                    {/* <h2 className="heading-2">QR<span className="text-qr-color">Smart</span></h2> */}
                    <ul>
                        <li>
                            <a href="/">Contact</a>
                        </li>
                        <li>
                            <a href="/">Help Center</a>
                        </li>
                        <li>
                            <button className="not-btn">
                                <Bell size={24}/>
                            </button>
                        </li>
                        <li>
                            <button className="user-profile-btn" data-count="2">
                                <UserRound size={24}/>
                            </button>
                        </li>
                        <li>
                            <button className="setting-btn">
                                <Settings size={24}/>
                            </button>
                        </li>
                    </ul>
                </nav>
            </div>
        </>
    )
}

export default Navbar;