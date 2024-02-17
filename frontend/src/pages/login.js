import { React } from "react";
//import Navbar from "../components/navbar";
//import Footer from "../components/footer";
import qrasset from "../assets/img/qr-asset-1.svg"

const Login = () => {

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
                <form className="formCtn flex flex-col justify-center items-center w-1/2">
                    <h2 class="hdl-2 text-qr-dark">QR<span class="text-qr-color">Smart</span></h2>
                    <div className="inner-form flex flex-col items-center justify-center text-qr-dark">
                        <h2 className="hdl-1 text-qr-dark">Login</h2>
                        <div className="formInput">
                            <label>Email</label>

                            <input className="input-form" type="email" placeholder="Email"/>
                        </div>
                        <div className="formInput">
                            <label>Password</label>
                            <input className="input-form" type="password" placeholder="Password"/>
                        </div>
                        <div className="submitInput">
                            <button className="btn-default">
                                Login
                            </button>
                            
                        </div>
                    </div>
                </form>

            </main>
        </div>
    )

}

export default Login
