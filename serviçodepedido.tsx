"use client"

import { useState } from "react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import { Textarea } from "@/components/ui/textarea"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export default function OrderService() {
  const [location, setLocation] = useState("")
  const [description, setDescription] = useState("")
  const [sector, setSector] = useState("")
  const [priority, setPriority] = useState("")
  const [observations, setObservations] = useState("")

  const handleSubmit = async (e) => {
    e.preventDefault()
    // Here you would typically make an API call to save the order
    // For now, we'll just log the order details
    console.log({ location, description, sector, priority, observations })
    alert("Order submitted successfully!")
  }

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-2xl font-bold mb-4">Service Order</h1>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-md space-y-4">
        <div>
          <Label htmlFor="location">Service Location</Label>
          <Input id="location" value={location} onChange={(e) => setLocation(e.target.value)} required />
        </div>
        <div>
          <Label htmlFor="description">Service Description</Label>
          <Input id="description" value={description} onChange={(e) => setDescription(e.target.value)} required />
        </div>
        <div>
          <Label htmlFor="sector">Sector</Label>
          <Select onValueChange={setSector}>
            <SelectTrigger>
              <SelectValue placeholder="Select a sector" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="operational">Operational</SelectItem>
              <SelectItem value="reception">Reception</SelectItem>
              <SelectItem value="maintenance">Maintenance</SelectItem>
              <SelectItem value="it">IT</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div>
          <Label htmlFor="priority">Priority</Label>
          <Select onValueChange={setPriority}>
            <SelectTrigger>
              <SelectValue placeholder="Select priority" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="urgent">Urgent</SelectItem>
              <SelectItem value="normal">Normal</SelectItem>
              <SelectItem value="low">Low</SelectItem>
            </SelectContent>
          </Select>
        </div>
        <div>
          <Label htmlFor="observations">Observations</Label>
          <Textarea id="observations" value={observations} onChange={(e) => setObservations(e.target.value)} />
        </div>
        <Button type="submit" className="w-full">
          Submit Order
        </Button>
      </form>
    </div>
  )
}

