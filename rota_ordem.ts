import { NextResponse } from "next/server"
import { PrismaClient } from "@prisma/client"

const prisma = new PrismaClient()

export async function POST(req: Request) {
  if (req.method === "POST") {
    try {
      const { currentDate, location, description, sector, priority, observations } = await req.json()

      const serviceOrder = await prisma.serviceOrder.create({
        data: {
          currentDate,
          location,
          description,
          sector,
          priority,
          observations,
        },
      })

      return NextResponse.json({ message: "Ordem de serviço gerada com sucesso.", serviceOrder }, { status: 201 })
    } catch (error) {
      console.error("Service order creation error:", error)
      return NextResponse.json({ error: "Erro ao gerar ordem de serviço." }, { status: 500 })
    }
  } else {
    return NextResponse.json({ error: "Method not allowed" }, { status: 405 })
  }
}

