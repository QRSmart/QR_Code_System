
import { api } from "./api";

export const signup = async (credentials) => {
    const response = await api().post("/auth/register", credentials)
    .then((res)=> {
        console.log(res)
        return res.data
    })
    .catch((err) => {
        throw err
    })
    return response
}


export const  signin = async (creadentials) => {

}