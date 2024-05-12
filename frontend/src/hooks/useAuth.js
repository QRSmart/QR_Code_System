import { Outlet, useNavigate } from "react-router-dom"
import { useLocalStorage } from "./useLocalStorage"
import { createContext, useContext, useMemo } from "react"

const AuthContext = createContext()

const AuthProvider = ({ children }) => {
    const [user, setUser] = useLocalStorage("user", null)
    const [token, setToken] = useLocalStorage("token", null)
    const navigate = useNavigate()
    
    // call this function when you want to authenticate the user
    /*const login = async (data) => {
        setUser(data);
        navigate("/profile");
    };*/

    // call this function to sign out logged in user
    /*const logout = () => {
        setUser(null);
        navigate("/", { replace: true });
    };*/
    const value = useMemo(() => ({
            user,
            setUser,
            token,
            setToken,
            //login,
            //logout,
        }),
        [user, setUser, token, setToken]
    );
    return <AuthContext.Provider value={value}>
        <Outlet/>
    </AuthContext.Provider>;
}

const useAuth = () => {
    return useContext(AuthContext)
}

export {
    AuthProvider,
    useAuth
}

