import { React } from "react"
import { Home, QrCode, BarChart3, FolderClosed, Plus } from 'lucide-react'
const Sidebar = () => {


    return (
        <>
            <div className="sidebar-app">
                <div className="logo-ctn">
                    <h2 className="hdl-2 hdl-2--sbold">QR<span className="text-qr-color">Smart</span></h2>
                </div>
                <div className="menu-ctn">
                    <div className="action-item">
                        <button className="sidebar-item sidebar-item--permanent">
                            <Plus size={16}/>
                            Create QR
                        </button>
                    </div>
                    <ul className="nav-items">
                        <li><a href="/" className="sidebar-item sidebar-item--active"><Home size={16}/> Dashboard</a></li>
                        <li><a href="/" className="sidebar-item sidebar-item--default"><QrCode size={16}/> My QR codes</a></li>
                        <li><a href="/" className="sidebar-item sidebar-item--default"><BarChart3 size={16}/> Stats</a></li>
                        <li><a href="/" className="sidebar-item sidebar-item--default"><FolderClosed size={16}/> Folders</a></li>
                    </ul>
                </div>
            </div>
        </>
    )
}

export default Sidebar