"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export default function ServiceOrder() {
  const [currentDate, setCurrentDate] = useState(new Date().toLocaleDateString("pt-BR"))
  const [location, setLocation] = useState("")
  const [description, setDescription] = useState("")
  const [sector, setSector] = useState("Ger.Operacional")
  const [priority, setPriority] = useState("Urgente")
  const [observations, setObservations] = useState("")

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    // Here you would typically make an API call to save the order
    console.log({ currentDate, location, description, sector, priority, observations })
    alert("Ordem de serviço gerada com sucesso.")
  }

  const handleClear = () => {
    setLocation("")
    setDescription("")
    setSector("Ger.Operacional")
    setPriority("Urgente")
    setObservations("")
    alert("Todos os campos foram limpos.")
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-2xl font-bold mb-6">Ordem de Serviço</h1>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md space-y-4">
        <div className="grid grid-cols-2 gap-4">
          <div>
            <Label htmlFor="date">Data de Abertura</Label>
            <Input id="date" value={currentDate} readOnly />
          </div>
          <div>
            <Label htmlFor="location">Local de Atendimento</Label>
            <Input id="location" value={location} onChange={(e) => setLocation(e.target.value)} required />
          </div>
        </div>
        <div>
          <Label htmlFor="description">Descrição do Serviço</Label>
          <Input id="description" value={description} onChange={(e) => setDescription(e.target.value)} required />
        </div>
        <div className="grid grid-cols-2 gap-4">
          <div>
            <Label htmlFor="sector">Setor</Label>
            <Select value={sector} onValueChange={setSector}>
              <SelectTrigger>
                <SelectValue placeholder="Selecione o setor" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="Ger.Operacional">Ger.Operacional</SelectItem>
                <SelectItem value="Recepção">Recepção</SelectItem>
                <SelectItem value="Governança">Governança</SelectItem>
                <SelectItem value="Manutenção">Manutenção</SelectItem>
                <SelectItem value="A&B">A&B</SelectItem>
                <SelectItem value="Eventos">Eventos</SelectItem>
                <SelectItem value="TI">TI</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div>
            <Label htmlFor="priority">Prioridade</Label>
            <Select value={priority} onValueChange={setPriority}>
              <SelectTrigger>
                <SelectValue placeholder="Selecione a prioridade" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="Sem urgência">Sem urgência</SelectItem>
                <SelectItem value="Urgente">Urgente</SelectItem>
                <SelectItem value="Avaliação">Avaliação</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>
        <div>
          <Label htmlFor="observations">Observações</Label>
          <Textarea
            id="observations"
            value={observations}
            onChange={(e) => setObservations(e.target.value)}
            className="h-32"
          />
        </div>
        <div className="flex justify-between">
          <Button type="button" variant="outline" onClick={handleClear}>
            Limpar Dados
          </Button>
          <Button type="submit">Salvar</Button>
        </div>
      </form>
    </div>
  )
}

