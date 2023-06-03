import React, { useState } from 'react'
import { apiTakePhoto } from '../../helpers/apiMethods';
import { PictureCard } from '../components';

export const CameraPage = () => {

    const [image, setImage] = useState();
    const [isLoading, setIsLoading] = useState(false);

    const onTakePhoto = async () => {
        setIsLoading(true);
        const res = await apiTakePhoto();
        setIsLoading(false);
        //const res = await fetch('https://picsum.photos/320/960');
        // const imageBlob = await res.blob();
        // const imageObjectURL = URL.createObjectURL(imageBlob);
        setImage(res);
    }

    return (
        <>
            <div className="container text-center">
                <h1>Fotomatón</h1>
            </div>
            <hr />

            <div className="row">
                <div className="col-md-8">
                    {
                        isLoading ? 
                        (<div className="d-flex justify-content-center">
                            <div className="spinner-border" role="status">
                            <span className="sr-only">Loading...</span>
                            </div>
                        </div>) : ''
                    } 
                </div>
                <div className="col-md-8">
                    {
                        !!image && !isLoading ? <PictureCard src={image} isLoading={isLoading} /> : ''
                    }
                </div>
                <div className="col-6 col-md-4">
                    <div className="d-grid gap-2">
                        <button onClick={async () => await onTakePhoto()} className='btn btn-primary btn-lg'>
                            Take Photo
                        </button>
                    </div>
                </div>
            </div>

        </>
    )
}
