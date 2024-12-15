export async function POST(request: Request) {
  try {
    const formData = await request.formData()

    const response = await fetch(`${process.env.BACKEND_URL}/clothing`, {
      method: 'POST',
      body: formData
    })

    if (response.status !== 200) {
      return new Response(response.statusText, { status: response.status })
    }

    const data = await response.json()

    return new Response(JSON.stringify(data), { status: 200 })
  } catch (error: any) {
    console.error(error)
    return new Response(error, { status: 500 })
  }
}
