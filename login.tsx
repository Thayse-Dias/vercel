"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Checkbox } from "@/components/ui/checkbox"

export default function Login({ onLogin, onRegister }) {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically make an API call to verify credentials
    // For now, we'll just simulate a successful login
    onLogin()
  }

  return (
    <form onSubmit={handleLogin} className="space-y-4">
      <h2 className="text-xl font-bold text-center">Faça seu Login</h2>
      <div>
        <Label htmlFor="email">E-mail do Usuário</Label>
        <Input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        <p className="text-xs text-gray-500 mt-1">*O campo e-mail é de caráter obrigatório.</p>
      </div>
      <div>
        <Label htmlFor="password">Senha do Usuário</Label>
        <Input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
        <p className="text-xs text-gray-500 mt-1">*O campo senha de usuário é de caráter obrigatório.</p>
      </div>
      <div className="flex items-center space-x-2">
        <Checkbox id="remember" />
        <label
          htmlFor="remember"
          className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
        >
          Lembrar-me
        </label>
      </div>
      <Button type="submit" className="w-full">
        Entrar
      </Button>
      <div className="text-center">
        <p className="text-sm">Não possui conta?</p>
        <Button variant="outline" className="mt-2" onClick={onRegister}>
          Cadastre-se
        </Button>
      </div>
    </form>
  )
}

