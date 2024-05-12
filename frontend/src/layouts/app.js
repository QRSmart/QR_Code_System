import { React } from "react";
import Sidebar from '../components/sidebar'
import Navbar from '../components/navbar'

const AppLayout = ({children}) => {

    return (
        <div className="app-container">
            <main className="app">
                <Sidebar/>
                <div className="app-content bd-md">
                    <Navbar/>
                    { children }
                </div>

            </main>
        </div>
    )

}

export default AppLayout
