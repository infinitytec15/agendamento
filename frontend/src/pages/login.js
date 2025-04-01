import { useState } from 'react'
import api from '../services/api'
import { setToken } from '../utils/auth'
import { useRouter } from 'next/router'

export default function Login() {
    const [form, setForm] = useState({ username: '', password: '' })
    const router = useRouter()

    const handleSubmit = async (e) => {
        e.preventDefault()
        const res = await api.post('/auth/login/', form)
        setToken(res.data.access)
        router.push('/dashboard')
    }

    return (
        <div>
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <input type="text" placeholder="Usuário" onChange={e => setForm({ ...form, username: e.target.value })} />
                <input type="password" placeholder="Senha" onChange={e => setForm({ ...form, password: e.target.value })} />
                <button type="submit">Entrar</button>
            </form>
        </div>
    )
}
