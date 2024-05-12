//import Navbar from "../components/navbar";
//import Footer from "../components/footer";
import qrasset from "../assets/img/qr-asset-login.png"
import googleIcon from "../assets/img/google-icon.svg"
import { useAuth } from "../hooks/useAuth";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useMutation } from "react-query";
import { firebaseSignIn } from "../services/firebase/auth";

const Login = () => {
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [isSignIn, setIsSignIn] = useState(false)
    const navigate = useNavigate()
    const {setUser, setToken} = useAuth()
    //console.log(auth)

    const signinMutation = useMutation(async (credentials)=> {
        return await firebaseSignIn(credentials)
    }, {
        onSuccess: (data, variables, context) => {
            console.log(data)
            if (data && data.accessToken) {
                setUser(data)
                setToken(data.accessToken)
                navigate('/dashboard')
            }
        }
    })

    const handleLogin = (e) => {
        e.preventDefault();
        // Login
        setIsSignIn(true)
        //return
        signinMutation.mutate({email : email, password: password})
    }

    return (
        <div className="login-page">
            <main>
                <div className="form-illus flex flex-col justify-center items-center w-1/2 h-full">
                    <img src={qrasset} alt="qr-smart"/>
                    <h2 className="hdl-3">
                        QRSmart is your all in one qrcode generator 
                    </h2>
                    <h4 className="bd-md">Generate easily your qr codes </h4>
                </div>
                <form className="formCtn flex flex-col justify-center items-center w-1/2 " onSubmit={handleLogin}>
                    <h2 className="hdl-2 text-qr-dark">QR<span className="text-qr-color">Smart</span></h2>
                    <div className="inner-form flex flex-col items-center justify-center text-qr-dark">
                        <h2 className="hdl-2 hdl-2--sbold text-qr-dark">Great to see you again!</h2>
                        <div className="formInput">
                            <label>Email</label>

                            <input className="input-form" type="email" placeholder="Email" value={email} onChange={(e)=> setEmail(e.target.value)}/>
                        </div>
                        <div className="formInput">
                            <label>Password</label>
                            <input className="input-form" type="password" placeholder="Password" value={password} onChange={(e)=> setPassword(e.target.value)}/>
                            <a href="/" className="forgot bd-foot"> Forgot Password?</a>
                        </div>
                        <div className="submitInput">
                            <button className="btn-default" disabled={isSignIn}>
                                { !isSignIn ? 'Login' : 'Login...'}
                            </button>
                        </div>
                        <div className="account-new bd-foot">
                            Don't have an account <a href="/signup" className="">Signup here</a>
                        </div>
                        <hr/>
                        <a href="/" className="google-signin">
                            <img src={googleIcon} alt="google-icon"/>
                            <span>Signin with google</span>
                        </a>
                    </div>
                </form>

            </main>
        </div>
    )

}

export default Login
