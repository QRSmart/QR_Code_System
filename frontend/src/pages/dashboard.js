import { React } from "react";
import AppCard from "../components/AppCard";

const Dashboard = () => {

    return (
        <div className="dashboard-page pages-app">
            <div className="greeting hdl-3 hdl-3--sbold">
                Hello Woody,
            </div>
            <div className="summary">
                <AppCard>
                    <div className="summary-ctn">
                        <p className="hdl-2 hdl-2--sbold"> Free Trial</p>
                        <p className="hdl-4 hdl-4--sbold"> (7 days remainings)</p>
                    </div>
                </AppCard>
                <AppCard>
                    <div className="summary-ctn">
                        <p className="hdl-2 hdl-2--sbold"> Total Scans</p>
                        <p className="hdl-4 hdl-4--sbold"> (3)</p>
                    </div>
                </AppCard>
                <AppCard>
                    <div className="summary-ctn">
                        <p className="hdl-2 hdl-2--sbold"> Dynamic QrCodes</p>
                        <p className="hdl-4 hdl-4--sbold"> 1 Acttive</p>
                    </div>
                </AppCard>
            </div>
        </div>
    )

}

export default Dashboard
