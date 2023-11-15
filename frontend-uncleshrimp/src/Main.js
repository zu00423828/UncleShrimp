import { HashRouter, Routes, Route, Navigate } from "react-router-dom"
import OrderManagement from "./OrderManagement/OrderManagement"
import ProductManagement from "./OrderManagement/OrderManagement"
const Main = ({ isAdmin, show }) => {
    const admin = (
        <HashRouter>
            <Routes>
                <Route key='root' path='/' element={<OrderManagement />} />
                <Route key="order-management" path="/admin/order" element={<OrderManagement />} />
                <Route key="product-management" path="/admin/product" element={<ProductManagement />} />
                <Route path="/"
                    element={<Navigate to="/" replace={true} />} />
            </Routes>
        </HashRouter>)

    const customer = (
        <HashRouter>
            <Routes>
                <Route key='root' path='/' element={<OrderManagement />} />
                <Route key="order-management" path="/admin/order" element={<OrderManagement />} />
                <Route key="product-management" path="/admin/product" element={<ProductManagement />} />
                <Route path="/"
                    element={<Navigate to="/" replace={true} />} />
            </Routes>
        </HashRouter>)

    return isAdmin ? admin : customer

}
export default Main