import 'bootstrap/dist/css/bootstrap.css';
import { Nav, NavItem, NavLink, Button } from 'reactstrap';
import { logOut } from "../common/api"
const Header = ({ admin, show }) => {
    const adminHeader = [
        <Nav fill pills>
            <NavItem >
                <NavLink href="/#/admin/order" >訂單管理</NavLink>
            </NavItem>
            <NavItem>
                <NavLink href="/#/admin/product">商品管理</NavLink>
            </NavItem>
            <NavItem>
                <Button onClick={logOut}>登出</Button>
            </NavItem>
        </Nav>]
    const customerHeader = [
        <Nav fill pills>
            <NavItem >
                <NavLink href="/shop" >購買</NavLink>
            </NavItem>
            <NavItem>
                <NavLink href="/order">訂單</NavLink>
            </NavItem>
            <NavItem>
                <Button onClick={logOut}>登出</Button>
            </NavItem>
        </Nav>]
    const NullHeader = [
        <Nav fill pills>
            <NavItem >
                {"\xa0\xa0\xa0\xa0\xa0\xa0\xa0"}
            </NavItem>
        </Nav>]
    if (show)
        return (admin ? adminHeader : customerHeader)
    return (NullHeader)

}
export default Header