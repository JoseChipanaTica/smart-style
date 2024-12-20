import type { Metadata } from 'next'
import localFont from 'next/font/local'
import { ToastContainer } from 'react-toastify'
import 'react-toastify/dist/ReactToastify.css'
import './globals.css'

const geistSans = localFont({
  src: './fonts/GeistVF.woff',
  variable: '--font-geist-sans',
  weight: '100 900'
})
const geistMono = localFont({
  src: './fonts/GeistMonoVF.woff',
  variable: '--font-geist-mono',
  weight: '100 900'
})

export const metadata: Metadata = {
  title: 'Smart-Style',
  description: 'Smart Style is a web application that generates style from clothing images'
}

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body className={`${geistSans.variable} ${geistMono.variable} antialiased`}>
        <div className="h-screen w-screen overflow-auto md:overflow-hidden">
          <div className="w-full h-full p-4 md:p-8">
            <div
              className="flex flex-col md:flex-row w-full h-full text-sm text-left
              text-white border border-gray-600/50 rounded-3xl space-y-4 md:space-y-0 overflow-auto md:overflow-hidden"
            >
              {children}
            </div>
          </div>
        </div>
        <ToastContainer />
      </body>
    </html>
  )
}
