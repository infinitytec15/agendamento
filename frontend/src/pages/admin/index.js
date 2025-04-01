import { useEffect, useState } from 'react'
import api from '../../services/api'
import withAuth from '../../utils/withAuth'

function AdminDashboard() {
    const [metrics, setMetrics] = useState({})

    useEffect(() => {
        api.get('/dashboard/admin/').then(res => setMetrics(res.data))
    }, [])

    return (
        <div>
            <h1>Admin Dashboard</h1>
            <ul>
                <li>Usuários Totais: {metrics.total_users}</li>
                <li>Ativos: {metrics.active_users}</li>
                <li>Assinantes: {metrics.subscribers}</li>
                <li>Agendamentos: {metrics.total_appointments}</li>
                <li>Faturamento R$: {metrics.total_revenue}</li>
            </ul>
        </div>
    )
}

export default withAuth(AdminDashboard, 'admin')
