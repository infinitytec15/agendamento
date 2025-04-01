import { useEffect, useState } from 'react'
import api from '../../services/api'
import withAuth from '../../utils/withAuth'

function Dashboard() {
    const [metrics, setMetrics] = useState({})

    useEffect(() => {
        api.get('/dashboard/user/').then(res => setMetrics(res.data))
    }, [])

    return (
        <div>
            <h1>Meu Dashboard</h1>
            <ul>
                <li>Pendentes: {metrics.pending}</li>
                <li>Realizados: {metrics.done}</li>
                <li>Hoje: {metrics.today}</li>
                <li>Clientes: {metrics.total_clients}</li>
            </ul>
        </div>
    )
}

export default withAuth(Dashboard, 'user')
