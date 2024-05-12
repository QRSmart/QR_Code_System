import axios from 'axios';

export const api = () =>  {
    const axiosInstance = axios.create({ 
        baseURL : `${process.env.REACT_APP_API_URL}`
    })

    const token = localStorage.getItem('token')
    if (token) {
        axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`
    }
    axiosInstance.interceptors.response.use(
        (response) => response,
        (error) => {
            if (error.response.status === 401) {
                localStorage.removeItem('token')
                localStorage.removeItem('user')
                //location.reload()
            }
            return Promise.reject(error)
        }
    )

    return axiosInstance
}