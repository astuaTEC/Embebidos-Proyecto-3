import { getEnvironments } from "./getEnvironments";


const { VITE_BASE_URL } = getEnvironments();


export const apiTakePhoto = async( ) => {
    const url = VITE_BASE_URL + "/home/getPhoto";
    
    try {
        const resp = await fetch(url, {
            method: "GET",
            redirect: "follow",
            cache: 'no-cache',
        })
        
        if(!resp.ok) throw new Error('No se pudo traer la imagen');

        const blob = await resp.blob();

        const src = URL.createObjectURL(blob);

        return src;

    } catch (error) {
        console.log(error);
        return null
    }

}
