"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Checkbox } from "@/components/ui/checkbox"

export default function Register({ onBack, onRegisterSuccess }) {
  const [username, setUsername] = useState("")
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [confirmPassword, setConfirmPassword] = useState("")

  const handleRegister = async (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically make an API call to register the user
    // For now, we'll just simulate a successful registration
    onRegisterSuccess()
  }

  return (
    <form onSubmit={handleRegister} className="space-y-4">
      <h2 className="text-xl font-bold text-center">Cadastro de Usuário</h2>
      <p className="text-sm text-center text-gray-500">*Preencha todos os campos com dados corretos</p>
      <div>
        <Label htmlFor="username">Nome do Usuário</Label>
        <Input id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
      </div>
      <div>
        <Label htmlFor="email">E-mail do Usuário</Label>
        <Input id="email" type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <div>
        <Label htmlFor="password">Senha do Usuário</Label>
        <Input id="password" type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>
      <div>
        <Label htmlFor="confirmPassword">Confirme sua senha</Label>
        <Input
          id="confirmPassword"
          type="password"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
      </div>
      <div className="flex items-center space-x-2">
        <Checkbox id="terms" required />
        <label
          htmlFor="terms"
          className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
        >
          Aceito todos os Termos e Política
        </label>
      </div>
      <Button type="submit" className="w-full">
        Salvar
      </Button>
      <Button variant="outline" className="w-full" onClick={onBack}>
        Voltar
      </Button>
    </form>
  )
}

