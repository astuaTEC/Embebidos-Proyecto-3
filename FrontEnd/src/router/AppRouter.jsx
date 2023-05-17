import { Route, Routes } from "react-router-dom"
import { LoginPage } from "../auth"
import { HomeRoutes } from "../fotomaton"
import { PrivateRoute } from "./PrivateRoute"
import { PublicRoute } from "./PublicRoute"

export const AppRouter = () => {
    return (
        <>

            <Routes>

                <Route path="login" element={
                    <PublicRoute>
                        <LoginPage />
                    </PublicRoute>
                } />

                <Route path="/*" element={
                    <PrivateRoute>
                        <HomeRoutes />
                    </PrivateRoute>
                } />

            </Routes>
        </>
    )
}
