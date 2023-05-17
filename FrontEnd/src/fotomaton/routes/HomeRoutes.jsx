import { Navigate, Route, Routes } from "react-router-dom"
import { Navbar } from "../../ui"
import { CameraPage } from "../pages"


export const HomeRoutes = () => {
    return (
        <>
            <Navbar />

            <div className="container">
                <Routes>
                    <Route path="home" element={<CameraPage />} />

                    <Route path="/*" element={<Navigate to="home" replace/>} />
                </Routes>

            </div>

        </>
    )
}
