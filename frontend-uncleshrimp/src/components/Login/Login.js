import { Form, Button, Input, Label, FormGroup, Col, Container, Row,Modal,ModalHeader,ModalBody,ModalFooter } from "reactstrap"
import { useState } from "react"
import { loginApi, baseHeaders } from "../../common/api"
const ininLoginInfo = { account: "", password: "" }
const Login = ({ show, setLoginState }) => {
    const [loginInfo, setLoginInfo] = useState(ininLoginInfo)
    const [registerModel,setRegisterModel]=useState(false)
    const toggle=()=>setRegisterModel(!registerModel)
    const {registerInfo,setRegisterInfo}=useState({})
    // const
    const login = () => {
        fetch(loginApi, {
            method: "POST",
            headers: baseHeaders,
            body: JSON.stringify(loginInfo),
        })
            .then(res => { return res.json() })
            .then(result => {
                const info = {
                    "access_token": result.access_token,
                    "expiration_datetime": result.expiration_datetime,
                    "isLogin": true
                }
                localStorage.setItem("access_token", result.token)
                localStorage.setItem("expiration_datetime", result.expiration_datetime)
                localStorage.setItem("isLogin", true)
                setLoginState(info)
            })
    }
    const registerForm=[
            <Modal isOpen={registerModel} toggle={toggle} >
                <ModalHeader toggle={toggle}>
                    會員註冊
                </ModalHeader>
                <ModalBody>

                    <Form>
                        <FormGroup>
                            <Label>
                                *帳號
                            </Label>
                            <Input
                                id="account"
                                name="name"
                                type="str"
                                onChange={(e)=>setRegisterInfo({...registerInfo,accout:e.target.value})}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label>
                                *密碼
                            </Label>
                            <Input
                                id="password"
                                name="password"
                                type="password"
                                onChange={(e) => setRegisterInfo({ ...registerInfo, password: e.target.value })}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label >
                                *姓名
                            </Label>
                            <Input
                                id="name"
                                name="name"
                                type="str"
                                onChange={(e) => setRegisterInfo({ ...registerInfo, name: e.target.value })}
                            />
                        </FormGroup>
                        <FormGroup>
                            <Label >
                                *電話
                            </Label>
                            <Input
                                id="phone"
                                name="phone"
                                type="phone"
                                onChange={(e) => setRegisterInfo({ ...registerInfo, phone: e.target.value })}
                            />
                        </FormGroup>                        
                        <FormGroup>
                            <Label >
                                *地址
                            </Label>
                            <Input
                                id="address"
                                name="address"
                                type="textarea"
                                onChange={(e) => setRegisterInfo({ ...registerInfo, address: e.target.value })}
                            />
                        </FormGroup>
                    </Form>
                    
                </ModalBody>
                <ModalFooter>
                    <Button color="primary" >
                        註冊
                    </Button>{' '}
                    <Button color="secondary"  onClick={toggle}>
                        取消
                    </Button>
                </ModalFooter>
            </Modal >]
    const form = [
        <Container>
            <Row xs="3">
                <Col></Col>
                <Col>
                    <Form>
                        <FormGroup row>
                            <Label
                                // sm={1}
                            >
                                帳號:
                            </Label>
                            <Col sm={10}>
                                <Input
                                    id="accout"
                                    name="accout"
                                    type="str"
                                    onChange={(e) => setLoginInfo({ ...loginInfo, account: e.target.value })}
                                />
                            </Col>
                        </FormGroup>
                        <FormGroup row>
                            <Label
                                // sm={1}
                            >
                                密碼:
                            </Label>
                            <Col sm={10}>
                                <Input
                                    id="password"
                                    name="password"
                                    type="password"
                                    onChange={(e) => setLoginInfo({ ...loginInfo, password: e.target.value })}
                                />
                            </Col>
                        </FormGroup>
                        <Button color="success" onClick={login}>
                            登入
                        </Button><Label sm={1}/>
                        <Button color="primary" onClick={toggle}>
                            註冊
                        </Button>
                    </Form >
                </Col>
                <Col></Col>
            </Row>
        </Container >,
    ]
    return (
    <div>
        {show ? (form) : null}
        {registerForm}
    </div>)
}
export default Login