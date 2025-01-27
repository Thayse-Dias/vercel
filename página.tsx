"use client"

import { useState } from "react"
import Login from "../components/Login"
import Register from "../components/Register"
import ServiceOrder from "../components/ServiceOrder"

export default function Home() {
  const [isLoggedIn, setIsLoggedIn] = useState(false)
  const [showRegister, setShowRegister] = useState(false)

  if (isLoggedIn) {
    return <ServiceOrder />
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold text-center mb-6">
          Bem Vindo(a) ao Teela
          <br />
          Gerenciamento de Ordem de Serviço
        </h1>
        {showRegister ? (
          <Register onBack={() => setShowRegister(false)} onRegisterSuccess={() => setShowRegister(false)} />
        ) : (
          <Login onLogin={() => setIsLoggedIn(true)} onRegister={() => setShowRegister(true)} />
        )}
      </div>
    </div>
  )
}

