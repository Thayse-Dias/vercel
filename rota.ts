import { NextResponse } from "next/server"
import bcrypt from "bcrypt"
import { PrismaClient } from "@prisma/client"

const prisma = new PrismaClient()

export async function POST(req: Request) {
  if (req.method === "POST") {
    try {
      const { username, email, password } = await req.json()

      // Check if user already exists
      const existingUser = await prisma.user.findUnique({
        where: { email },
      })

      if (existingUser) {
        return NextResponse.json({ error: "E-mail já cadastrado." }, { status: 400 })
      }

      // Hash the password
      const hashedPassword = await bcrypt.hash(password, 10)

      // Create new user
      const user = await prisma.user.create({
        data: {
          username,
          email,
          password: hashedPassword,
        },
      })

      return NextResponse.json({ message: "Usuário cadastrado com sucesso." }, { status: 201 })
    } catch (error) {
      console.error("Registration error:", error)
      return NextResponse.json({ error: "Erro ao cadastrar usuário." }, { status: 500 })
    }
  } else {
    return NextResponse.json({ error: "Method not allowed" }, { status: 405 })
  }
}

