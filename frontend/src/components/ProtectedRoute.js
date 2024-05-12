import { Navigate } from "react-router-dom";
import { useAuth } from "../hooks/useAuth";

export const ProtectedRoute = ({ children }) => {
    const { user, token } = useAuth();
    if (!user || !token) {
        return <Navigate to="/login" />;
    }
    return children;
};