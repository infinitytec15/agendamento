import { useRouter } from 'next/router'
import { useEffect } from 'react'
import { getToken } from './auth'

export default function withAuth(Component, role) {
    return function AuthenticatedComponent(props) {
        const router = useRouter()
        useEffect(() => {
            const token = getToken()
            if (!token) router.push('/login')
            if (role === 'admin' && !props.user?.is_admin) router.push('/dashboard')
        }, [])
        return <Component {...props} />
    }
}
