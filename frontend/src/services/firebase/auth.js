import firebase from './index';
import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
const auth = getAuth();

export const firebaseSignIn = async (userCredential) => {
    return await signInWithEmailAndPassword(auth, userCredential.email, userCredential.password)
    .then((credentials)=> {
        //console.log(credentials)
        const user = credentials.user
        console.log(user)
        return user
    })
    .catch(error => {
        throw error
    })
}