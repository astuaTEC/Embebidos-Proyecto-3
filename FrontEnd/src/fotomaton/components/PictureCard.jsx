
export const PictureCard = ({ src, isLoading }) => {
    return (
        <>
            <img className="img-fluid rounded mx-auto d-block" src={ src } alt="Photo" />
        </>
    )
}
