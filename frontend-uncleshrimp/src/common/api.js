// const ApiRoot = `${window.location.origin}:5000`
export const ApiRoot = "http://localhost:5000"
export const userApi = `${ApiRoot}/api/users`
export const loginApi = `${ApiRoot}/api/auth`
export const productApi = `${ApiRoot}/api/products`
export const orderApi = `${ApiRoot}/api/orders`

export const baseHeaders = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
export const authHeaders = {
    ...baseHeaders,
    "Authorization": `Bearer ${localStorage.getItem("access_token")}`,
}
export const formHeaders = {
    "Authorization": `Bearer ${localStorage.getItem("access_token")}`
}

export const logOut = () => {
    localStorage.clear()
}