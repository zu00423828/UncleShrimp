import { Button, Table, Modal, ModalBody, ModalHeader, ModalFooter, Input, Form, FormGroup, Label } from "reactstrap";
import { useState, useEffect } from "react";
import { productApi, ApiRoot, authHeaders } from "../common/api";
import 'bootstrap/dist/css/bootstrap.css';
const ProductManagement = () => {
    const initPorduct = { name: "", price: 0, depiction: "", image: null, display: false }
    const [productData, setProductData] = useState([])
    useEffect(() => { getproductInfo() }, [])

    const [modal, setModal] = useState(false);
    const toggle = () => setModal(!modal);
    const [addModal, setAddModal] = useState(false);
    const AddToggle = () => setAddModal(!addModal);
    const [product, setProduct] = useState(initPorduct)
    const [modifyProduct, setModifyProduct] = useState({})
    const getproductInfo = () => {
        fetch(productApi, {
            headers: authHeaders,
        })
            .then(res => { return res.json() })
            .then(result => { setProductData(result); console.log(result) })
    }
    const formatData = () => {
        const row = []
        if (productData.length > 0) {
            productData.sort((a, b) => a.id - b.id).forEach(item => {
                row.push(
                    <tr align="center">
                        <td><Button color="danger" onClick={() => { toggle(); setModifyProduct({ ...item }) }}>刪除</Button></td>
                        <td><Button color="info" onClick={() => { toggle(); setModifyProduct({ ...item }) }}>編輯</Button></td>
                        <td>{item.id}</td>
                        <td>{item.name}</td>
                        <td><img src={`${ApiRoot}/${item.image_path}`} height="100" alt={item.image_path}></img></td>
                        <td>{item.depiction}</td>
                        <td>{item.price}</td>
                        <td>{String(item.display)}</td>
                    </tr >)
            })
        }
        return row
    }
    const addProductInfo = () => {
        return (
            <Modal isOpen={addModal} toggle={AddToggle} >
                <ModalHeader toggle={AddToggle}>
                    新增商品
                </ModalHeader>
                <ModalBody>

                    <Form>
                        <FormGroup>
                            <Label>
                                *商品名稱
                            </Label>
                            <Input
                                id="name"
                                name="name"
                                type="str"
                                onChange={(e) => {
                                    setProduct({ ...product, name: e.target.value })
                                }}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label>
                                *金額
                            </Label>
                            <Input
                                id="exampleNumber"
                                name="number"
                                type="number"
                                onChange={(e) => {
                                    setProduct({ ...product, price: e.target.value })
                                }}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label >
                                *商品敘述
                            </Label>
                            <Input
                                id="depiction"
                                name="depiction"
                                type="textarea"
                                onChange={(e) => {
                                    setProduct({ ...product, depiction: e.target.value })
                                }}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="exampleFile">
                                *商品照片
                            </Label>
                            <Input
                                id="exampleFile"
                                name="file"
                                type="file"
                            />
                        </FormGroup>
                        <FormGroup switch >
                            <Label check>*顯示商品</Label>
                            <Input type="switch"
                                onChange={(e) => {
                                    setProduct({ ...product, display: e.target.value })
                                }}
                            />
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={() => { AddToggle(); }}>
                        新增
                    </Button>{' '}
                    <Button color="secondary" onClick={AddToggle}>
                        取消
                    </Button>
                </ModalFooter>
            </Modal >)
    }
    const modifyProductInfo = () => {
        console.log(modifyProduct)
        return (
            <Modal isOpen={modal} toggle={toggle} >
                <ModalHeader toggle={toggle}>
                    修改商品
                </ModalHeader>
                <ModalBody>

                    <Form>
                        <FormGroup>
                            <Label>
                                商品名稱
                            </Label>
                            <Input
                                id="name"
                                name="name"
                                type="str"
                                value={modifyProduct.name}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label>
                                金額
                            </Label>
                            <Input
                                id="price"
                                name="price"
                                type="number"
                                value={modifyProduct.price}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label >
                                商品敘述
                            </Label>
                            <Input
                                id="depiction"
                                name="depiction"
                                type="textarea"
                                value={modifyProduct.depiction}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label for="exampleFile">
                                商品照片
                            </Label>
                            <Input
                                id="product-img"
                                name="product-img"
                                type="file"
                            />
                        </FormGroup>
                        <FormGroup switch disabled>
                            <Input type="switch" />
                            <Label check>顯示商品</Label>
                        </FormGroup>
                    </Form>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={() => { toggle() }}>
                        儲存
                    </Button>{' '}
                    <Button color="secondary" onClick={toggle}>
                        取消
                    </Button>
                </ModalFooter>
            </Modal >)
    }
    const porductTable = (
        <Table>
            <thead>
                <tr align="center">
                    <th>刪除</th>
                    <th>編輯</th>
                    <th>
                        商品編號
                    </th>
                    <th>
                        商品名稱
                    </th>
                    <th>商品照片</th>
                    <th>
                        商品敘述
                    </th>
                    <th>
                        金額
                    </th>
                    <th>
                        顯示
                    </th>
                </tr>
            </thead>
            <tbody>
                {formatData()}
            </tbody>
        </Table>)
    return (
        <div>
            {<Button color="danger" onClick={AddToggle}>新增商品</Button>}
            {porductTable}
            {addProductInfo()}
            {modifyProductInfo()}
        </div>
    )
}

export default ProductManagement
