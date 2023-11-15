import { Button, Table, Modal, ModalBody, ModalHeader, ModalFooter, Input } from "reactstrap";
import 'bootstrap/dist/css/bootstrap.css';
import { useState, useEffect } from "react";
import { orderApi, authHeaders } from "../common/api";
const OrderManagement = () => {
    const [orderData, setOrderData] = useState([])
    useEffect(() => { getOrderInfo() }, [])
    const [modal, setModal] = useState(false);
    const toggle = () => setModal(!modal);
    const [modifyOrder, setModifyOrder] = useState({})
    const getOrderInfo = () => {
        fetch(orderApi, {
            headers: authHeaders,
        })
            .then(res => { return res.json() })
            .then(result => { setOrderData(result) })
    }
    const updateOrderInfo = () => {
        fetch(`${orderApi}/${modifyOrder.id}`, {
            method: "PUT",
            headers: authHeaders,
            body: JSON.stringify({ "status": modifyOrder.status })
        })
            .then(res => {
                if (res.status === 200) {
                    return res.json()
                }
            })
            .then(result => {
                setOrderData((prev) => [...prev.filter(row => row.id !== result.id), result])
            })
    }
    const formatData = () => {
        const row = []
        if (orderData.length > 0) {
            orderData.sort((a, b) => a.id - b.id).forEach(item => {
                row.push(
                    <tr align="center">
                        <td><Button color="info" onClick={() => { toggle(); setModifyOrder({ id: item.id, status: item.status }) }}>編輯</Button></td>
                        <td>{item.id}</td>
                        <td><Button onClick={() => { userFomat(item.user_info) }} value={item.user_info}>客戶資訊</Button></td>
                        <td>{item.info}</td>
                        <td>{item.status}</td>
                        <td>{item.total}</td>
                    </tr >)
            })
        }
        return row
    }
    const userFomat = (data) => {
        alert(`姓名:${data.name}"\n電話:${data.phone}\n地址:${data.address}\n`)
    }
    const modifyStatus = () => {
        return (
            <Modal isOpen={modal} toggle={toggle} >
                <ModalHeader toggle={toggle}>
                    修改訂單狀態
                </ModalHeader>
                <ModalBody>
                    <Input
                        type="select"
                        name="status"
                        id="status"
                        onChange={(e) => { setModifyOrder({ id: modifyOrder.id, 'status': e.target.value }); }}
                        value={modifyOrder.status}
                    >
                        <option value="未出貨">未出貨</option>
                        <option value="已出貨">已出貨</option>
                        <option value="完成訂單">完成訂單</option>
                    </Input>
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" onClick={() => { toggle(); updateOrderInfo() }}>
                        儲存
                    </Button>{' '}
                    <Button color="secondary" onClick={toggle}>
                        取消
                    </Button>
                </ModalFooter>
            </Modal >)
    }

    const orderTable = (
        <Table>
            <thead>
                <tr align="center">
                    <th >
                        修改狀態
                    </th>
                    <th>
                        訂單號
                    </th>
                    <th>
                        客戶資訊
                    </th>
                    <th>
                        訂單資訊
                    </th>
                    <th>
                        狀態
                    </th>
                    <th>
                        總金額
                    </th>
                </tr>
            </thead>
            <tbody>
                {formatData()}
            </tbody>
        </Table>)
    return (
        <div>
            {orderTable}
            {modifyStatus()}
        </div>
    )
}

export default OrderManagement
