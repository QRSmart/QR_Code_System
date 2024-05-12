import { React, useState } from "react";
//import Navbar from "../components/navbar";
//import Footer from "../components/footer";
import qrasset from "../assets/img/qr-asset-login.png"
import googleIcon from "../assets/img/google-icon.svg";
//import useSWR from 'swr'
import { signup } from "../services/auth";
import { useMutation } from 'react-query'
import { useNavigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";
import { firebaseSignIn } from "../services/firebase/auth";


const Signup = () => {

    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const navigate = useNavigate()
    const {setUser, setToken} = useAuth()
    /*const { data, error } = useSWR(
        `${process.env.REACT_APP_API_URL}/auth/register`,  // Pass body data here
    );*/
    const signupMutation = useMutation(userData => signup(userData), {
        onSuccess: async (data, variables, context) => {
            console.log(data)
            if (data.success) {
                //setToken(data.data.token)
                //setUser(data.data.user)
                const userData = await firebaseSignIn({
                    email: email,
                    password: password
                })
                if (userData && userData.accessToken) {
                    setUser(userData)
                    setToken(userData.accessToken)
                    navigate("/dashboard")
                }
            }
        }
    })
    const handleSignup = async (e) => {
        e.preventDefault()
        signupMutation.mutate({ 
            user: {
                email: email,
                password: password
            }
        })
    }

    return (
        <div className="signup-page">
            <main>
                <form className="formCtn flex flex-col justify-center items-center w-1/2 " onSubmit={handleSignup}>
                    <h2 className="hdl-2 text-qr-dark">QR<span className="text-qr-color">Smart</span></h2>
                    <div className="inner-form flex flex-col items-center justify-center text-qr-dark">
                        <h2 className="hdl-2 hdl-2--sbold text-qr-dark">Get started for free now!</h2>
                        <div className="formInput">
                            <label>Email</label>

                            <input className="input-form" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
                        </div>
                        <div className="formInput">
                            <label>Password</label>
                            <input className="input-form" type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)}/>
                            
                        </div>
                        <div className="submitInput">
                            <button className="btn-default">
                                Signup
                            </button>
                        </div>
                        <div className="account-new bd-foot">
                            Already have an accoount Login <a href="/login" className="">here</a>
                        </div>
                        <hr/>
                        <a href="/" className="google-signin">
                            <img src={googleIcon} alt="google-icon"/>
                            <span>Signup with google</span>
                        </a>
                        <div className="terms bd-foot">
                            By creating an account, you consent that you have read and agree to our <a  href="/">terms of use</a> and contract and the <a href="/">privacy policy</a>.
                        </div>
                    </div>
                </form>
                <div className="form-illus flex flex-col justify-center items-center w-1/2 h-full">
                    <img src={qrasset} alt="qr-smart"/>
                    <h2 className="hdl-3">
                        Customers has never been easy to reach 
                    </h2>
                    <h4 className="bd-md">Scale your business without limits</h4>
                </div>

            </main>
        </div>
    )

}

export default Signup
