import React, { useState } from 'react'
import { apiTakePhoto } from '../../helpers/apiMethods';
import { PictureCard } from '../components';

export const CameraPage = () => {

    const [image, setImage] = useState();

    const onTakePhoto = async () => {
        //const res = await apiTakePhoto();
        const res = await fetch('https://picsum.photos/500');
        const imageBlob = await res.blob();
        const imageObjectURL = URL.createObjectURL(imageBlob);
        setImage(imageObjectURL);
    }

    return (
        <>
            <div class="container text-center">
                <h1>Fotomatón</h1>
            </div>
            <hr />


            <div className="row">
                <div className="col-md-8">
                    {
                        !!image ? <PictureCard src={image} /> : ''
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
